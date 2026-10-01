def update_exam_details():
    print("\n=== Update Exam Details ===")
    courses = load_courses()
    exams = load_exams()
    grades = load_grades()

    if not courses:
        print("Course record" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
              ". Please" + TextColors.CYAN_BOLD + " SELECT 2 " + TextColors.RESET +
              "to add courses first.")
        return

    if not exams:
        print("Exam record" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
              ". Please" + TextColors.CYAN_BOLD + " SELECT 3 " + TextColors.RESET +
              "to add exam details first.")
        return

    # Display existing exams
    print("\nExisting Exams:")
    for cid, course_exams in exams.items():
        if course_exams:
            course_name = courses.get(cid, "Unknown Course")
            print(f"\nCourse Name: {course_name} \nCourse ID:{cid}")
            i = 1
            for exam in course_exams:
                print(f"  {i:3}. Exam Name: {exam['test_name']}\n       Marks Ratio: {exam['marks_ratio']}%")
                print()
                i += 1

    while True:
        cid = input("Enter Course ID to update or 'Q' to quit: ").strip()

        if cid.upper() == 'Q':
            print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
            return

        if len(cid) != 4 or not cid.isdigit():
            print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                  "Course ID must be" + TextColors.CYAN_BOLD + " 4 numerical digits" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Course ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit." + TextColors.RESET)
            continue

        if cid not in exams or not exams[cid]:
            print("Course ID" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
                  " or " + TextColors.RED_BOLD + "has no exams" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Course ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit" + TextColors.RESET + ".")
            continue

        break

    print(f"\nExams for {courses.get(cid, 'Unknown Course')}:")
    i = 1
    for exam in exams[cid]:
        print(f"{i}. {exam['test_name']} ({exam['marks_ratio']}%)")
        i += 1

    while True:
        try:
            exam_num = int(input("\nSelect exam number to update: "))
            if 1 <= exam_num <= len(exams[cid]):
                break
            else:
                print(f"Please enter a number between {TextColors.CYAN_BOLD}1 and {len(exams[cid])}{TextColors.RESET}.")
        except ValueError:
            print("Please enter a " + TextColors.CYAN_BOLD + "valid number." + TextColors.RESET)

    selected_exam = exams[cid][exam_num - 1]
    old_test_name = selected_exam['test_name']
    old_ratio = selected_exam['marks_ratio']

    print(f"\nCurrent details for exam:")
    print(f"1. Test Name: {old_test_name}")
    print(f"2. Marks Ratio: {old_ratio}%")

    # Ask what to update
    while True:
        choice = input("\nWhat would you like to update? \n1: Test Name \n2: Marks Ratio \n3: Both (Test Name & Marks Ratio) \n'Q': quit \nSelect (1/2/3/Q): ").strip()

        if choice.upper() == 'Q':
            print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
            return

        if choice in ['1', '2', '3']:
            break
        else:
            print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                  "Please enter: " +
                  TextColors.CYAN_BOLD + "\n'1'" + TextColors.RESET + ": Test Name " +
                  TextColors.CYAN_BOLD + "\n'2'" + TextColors.RESET + ": Marks Ratio " +
                  TextColors.CYAN_BOLD + "\n'3'" + TextColors.RESET + ": Both (Test Name & Marks Ratio)  " +
                  TextColors.CYAN_BOLD + "\n'Q'" + TextColors.RESET + ": quit")

    new_test_name = old_test_name
    new_ratio = old_ratio

    # Update Test Name
    if choice in ['1', '3']:
        while True:
            new_test_name = input(f"\nEnter new exam name (Current name: '{old_test_name}'): ").strip().upper()

            if not new_test_name or new_test_name.isspace():
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      "Test name " + TextColors.CYAN_BOLD + "cannot be empty." + TextColors.RESET)
                while True:
                  changes = input("\nDo you still want to make changes? (Y/N): ").strip().upper()

                  if changes not in ("Y", "N"):
                      print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                            "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
                            " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
                      continue

                  if changes == "Y":
                      break
                  elif changes == "N":
                      print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
                      return
                continue

            if new_test_name.replace(" ", "").isdigit():
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      "Test name " + TextColors.CYAN_BOLD + "cannot be numbers only." + TextColors.RESET)
                while True:
                  changes = input("\nDo you still want to make changes? (Y/N): ").strip().upper()

                  if changes not in ("Y", "N"):
                      print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                            "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
                            " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
                      continue

                  if changes == "Y":
                      break
                  elif changes == "N":
                      print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
                      return
                continue

            if not any (char.isalpha() for char in new_test_name):
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      "Test name must contain " + TextColors.CYAN_BOLD + "at least one letter." + TextColors.RESET)
                while True:
                  changes = input("\nDo you still want to make changes? (Y/N): ").strip().upper()

                  if changes not in ("Y", "N"):
                      print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                            "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
                            " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
                      continue

                  if changes == "Y":
                      break
                  elif changes == "N":
                      print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
                      return
                continue

            if new_test_name == old_test_name:
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      TextColors.CYAN_BOLD + "New test name " + TextColors.RESET + "is the " + TextColors.CYAN_BOLD + "same" + TextColors.RESET +
                      " as " + TextColors.CYAN_BOLD + "old test name." + TextColors.RESET)
                while True:
                  changes = input("\nDo you still want to make changes? (Y/N): ").strip().upper()

                  if changes not in ("Y", "N"):
                      print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                            "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
                            " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
                      continue

                  if changes == "Y":
                      break
                  elif changes == "N":
                      print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
                      return
                continue

            allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'1234567890")
            if not all(char in allowed_chars for char in new_test_name):
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      "Test name contains " + TextColors.CYAN_BOLD + "invalid characters." + TextColors.RESET)
                while True:
                  changes = input("\nDo you still want to make changes? (Y/N): ").strip().upper()

                  if changes not in ("Y", "N"):
                      print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                            "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
                            " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
                      continue

                  if changes == "Y":
                      break
                  elif changes == "N":
                      print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
                      return
                continue

            # Check if exam name already exists in this course
            exam_names = [exam['test_name'] for exam in exams[cid]]
            if new_test_name in exam_names:
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      "Test name: " + TextColors.CYAN_BOLD + f"'{new_test_name}'" + TextColors.RESET +
                      " already exists in this course.")
                while True:
                  changes = input("\nDo you still want to make changes? (Y/N): ").strip().upper()

                  if changes not in ("Y", "N"):
                      print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                            "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
                            " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
                      continue

                  if changes == "Y":
                      break
                  elif changes == "N":
                      print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
                      return
                continue

            break

    # Update Marks Ratio
    if choice in ['2', '3']:
        while True:
            new_ratio_input = input(f"\nEnter new marks ratio (Current ratio: {old_ratio}%): ").strip()

            try:
                new_ratio = float(new_ratio_input)
                if 0 < new_ratio <= 100:
                    break
                else:
                    print(TextColors.RED_BOLD + "Invalid ratio! " + TextColors.RESET +
                          "Marks ratio must be between " + TextColors.CYAN_BOLD + "0 and 100" + TextColors.RESET + ".")
                    while True:
                        changes = input("\nDo you still want to make changes? (Y/N): ").strip().upper()
                        if changes not in ("Y", "N"):
                            print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                                  "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
                                  " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
                            continue
                        if changes == "Y":
                            break
                        elif changes == "N":
                            print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
                            return
                    continue
            except ValueError:
                print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                      "Please enter " + TextColors.CYAN_BOLD + "a valid number" + TextColors.RESET + ".")
                while True:
                    changes = input("\nDo you still want to make changes? (Y/N): ").strip().upper()
                    if changes not in ("Y", "N"):
                        print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                              "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
                              " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
                        continue
                    if changes == "Y":
                        break
                    elif changes == "N":
                        print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
                        return
                continue

    # Show changes
    print(f"\nChanges to be made:")
    if old_test_name != new_test_name:
        print(f"Old Test Name: '{old_test_name}'\nNew Test Name: '{new_test_name}'")
    if old_ratio != new_ratio:
        print(f"Old Marks Ratio: {old_ratio}%\nNew Marks Ratio: {new_ratio}%")

    # Check if there are associated grade records
    grade_count = len([g for g in grades if (
        g["course_id"] == cid and
        g.get("test_name", "General") == old_test_name
    )])

    if grade_count > 0:
        print(f"\nThis exam has {grade_count} grade record(s) that will be updated.")

    # Confirm update
    confirm = input("\nConfirm update? (Y/N): ").strip().upper()

    while confirm not in ("Y", "N"):
        print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
              "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
              " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
        confirm = input("Confirm update? (Y/N): ").strip().upper()

    if confirm == "Y":
        # Update the exam record
        selected_exam['test_name'] = new_test_name
        selected_exam['marks_ratio'] = new_ratio

        # Update associated grade records
        grades_updated = False
        for grade_record in grades:
            if (grade_record["course_id"] == cid and
                grade_record.get("test_name", "General") == old_test_name):

                # Update test name
                grade_record["test_name"] = new_test_name

                # Update marks format if ratio changed
                if old_ratio != new_ratio:
                    marks_str = grade_record["marks_display"]
                    if '/' in marks_str:
                        try:
                            actual_str, max_str = marks_str.split('/')
                            actual_marks = float(actual_str)

                            # Calculate new marks based on same percentage
                            old_percentage = (actual_marks / old_ratio) * 100
                            new_actual_marks = (old_percentage * new_ratio) / 100

                            # Update marks with new ratio
                            grade_record["marks_display"] = (f"{new_actual_marks:.1f}/{new_ratio:.0f}")

                            # Recalculate grade based on same percentage
                            grade_record["grade"] = calculate_grade(old_percentage)

                            grades_updated = True
                        except (ValueError, ZeroDivisionError):
                            pass

        # Save all exams back to file
        with open(EXAMS_FILE, "w") as f:
            for course_id, course_exams in exams.items():
                for exam in course_exams:
                    f.write(f"{course_id},{exam['test_name']},{exam['marks_ratio']}\n")

        # Save updated grades if any
        if grades_updated:
            save_grades(grades)

        print("Exam details updated" + TextColors.GREEN_BOLD + " SUCCESSFULLY." + TextColors.RESET)
    else:
        print(TextColors.RED_BOLD + "Update cancelled." + TextColors.RESET + " No changes made.")


def delete_exam_details():
    print("\n=== Delete Exam Details ===")
    courses = load_courses()
    exams = load_exams()
    grades = load_grades()

    if not courses:
        print("Course record" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
              ". Please" + TextColors.CYAN_BOLD + " SELECT 2 " + TextColors.RESET +
              "to add courses first.")
        return

    if not exams:
        print("Exam record" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
              ". Please" + TextColors.CYAN_BOLD + " SELECT 3 " + TextColors.RESET +
              "to add exam details first.")
        return

    # Display existing exams
    print("\nExisting Exams:")
    i = 1
    for cid, course_exams in exams.items():
        if course_exams:
            course_name = courses.get(cid, "Unknown Course")
            print(f"\nCourse Name: {course_name} \nCourse ID: {cid}:")
            for exam in course_exams:
                print(f"  {i:3}. Exam Name: {exam['test_name']}\n       Marks Ratio: {exam['marks_ratio']}%")
                print()
                i += 1

    while True:
        cid = input("\nEnter Course ID to delete exam from (or 'Q' to quit): ").strip()

        if cid.upper() == 'Q':
            print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
            return

        if len(cid) != 4 or not cid.isdigit():
            print(TextColors.RED_BOLD + "Invalid Course ID! " + TextColors.RESET +
                  "Course ID must be " + TextColors.CYAN_BOLD + "4 numerical digits." + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Course ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit" + TextColors.RESET + ".")
            continue

        if cid not in exams or not exams[cid]:
            print("Course ID" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
                  " or " + TextColors.RED_BOLD + "has no exams" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Course ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit" + TextColors.RESET + ".")
            continue
        break

    # Show exams for the selected course
    print(f"\nExams for {courses.get(cid, 'Unknown Course')}:")
    i = 1
    for exam in exams[cid]:
        print(f"{i}. {exam['test_name']} ({exam['marks_ratio']}%)")
        i += 1

    # Get exam number to delete
    while True:
        try:
            exam_num = int(input("\nSelect exam number to delete: "))
            if 1 <= exam_num <= len(exams[cid]):
                break
            else:
                print(f"Please enter a number between {TextColors.CYAN_BOLD}1 and {len(exams[cid])}{TextColors.RESET}.")
        except ValueError:
            print("Please enter " + TextColors.CYAN_BOLD + "a valid number" + TextColors.RESET + ".")

    selected_exam = exams[cid][exam_num - 1]
    test_name_to_delete = selected_exam['test_name']

    # Check if there are associated grade records
    associated_records = [g for g in grades if (
        g["course_id"] == cid and
        g.get("test_name", "General") == test_name_to_delete
    )]

    print(f"\nExam to delete:")
    print(f"- Course ID: {cid}")
    print(f"- Exam Name: {test_name_to_delete}")
    print(f"- Marks Ratio: {selected_exam['marks_ratio']}%")

    if associated_records:
        print(f"  {TextColors.RED_BOLD}Warning: {TextColors.RESET}This exam has {len(associated_records)} associated grade record(s) that will also be deleted!")

    # Ask for confirmation
    confirm = input("\nAre you sure you want to delete this exam? (Y/N): ").strip().upper()

    while confirm not in ("Y", "N"):
        print("Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
              " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
        confirm = input("Are you sure you want to delete this exam? (Y/N): ").strip().upper()

    if confirm == "Y":
        # Remove associated grade records
        if associated_records:
            grades = [g for g in grades if not (
                g["course_id"] == cid and
                g.get("test_name", "General") == test_name_to_delete
            )]
            save_grades(grades)
            print(f"Deleted {len(associated_records)} associated grade record(s).")

        # Remove the selected exam
        del exams[cid][exam_num - 1]

        # If no exams left for this course, remove the course entry entirely
        if not exams[cid]:
            del exams[cid]

        # Save all remaining exams back to file
        with open(EXAMS_FILE, "w") as f:
            for course_id, course_exams in exams.items():
                for exam in course_exams:
                    f.write(f"{course_id},{exam['test_name']},{exam['marks_ratio']}\n")

        print("Exam details deleted" + TextColors.GREEN_BOLD + " SUCCESSFULLY." + TextColors.RESET)
    else:
        print(TextColors.RED_BOLD + "Deletion cancelled." + TextColors.RESET + " No changes made.")