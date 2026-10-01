def record_student_marks():
    print("\n=== Record Student Marks ===")
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

    # Display existing students
    print("\nExisting Students:")
    i = 1
    for sid, student_info in students.items():
        print(f"{i:3}. Student ID: {sid}\n     Student Name:  {student_info['name']}\n     Student Email: {student_info['email']}")
        print()
        i  += 1

    while True:
        sid = input("Enter Student ID (or 'Q' to quit): ").strip().upper()

        if sid == 'Q':
            print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
            return

        if sid not in students:
            print("Student ID" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Student ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit" + TextColors.RESET + "." )
            continue
        break

    print("\nAvailable Courses:")
    i = 1
    for cid_key, cname in courses.items():
      print(f"{i:3}. Course ID: {cid_key}\n     Course Name: {cname}")
      print()
      i  += 1

    while True:
        cid = input("Enter Course ID (or 'Q' to quit): ").strip()

        if cid.upper() == 'Q':
            print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
            return

        if cid not in courses:
            print("Course ID" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Course ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit" + TextColors.RESET + "." )
            continue
        break

    # Show available test
    exams_data = load_exams()

    if cid in exams_data and exams_data[cid]:
        print(f"\nAvailable Tests for {courses[cid]}:")
        for i, exam in enumerate(exams_data[cid], 1):
            max_marks = exam['marks_ratio']
            print(f"{i}. {exam['test_name']} (/{max_marks:.0f})")
    else:
      print(f"{TextColors.RED_BOLD}No exam details found{TextColors.RESET} for course {courses[cid]}. Please{TextColors.CYAN_BOLD} add exam details first{TextColors.RESET}.")
      return

    # Ask user choose test
    while True:
        try:
            test_choice = int(input(f"\nSelect test (1-{len(exams_data[cid])}): "))
            if 1 <= test_choice <= len(exams_data[cid]):
                selected_test = exams_data[cid][test_choice - 1]
                break
            else:
                print(f"Please enter a number between {TextColors.CYAN_BOLD}1 and {len(exams_data[cid])}{TextColors.RESET}.")
        except ValueError:
            print(f"Please {TextColors.CYAN_BOLD}enter a valid number{TextColors.RESET}.")

    test_name = selected_test['test_name']
    max_marks = selected_test['marks_ratio']

   # Check for existing record before input marks
    grades = load_grades()
    existing = None
    for record in grades:
        if (record["student_id"] == sid and
            record["course_id"] == cid and
            record.get("test_name", "General") == test_name):
            existing = record
            break

    # Show current result if exists
    if existing:
        if '/' in existing['marks_display']:
            current_marks_str, max_str = existing['marks_display'].split('/')
            try:
                current_marks = float(current_marks_str)
                max_marks_current = float(max_str)  # Renamed to avoid conflict
                current_percentage = (current_marks / max_marks_current) * 100

                if current_percentage >= 70:
                    marks_color = TextColors.GREEN_BOLD
                elif current_percentage >= 40:
                    marks_color = TextColors.YELLOW_BOLD
                else:
                    marks_color = TextColors.RED_BOLD

                print(f"Current result for {test_name}: {marks_color}{existing['marks_display']}{TextColors.RESET}")
                print(f"Current Grade: {existing['grade']}")
            except:
                print(f"Current result for {test_name}: {existing['marks_display']}")
                print(f"Current Grade: {existing['grade']}")
        else:
            print(f"Current result for {test_name}: {existing['marks_display']}")
            print(f"Current Grade: {existing['grade']}")

        choice = input("Do you want to overwrite it? (Y/N): ").strip().upper()

        while choice not in ("Y", "N"):
            print(TextColors.RED_BOLD + "Invalid choice! " + TextColors.RESET +
                            "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
                            " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
            choice = input("Do you want to overwrite it? (Y/N): ").strip().upper()

        if choice == "N":
            print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
            return
    else:
        # No existing record. Ask if user wants to create a new record
        print(f"{TextColors.RED_BOLD}No existing record found {TextColors.RESET}for {test_name}.")
        choice = input("Do you want to create a new record? (Y/N): ").strip().upper()

        while choice not in ("Y", "N"):
            print(TextColors.RED_BOLD + "Invalid choice! " + TextColors.RESET +
                            "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
                            " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
            choice = input("Do you want to create a new record? (Y/N): ").strip().upper()

        if choice == "N":
            print(TextColors.RED_BOLD + "Operation cancelled" + TextColors.RESET +
                  ". No record created.")
            return

    # Ask user to input marks
    print(f"\nEnter marks for {test_name}:")

    while True:
        try:
            marks_input = input(f"Enter marks (/{max_marks:.0f}): ").strip()
            actual_marks = float(marks_input)

            if 0 <= actual_marks <= max_marks:
                # Calculate percentage for grade calculation
                percentage = (actual_marks / max_marks) * 100

                grade_with_color = calculate_grade(percentage)

                # Determine color based on percentage
                if percentage >= 70:
                    marks_color = TextColors.GREEN_BOLD
                elif percentage >= 40:
                    marks_color = TextColors.YELLOW_BOLD
                else:
                    marks_color = TextColors.RED_BOLD

                break
            else:
                print(f"Marks must be between {TextColors.CYAN_BOLD}0 and {max_marks:.0f}{TextColors.RESET}.")
        except ValueError:
            print(f"Please {TextColors.CYAN_BOLD}enter a valid number{TextColors.RESET}.")

    # For display purposes only
    formatted_display = f"{actual_marks:.0f}/{max_marks:.0f}"

    # Save the record
    if existing:
        #  existing record
        existing["marks_display"] = formatted_display
        existing["marks_numeric"] = actual_marks
        existing["grade"] = grade_with_color
        existing["test_name"] = test_name
        save_grades(grades)
        print("Record updated" + TextColors.GREEN_BOLD + " SUCCESSFULLY" + TextColors.RESET)
    else:
        # Create new record
        new_record = {
            "student_id": sid,
            "course_id": cid,
            "marks_display": formatted_display,
            "marks_numeric": actual_marks,
            "grade": grade_with_color,
            "test_name": test_name
        }
        grades.append(new_record)
        save_grades(grades)
        print("Marks recorded" + TextColors.GREEN_BOLD + " SUCCESSFULLY." + TextColors.RESET)