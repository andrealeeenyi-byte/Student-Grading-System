def update_student_details():
    print("\n===  Details ===")
    students = load_students()

    if not students:
        print("Student record" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
              ". Please" + TextColors.CYAN_BOLD + " SELECT 1 " + TextColors.RESET +
              "to add students first.")
        return

    # Display existing students
    print("\nExisting Students:")
    i = 1
    for sid, student_info in students.items():
        print(f"{i:3}. Student ID: {sid}"
              f"\n     Student Name:  {student_info['name']}"
              f"\n     Student Email: {student_info['email']}")
        print()
        i  += 1

    while True:
        sid = input("Enter Student ID to update or 'Q' to quit: ").strip()

        if sid.upper() == 'Q':
            print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
            return

        if len(sid) != 8 or not sid.isdigit():
            print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                  "Student ID must be" + TextColors.CYAN_BOLD + " 8 numerical digits" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Student ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit." + TextColors.RESET)
            continue

        if sid not in students:
            print("Student ID" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Student ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit" + TextColors.RESET + "." )
            continue

        break

    student = students[sid]
    old_name = student['name']
    old_email = student['email']

    print(f"\nCurrent details for student {sid}:")
    print(f"  1. Name: {old_name}")
    print(f"  2. Email: {old_email}")

    # Ask what to update
    while True:
        choice = input("\nWhat would you like to update? \n1: Name \n2: Email \n3: Both (Name & Email) \n'Q': quit \nSelect (1/2/3/Q): ").strip()

        if choice.upper() == 'Q':
            print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
            return

        if choice in ['1', '2', '3']:
            break
        else:
            print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
                  "Please enter: " +
                  TextColors.CYAN_BOLD + "\n'1'" + TextColors.RESET + ": Name " +
                  TextColors.CYAN_BOLD + "\n'2'" + TextColors.RESET + ": Email " +
                  TextColors.CYAN_BOLD + "\n'3'" + TextColors.RESET + ": Both (Name & Email)  " +
                  TextColors.CYAN_BOLD + "\n'Q'" + TextColors.RESET + ": quit")

    new_name = old_name
    new_email = old_email

    # Update Name
    if choice in ['1', '3']:
        while True:
            new_name = input(f"\nEnter new name (Current name: '{old_name}'): ").strip()

            if not new_name or new_name.isspace():
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      "Name " + TextColors.CYAN_BOLD + "cannot be empty." + TextColors.RESET)
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

            if new_name.replace(" ", "").isdigit():
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      "Name " + TextColors.CYAN_BOLD + "cannot be numbers only." + TextColors.RESET)
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

            if not any(char.isalpha() for char in new_name):
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      "Name must contain " + TextColors.CYAN_BOLD + "at least one letter." + TextColors.RESET)
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

            if new_name == old_name:
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      TextColors.CYAN_BOLD + "New name " + TextColors.RESET +
                      "is the " + TextColors.CYAN_BOLD + "same" + TextColors.RESET +
                      " as "+ TextColors.CYAN_BOLD + "old name." + TextColors.RESET)
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
            if not all(char in allowed_chars for char in new_name):
                print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                      "Name contains " + TextColors.CYAN_BOLD + "invalid characters." + TextColors.RESET)
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

    # Update Email
    if choice in ['2', '3']:
        while True:
            new_email = input(f"\nEnter new email (Current email: '{old_email}'): ").strip().lower()

            if ("@" not in new_email) or (not (new_email.endswith(".com") or new_email.endswith(".edu.my"))):
                print(TextColors.RED_BOLD + "Invalid email! " + TextColors.RESET +
                      "Email must contain" + TextColors.CYAN_BOLD + " @ " + TextColors.RESET +
                      "and end with" + TextColors.CYAN_BOLD + " '.com' " + TextColors.RESET +
                      "or" + TextColors.CYAN_BOLD + " '.edu.my'. " + TextColors.RESET)
                while True:
                    changes = input ("\nDo you still want to make changes? (Y/N): ").strip().upper()
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

            if new_email == old_email:
                print(TextColors.RED_BOLD + "Invalid email! " + TextColors.RESET +
                      TextColors.CYAN_BOLD + "New email " + TextColors.RESET +
                      "is the " + TextColors.CYAN_BOLD + "same" + TextColors.RESET +
                      " as "+ TextColors.CYAN_BOLD + "old email." + TextColors.RESET)
                while True:
                    changes = input ("\nDo you still want to make changes? (Y/N): ").strip().upper()
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

            if "@" in new_email:
                username = new_email.split("@")[0]

                if not username:
                    print(TextColors.RED_BOLD + "Invalid email! " + TextColors.RESET +
                          "Email username " + TextColors.CYAN_BOLD + "cannot be empty." + TextColors.RESET)

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

                if not any(char.isalnum() for char in username):
                    print(TextColors.RED_BOLD + "Invalid email! " + TextColors.RESET +
                          "Email username must contain " + TextColors.CYAN_BOLD + "at least one letter " + TextColors.RESET +
                          "or " + TextColors.CYAN_BOLD + "number" + TextColors.RESET + ".")

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

            # Check if new email already exists (excluding current student's old email)
            email_exists = False
            for student_id, student_info in students.items():
                if student_id != sid and student_info['email'] == new_email:
                    email_exists = True
                    break

            if email_exists:
                print("Email " + TextColors.RED_BOLD + "ALREADY EXISTS!" + TextColors.RESET +
                      " Please " + TextColors.CYAN_BOLD + "enter a different email " + TextColors.RESET + "." )
                while True:
                    changes = input ("\nDo you still want to make changes? (Y/N): ").strip().upper()
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
    if old_name != new_name:
        print(f"Old Name: '{old_name}'\nNew Name:'{new_name}'")
    if old_email != new_email:
        print(f"Old Email: '{old_email}' \nNew Email '{new_email}'")

    # Confirm update
    confirm = input("\nConfirm update? (Y/N): ").strip().upper()

    while confirm not in ("Y", "N"):
        print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
              "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
              " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
        confirm = input("Confirm update? (Y/N): ").strip().upper()

    if confirm == "Y":
        # Update student details
        students[sid]['name'] = new_name
        students[sid]['email'] = new_email

        # Save updated students to file
        with open(STUDENTS_FILE, "w") as f:
            for student_id, student_info in students.items():
                f.write(f"{student_id},{student_info['name']},{student_info['email']}\n")

        print("Student details updated" + TextColors.GREEN_BOLD + " SUCCESSFULLY." + TextColors.RESET)
    else:
        print(TextColors.RED_BOLD + "Update cancelled." + TextColors.RESET + " No changes made.")

def delete_student():
    print("\n=== Delete Student ===")
    students = load_students()
    grades = load_grades()

    if not students:
        print("Student record" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
              ". Please" + TextColors.CYAN_BOLD + " SELECT 1 " + TextColors.RESET +
              "to add students first.")
        return

    # Display existing students
    print("\nExisting Students:")
    i = 1
    for sid, student_info in students.items():
        print(f"{i:3}. Student ID: {sid}\n     Student Name:  {student_info['name']}\n     Student Email: {student_info['email']}")
        print()
        i  += 1

    while True:
        sid = input("\nEnter Student ID to delete (or 'Q' to quit): ").strip()

        if sid.upper() == 'Q':
            print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
            return

        if len(sid) != 8 or not sid.isdigit():
            print(TextColors.RED_BOLD + "Invalid Student ID! " + TextColors.RESET +
                  "Student ID must be " + TextColors.CYAN_BOLD + "8 numerical digits." + TextColors.RESET +
                  " 3Please enter a " + TextColors.CYAN_BOLD + "valid Student ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit" + TextColors.RESET + "." )
            continue

        if sid not in students:
            print("Student ID" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Student ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit" + TextColors.RESET + "." )
            continue
        break

    # Get student details for confirmation
    student_name = students[sid]['name']
    student_email = students[sid]['email']

    # Check if student has any grade records
    student_grades = [g for g in grades if g["student_id"] == sid]
    grade_count = len(student_grades)

    print(f"\nStudent to delete:")
    print(f"- ID: {sid}")
    print(f"- Name: {student_name}")
    print(f"- Email: {student_email}")

    if grade_count > 0:
        print(f"  {TextColors.RED_BOLD}Warning:{TextColors.RESET} This student has {grade_count} grade record(s) that will also be deleted!")

    # Ask for confirmation
    confirm = input(f"\nAre you sure you want to delete student {sid}? (Y/N): ").strip().upper()

    while confirm not in ("Y", "N"):
        print(TextColors.RED_BOLD + "Invalid input! " + TextColors.RESET +
              "Please enter " + TextColors.GREEN_BOLD + "'Y'" + TextColors.RESET +
              " or " + TextColors.RED_BOLD + "'N'" + TextColors.RESET + ".")
        confirm = input(f"Are you sure you want to delete student {sid}? (Y/N): ").strip().upper()

    if confirm == "Y":
        # Remove student from students dictionary
        del students[sid]

        # Remove student's grade records
        if grade_count > 0:
            grades = [g for g in grades if g["student_id"] != sid]
            save_grades(grades)
            print(f"Deleted {grade_count} grade record(s) for this student.")

        # Save updated students to file
        with open(STUDENTS_FILE, "w") as f:
            for student_id, student_info in students.items():
                f.write(f"{student_id},{student_info['name']},{student_info['email']}\n")

        print("Student record deleted" + TextColors.GREEN_BOLD + " SUCCESSFULLY." + TextColors.RESET)
    else:
        print(TextColors.RED_BOLD + "Deletion cancelled." + TextColors.RESET + " No changes made.")