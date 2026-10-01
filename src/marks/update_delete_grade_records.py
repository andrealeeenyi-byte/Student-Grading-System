def update_grade_record():
    print("\n=== Update Grade Record ===")
    grades = load_grades()
    students = load_students()
    courses = load_courses()
    exams = load_exams()

    if not students:
        print("Student record" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
              ". Please" + TextColors.CYAN_BOLD + " SELECT 1 " + TextColors.RESET +
              "to add students first.")
        return

    if not courses:
        print("Course record" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
              ". Please" + TextColors.CYAN_BOLD + " SELECT 2 " + TextColors.RESET + "to add courses first.")
        return

    if not grades:
        print(TextColors.RED_BOLD + "No grade records " + TextColors.RESET + "to update." +
              " Please " + TextColors.CYAN_BOLD + "SELECT 4 " + TextColors.RESET + "to record grades first.")
        return

    # Display existing grade records
    print("\nExisting Grade Records:")
    i = 1
    for grade in grades:
        student_name = students.get(grade["student_id"], {}).get("name", "Unknown Student")
        course_name = courses.get(grade["course_id"], "Unknown Course")
        test_name = grade.get("test_name", "General")
        print(f"{i:3}. Student ID: {grade['student_id']}")
        print(f"     Student Name: {student_name}")
        print(f"     Course ID: {grade['course_id']}")
        print(f"     Course Name: {course_name}")
        print(f"     Exam: {test_name}")
        print(f"     Marks: {grade['marks_display']}, Grade: {grade['grade']}\n")
        i += 1

    while True:
        sid = input("Enter Student ID to update or 'Q' to quit: ").strip()

        if sid.upper() == 'Q':
            print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
            return

        if sid not in students:
            print("Student ID" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Student ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit." + TextColors.RESET)
            continue

        # Get student's grade records
        student_records = [rec for rec in grades if rec["student_id"] == sid]
        if not student_records:
            print("No grade records found for student" + TextColors.RED_BOLD + f" {sid}" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "different Student ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit." + TextColors.RESET)
            continue

        print(f"\nCourses for {students[sid]['name']} ({sid}):")
        unique_courses = set(rec["course_id"] for rec in student_records)
        for course_id in unique_courses:
            course_name = courses.get(course_id, "Unknown Course")
            print(f"- {course_id}: {course_name}")

        while True:
            cid = input("\nEnter Course ID to update or 'Q' to quit: ").strip()

            if cid.upper() == 'Q':
                print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
                return

            if cid not in unique_courses:
                print("Course ID" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
                      " for this student. Please enter a " + TextColors.CYAN_BOLD + "valid Course ID" + TextColors.RESET +
                      " or " + TextColors.CYAN_BOLD + "'Q' to quit." + TextColors.RESET)
                continue
            break

        # Get student's records for this course
        student_course_records = [rec for rec in student_records if rec["course_id"] == cid]

        rec = None

        # If multiple tests for this course, let user choose which one to update
        if len(student_course_records) > 1:
            print(f"\nMultiple test records found for {students[sid]['name']} in {courses[cid]}:")
            i = 1
            for r in student_course_records:
                test_name = r.get("test_name", "General")
                print(f"{i}. {test_name}: {r['marks_display']}, Grade: {r['grade']}")
                i += 1

            while True:
                try:
                    test_choice_input = input(f"\nSelect test to update (1-{len(student_course_records)}) or 'Q' to quit: ").strip()
                    if test_choice_input.upper() == 'Q':
                        print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
                        return
                    choice_int = int(test_choice_input)
                    if 1 <= choice_int <= len(student_course_records):
                        rec = student_course_records[choice_int - 1]
                        break
                    else:
                        print(f"Please enter a number between {TextColors.CYAN_BOLD}1 and {len(student_course_records)}{TextColors.RESET}.")
                except ValueError:
                    print("Please enter a " + TextColors.CYAN_BOLD + "valid number." + TextColors.RESET)
        else:
            # Only one record for this course, select it automatically
            rec = student_course_records[0]

        test_name = rec.get("test_name", "General")

        # Parse the marks string
        try:
            marks_str = rec['marks_display']
            if '/' in marks_str:
                actual_str, max_str = marks_str.split('/')
                actual_marks = float(actual_str)
                max_marks = float(max_str)
                percentage = (actual_marks / max_marks) * 100
            else:

                # For backward compatibility with old format
                actual_marks = float(marks_str)
                max_marks = 100
                percentage = actual_marks

            print(f"\nStudent: {students[sid]['name']} ({sid})")
            print(f"Course: {courses[cid]} ({cid})")
            if test_name != "General":
                print(f"Test: {test_name}")
            print(f"Current: Marks = {marks_str}, Grade = {rec['grade']}")

            # Get max marks for this test
            if test_name != "General" and cid in exams:
                for exam in exams[cid]:
                    if exam['test_name'] == test_name:
                        max_marks = exam['marks_ratio']
                        break

            # Get new marks
            print(f"\nEnter new marks for {test_name} (maximum: {max_marks:.0f}):")
            while True:
                try:
                    new_actual_marks = float(input(f"Enter marks (0-{max_marks:.0f}): ").strip())
                    if 0 <= new_actual_marks <= max_marks:
                        break
                    else:
                        print(f"Marks must be between {TextColors.CYAN_BOLD}0 and {max_marks:.0f}{TextColors.RESET}.")
                except ValueError:
                    print("Please enter a " + TextColors.CYAN_BOLD + "valid number." + TextColors.RESET)

            # Calculate percentage and grade
            new_percentage = (new_actual_marks / max_marks) * 100
            new_grade = calculate_grade(new_percentage)

            # Format marks for storage
            if test_name != "General":
                new_marks_str = f"{new_actual_marks:.1f}/{max_marks:.0f}"
            else:
                new_marks_str = f"{new_actual_marks:.1f}"


            # Display existing marks with color coding
            if percentage >= 70:
                displayed_colored_marks = (f"{TextColors.GREEN_BOLD}{marks_str}{TextColors.RESET}")
            elif percentage >= 40:
                displayed_colored_marks = (f"{TextColors.YELLOW_BOLD}{marks_str}{TextColors.RESET}")
            else:
                displayed_colored_marks = (f"{TextColors.RED_BOLD}{marks_str}{TextColors.RESET}")

            # Colored marks for new marks
            if new_percentage >= 70:
                new_colored_marks = (f"{TextColors.GREEN_BOLD}{new_marks_str}{TextColors.RESET}")
            elif new_percentage >= 40:
                new_colored_marks = (f"{TextColors.YELLOW_BOLD}{new_marks_str}{TextColors.RESET}")
            else:
                new_colored_marks = (f"{TextColors.RED_BOLD}{new_marks_str}{TextColors.RESET}")

            # Show changes
            print(f"\nChanges to be made:")
            print(f"Old Marks: {displayed_colored_marks}")
            print(f"New Marks: {new_colored_marks}")
            print(f"Old Grade: {rec['grade']}")
            print(f"New Grade: {new_grade}")

            # Confirm update
            confirm = input("\nConfirm update? (Y/N): ").strip().upper()

            while confirm not in ("Y", "N"):
                print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                      "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
                      " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
                confirm = input("Confirm update? (Y/N): ").strip().upper()

            if confirm == "Y":
                rec["marks_display"] = new_marks_str
                rec["grade"] = new_grade
                save_grades(grades)
                print("Grade record updated" + TextColors.GREEN_BOLD + " SUCCESSFULLY." + TextColors.RESET)
                return
            else:
                print(TextColors.RED_BOLD + "Update cancelled." + TextColors.RESET + " No changes made.")
                return

        except (ValueError, ZeroDivisionError) as e:
            print(f"{TextColors.RED_BOLD}Invalid marks format {TextColors.RESET}in record: {marks_str}")
            continue

def delete_grade_record():
    print("\n=== Delete Grade Record ===")
    grades = load_grades()
    students = load_students()
    courses = load_courses()

    if not students:
        print("Student record" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
              ". Please" + TextColors.CYAN_BOLD + " SELECT 1 " + TextColors.RESET +
              "to add students first.")
        return

    if not courses:
        print("Course record" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
              ". Please" + TextColors.CYAN_BOLD + " SELECT 2 " + TextColors.RESET + "to add courses first.")
        return

    if not grades:
        print(TextColors.RED_BOLD + "No grade records " + TextColors.RESET + "to delete." +
              " Please " + TextColors.CYAN_BOLD + "SELECT 4 " + TextColors.RESET + "to record grades first.")
        return

    # Display existing grade records
    print("\nExisting Grade Records:")
    i = 1
    for grade in grades:
        student_name = students.get(grade["student_id"], {}).get("name", "Unknown Student")
        course_name = courses.get(grade["course_id"], "Unknown Course")
        test_name = grade.get("test_name", "General")
        print(f"{i:3}. Student ID: {grade['student_id']}")
        print(f"     Student Name: {student_name}")
        print(f"     Course ID: {grade['course_id']}")
        print(f"     Course Name: {course_name}")
        print(f"     Exam: {test_name}")
        print(f"     Marks: {grade['marks_display']}, Grade: {grade['grade']}\n")
        i += 1

    while True:
        sid = input("\nEnter Student ID to delete grade from or 'Q' to quit: ").strip()

        if sid.upper() == 'Q':
            print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
            return

        if sid not in students:
            print("Student ID" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Student ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit." + TextColors.RESET)
            continue

        # Get student's grade records
        student_records = [rec for rec in grades if rec["student_id"] == sid]
        if not student_records:
            print("No grade records found for student" + TextColors.RED_BOLD + f" {sid}" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "different Student ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit." + TextColors.RESET)
            continue

        print(f"\nCourses for {students[sid]['name']} ({sid}):")
        unique_courses = set(rec["course_id"] for rec in student_records)
        for course_id in unique_courses:
            course_name = courses.get(course_id, "Unknown Course")
            print(f"- {course_id}: {course_name}")

        while True:
            cid = input("\nEnter Course ID to delete from or 'Q' to quit: ").strip()

            if cid.upper() == 'Q':
                print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
                return

            if cid not in unique_courses:
                print("Course ID" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
                      " for this student. Please enter a " + TextColors.CYAN_BOLD + "valid Course ID" + TextColors.RESET +
                      " or " + TextColors.CYAN_BOLD + "'Q' to quit." + TextColors.RESET)
                continue
            break

        # Get student's records for this course
        student_course_records = [rec for rec in student_records if rec["course_id"] == cid]

        record_to_delete = None

        # If multiple records, let user choose which one
        if len(student_course_records) > 1:
            print(f"\nMultiple test records found for {students[sid]['name']} in {courses[cid]}:")
            i = 1
            for r in student_course_records:
                test_name = r.get("test_name", "General")
                print(f"{i}. {test_name}: {r['marks_display']}, Grade: {r['grade']}")
                i += 1

            while True:
                try:
                    test_choice_input = input(f"\nSelect test to delete (1-{len(student_course_records)}) or 'Q' to quit: ").strip()

                    if test_choice_input.upper() == 'Q':
                        print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
                        return

                    choice_int = int(test_choice_input)
                    if 1 <= choice_int <= len(student_course_records):
                        record_to_delete = student_course_records[choice_int - 1]
                        break
                    else:
                        print(f"Please enter a number between {TextColors.CYAN_BOLD}1 and {len(student_course_records)}{TextColors.RESET}.")
                except ValueError:
                    print("Please enter a " + TextColors.CYAN_BOLD + "valid number." + TextColors.RESET)
        else:
            record_to_delete = student_course_records[0]

        # Parse marks for display
        marks_str = record_to_delete['marks_display']
        test_name = record_to_delete.get("test_name", "General")

        # Calculate percentage for color coding
        try:
            if '/' in marks_str:
                actual_str, max_str = marks_str.split('/')
                actual_marks = float(actual_str)
                max_marks = float(max_str)
                percentage = (actual_marks / max_marks) * 100
            else:
                percentage = float(marks_str)

            if percentage >= 70:
                displayed_colored_marks = (f"{TextColors.GREEN_BOLD}{marks_str}{TextColors.RESET}")
            elif percentage >= 40:
                displayed_colored_marks = (f"{TextColors.YELLOW_BOLD}{marks_str}{TextColors.RESET}")
            else:
                displayed_colored_marks = (f"{TextColors.RED_BOLD}{marks_str}{TextColors.RESET}")
        except:
            displayed_colored_marks = marks_str

        print(f"\nRecord to delete:")
        print(f"- Student: {students[sid]['name']} ({sid})")
        print(f"- Course: {courses[cid]} ({cid})")
        if test_name != "General":
            print(f"- Test: {test_name}")
        print(f"- Marks: {displayed_colored_marks}")
        print(f"- Grade: {record_to_delete['grade']}")

        # Ask for confirmation
        confirm = input("\nAre you sure you want to delete this grade record? (Y/N): ").strip().upper()

        while confirm not in ("Y", "N"):
            print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                  "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
                  " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
            confirm = input("Are you sure you want to delete this grade record? (Y/N): ").strip().upper()

        if confirm == "Y":
            # Remove the specific record
            new_grades = [rec for rec in grades if not (
                rec["student_id"] == sid and
                rec["course_id"] == cid and
                rec.get("test_name", "General") == test_name
            )]
            save_grades(new_grades)
            print("Grade record deleted" + TextColors.GREEN_BOLD + " SUCCESSFULLY." + TextColors.RESET)
            return
        else:
            print(TextColors.RED_BOLD + "Deletion cancelled." + TextColors.RESET + " No changes made.")
            return