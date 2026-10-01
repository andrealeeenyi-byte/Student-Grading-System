def add_student():
    print("\n=== Add New Student ===")
    students = load_students()

    while True:
        sid = input("Enter Student ID: ").strip()

        if len(sid) !=8 or not sid.isdigit():
            print(TextColors.RED_BOLD + "Invalid Student ID! " + TextColors.RESET +
                  "Student ID must be " + TextColors.CYAN_BOLD + "8 numerical digits." + TextColors.RESET +
                  TextColors.RED_BOLD + "\nPlease try again\n" + TextColors.RESET)
            continue

        if sid in students:
            print("Student ID" + TextColors.RED_BOLD + " ALREADY EXIST" + TextColors.RESET +
                  "." + TextColors.RED_BOLD + "\nOPERATION CANCELLED" + TextColors.RESET)
            return
        break

    while True:
        name = input("Enter Student Name: ").strip()

        # Check if name is empty or contains only whitespace
        if not name or name.isspace():
            print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                  "Name " + TextColors.CYAN_BOLD + "cannot be empty." + TextColors.RESET +
                  TextColors.RED_BOLD + "\nPlease try again." + TextColors.RESET)
            continue

        # Check if name contains only numbers
        if name.replace(" ", "").isdigit():
            print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                  "Name "+ TextColors.CYAN_BOLD + "cannot be only numbers." + TextColors.RESET +
                  TextColors.RED_BOLD + "\nPlease try again." + TextColors.RESET)
            continue

        # Check if name contains any letters (at least one non-digit character)
        if not any(char.isalpha() for char in name):
            print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                  "Name must contain " + TextColors.CYAN_BOLD + "at least one letter." + TextColors.RESET +
                  TextColors.RED_BOLD + "\nPlease try again." + TextColors.RESET)
            continue

        # This allows spaces, hyphens, and apostrophes
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'1234567890")
        if not all(char in allowed_chars for char in name):
            print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                  "Name contains " + TextColors.CYAN_BOLD + "invalid characters." + TextColors.RESET +
                  TextColors.RED_BOLD + "\nPlease try again." + TextColors.RESET)
            continue
        break

    while True:
        email = input("Enter Student Email: ").strip().lower()

        if ("@" not in email) or (not (email.endswith(".com") or email.endswith(".edu.my"))):
          print(TextColors.RED_BOLD + "Invalid email! " + TextColors.RESET +
                "Email must contain" + TextColors.CYAN_BOLD + " @ " + TextColors.RESET + "and end with" +
                TextColors.CYAN_BOLD + " '.com' " + TextColors.RESET + "or" + TextColors.CYAN_BOLD +
                " '.edu.my'. " + TextColors.RESET)
          continue

        if "@" in email:
            username = email.split("@")[0]

            if not username:
                print(TextColors.RED_BOLD + "Invalid email! " + TextColors.RESET +
                      "Email username " + TextColors.CYAN_BOLD + "cannot be empty." + TextColors.RESET)
                continue

            if not any(char.isalnum() for char in username):
                print(TextColors.RED_BOLD + "Invalid email! " + TextColors.RESET +
                       "Email username must contain " + TextColors.CYAN_BOLD + "at least one letter " +
                      TextColors.RESET + "or " + TextColors.CYAN_BOLD + "number" + TextColors.RESET + ".")
                continue

        email_exists = any(student["email"] == email for student in students.values())

        if email_exists == True:
            print("Email " + TextColors.RED_BOLD + "ALREADY EXISTS!" + TextColors.RESET +
              TextColors.RED_BOLD + "\nOPERATION CANCELLED." + TextColors.RESET)
            return
        break

    with open(STUDENTS_FILE, "a") as f:
        f.write(f"{sid},{name},{email}\n")

    print("Student added" + TextColors.GREEN_BOLD + " SUCCESSFULLY." + TextColors.RESET)