def update_course():
    print("\n=== Update Course Details ===")
    courses = load_courses()
    exams = load_exams()
    grades = load_grades()

    if not courses:
        print("Course record" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
              ". Please" + TextColors.CYAN_BOLD + " SELECT 2 " + TextColors.RESET +
              "to add courses first.")
        return

    # Display existing courses
    print("\nExisting Courses:")
    i = 1
    for cid, cname in courses.items():
        print(f"{i:3}. Course ID: {cid}\n     Course Name: {cname}")
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

        if cid not in courses:
            print("Course ID" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Course ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit" + TextColors.RESET + ".")
            continue

        break

    old_cname = courses[cid]

    print(f"\nCurrent details for course {cid}:")
    print(f"1. Course ID: {cid}")
    print(f"2. Course Name: {old_cname}")

    # Ask what to update
    while True:
        choice = input("\nWhat would you like to update? \n1: Course ID \n2: Course Name \n3: Both (Course ID & Name) \n'Q': quit \nSelect (1/2/3/Q): ").strip()

        if choice.upper() == 'Q':
            print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
            return

        if choice in ['1', '2', '3']:
            break
        else:
            print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                  "Please enter: " +
                  TextColors.CYAN_BOLD + "\n'1'" + TextColors.RESET + ": Course ID " +
                  TextColors.CYAN_BOLD + "\n'2'" + TextColors.RESET + ": Course Name " +
                  TextColors.CYAN_BOLD + "\n'3'" + TextColors.RESET + ": Both (Course ID & Name)  " +
                  TextColors.CYAN_BOLD + "\n'Q'" + TextColors.RESET + ": quit")

    new_cid = cid
    new_cname = old_cname

    # Update Course ID
    if choice in ['1', '3']:
        while True:
            new_cid = input(f"\nEnter new Course ID (Current ID: '{cid}'): ").strip()

            if not new_cid or new_cid.isspace():
                print(TextColors.RED_BOLD + "Invalid ID! " + TextColors.RESET +
                      "Course ID " + TextColors.CYAN_BOLD + "cannot be empty." + TextColors.RESET)
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

            if len(new_cid) != 4 or not new_cid.isdigit():
                print(TextColors.RED_BOLD + "Invalid ID! " + TextColors.RESET +
                      "Course ID must be" + TextColors.CYAN_BOLD + " 4 numerical digits" + TextColors.RESET + ".")
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

            if new_cid == cid:
                print(TextColors.RED_BOLD + "Invalid ID! " + TextColors.RESET +
                      TextColors.CYAN_BOLD + "New Course ID " + TextColors.RESET +
                      "is the " + TextColors.CYAN_BOLD + "same" + TextColors.RESET +
                      " as " + TextColors.CYAN_BOLD + "old Course ID." + TextColors.RESET)
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

            if new_cid in courses:
                print("Course ID " + TextColors.RED_BOLD + "ALREADY EXISTS! " + TextColors.RESET +
                      "Please " + TextColors.CYAN_BOLD + "enter a different Course ID " + TextColors.RESET + ".")
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

    # Update Course Name
    if choice in ['2', '3']:
        while True:
            new_cname = input(f"\nEnter new course name (Current name: '{old_cname}'): ").strip()

            if not new_cname or new_cname.isspace():
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      "Course name " + TextColors.CYAN_BOLD + "cannot be empty." + TextColors.RESET)
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

            if new_cname.replace(" ", "").isdigit():
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      "Course name " + TextColors.CYAN_BOLD + "cannot be numbers only." + TextColors.RESET)
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

            if not any(char.isalpha() for char in new_cname):
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      "Course name must contain " + TextColors.CYAN_BOLD + "at least one letter." + TextColors.RESET)
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

            if new_cname == old_cname:
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      TextColors.CYAN_BOLD + "New course name " + TextColors.RESET +
                      "is the " + TextColors.CYAN_BOLD + "same" + TextColors.RESET +
                      " as " + TextColors.CYAN_BOLD + "old course name." + TextColors.RESET)
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
            if not all(char in allowed_chars for char in new_cname):
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      "Course name contains " + TextColors.CYAN_BOLD + "invalid characters." + TextColors.RESET)
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

    # Show changes
    print(f"\nChanges to be made:")
    if cid != new_cid:
        print(f"Old Course ID: '{cid}'\nNew Course ID: '{new_cid}'")
    if old_cname != new_cname:
        print(f"Old Course Name: '{old_cname}'\nNew Course Name: '{new_cname}'")

    # Check if there are associated records
    exam_count = 0
    if cid in exams:
        exam_count = len(exams[cid])

    grade_count = len([g for g in grades if g["course_id"] == cid])

    if exam_count > 0 or grade_count > 0:
        print(f"\nThis course has:")
        if exam_count > 0:
            print(f"- {exam_count} exam record(s)")
        if grade_count > 0:
            print(f"- {grade_count} grade record(s)")

        if cid != new_cid:
            print("These records will be updated with the new Course ID.")

    # Confirm update
    confirm = input("\nConfirm update? (Y/N): ").strip().upper()

    while confirm not in ("Y", "N"):
        print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
              "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
              " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
        confirm = input("Confirm update? (Y/N): ").strip().upper()

    if confirm == "Y":
        # Update course details
        if cid != new_cid:
            # Remove old course and add new one
            del courses[cid]
            courses[new_cid] = new_cname

            # Update exams with new course ID
            if cid in exams:
                exams[new_cid] = exams[cid]
                del exams[cid]

            # Update grades with new course ID
            for grade_record in grades:
                if grade_record["course_id"] == cid:
                    grade_record["course_id"] = new_cid
        else:
            # Just update the course name
            courses[cid] = new_cname

        # Save updated courses to file
        with open(COURSES_FILE, "w") as f:
            for course_id, course_name in courses.items():
                f.write(f"{course_id},{course_name}\n")

        # Save updated exams if course ID changed
        if cid != new_cid and exams:
            with open(EXAMS_FILE, "w") as f:
                for course_id, course_exams in exams.items():
                    for exam in course_exams:
                        f.write(f"{course_id},{exam['test_name']},{exam['marks_ratio']}\n")

        # Save updated grades if course ID changed
        if cid != new_cid and grade_count > 0:
            save_grades(grades)

        print("Course details updated" + TextColors.GREEN_BOLD + " SUCCESSFULLY." + TextColors.RESET)
    else:
        print(TextColors.RED_BOLD + "Update cancelled." + TextColors.RESET + " No changes made.")

def delete_course():
    print("\n=== Delete Course ===")
    courses = load_courses()
    exams = load_exams()
    grades = load_grades()

    if not courses:
      print(TextColors.RED_BOLD + "No courses found. " + TextColors.RESET +
            "Please " + TextColors.CYAN_BOLD + "SELECT 2 " + TextColors.RESET + "to add courses first")
      return

    # Display existing courses
    print("\nExisting Courses:")
    i = 1
    for cid, cname in courses.items():
        print(f"{i:3}. Course ID: {cid}\n     Course Name: {cname}")
        print()
        i  += 1

    while True:
        cid = input("Enter Course ID to delete (or 'Q' to quit): ").strip()

        if cid.upper() == 'Q':
            print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
            return

        if len(cid) != 4 or not cid.isdigit():
            print("Course ID must be " + TextColors.CYAN_BOLD + "4 numerical digits" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Course ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit." + TextColors.RESET)
            continue

        if cid not in courses:
            print("Course ID" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Course ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit." + TextColors.RESET)
            continue

        break

    # Get course name for confirmation
    course_name = courses[cid]

    # Check if course has any exam records
    exam_count = 0
    if cid in exams:
        exam_count = len(exams[cid])

    # Check if course has any grade records
    course_grades = [g for g in grades if g["course_id"] == cid]
    grade_count = len(course_grades)

    print(f"\nCourse to delete:")
    print(f"- ID: {cid}")
    print(f"- Name: {course_name}")

    if exam_count > 0:
        print(f"  {TextColors.RED_BOLD}Warning: {TextColors.RESET}This course has {exam_count} exam record(s) that will also be deleted!")

    if grade_count > 0:
        print(f"  {TextColors.RED_BOLD}Warning: {TextColors.RESET}This course has {grade_count} grade record(s) that will also be deleted!")

    # Ask for confirmation
    confirm = input(f"\nAre you sure you want to delete course {cid}? (Y/N): ").strip().upper()

    while confirm not in ("Y", "N"):
        print("Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
              " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
        confirm = input(f"Are you sure you want to delete course {cid}? (Y/N): ").strip().upper()

    if confirm == "Y":
        # Remove course from courses dictionary
        del courses[cid]

        # Remove course's exam records
        if cid in exams:
            del exams[cid]
            # Save updated exams to file
            with open(EXAMS_FILE, "w") as f:
                for course_id, course_exams in exams.items():
                    for exam in course_exams:
                        f.write(f"{course_id},{exam['test_name']},{exam['marks_ratio']}\n")

        # Remove course's grade records
        if grade_count > 0:
            grades = [g for g in grades if g["course_id"] != cid]
            save_grades(grades)
            print(f"Deleted {grade_count} grade record(s) for this course.")

        # Save updated courses to file
        with open(COURSES_FILE, "w") as f:
            for course_id, course_name in courses.items():
                f.write(f"{course_id},{course_name}\n")

        print("Course deleted" + TextColors.GREEN_BOLD + " SUCCESSFULLY." + TextColors.RESET)
    else:
        print(TextColors.RED_BOLD + "Deletion cancelled." + TextColors.RESET + " No changes made.")