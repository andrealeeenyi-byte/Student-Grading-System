def add_course():
    print("\n=== Add New Course ===")
    courses = load_courses()

    while True:
        cid = input("Enter Course ID: ").strip()

        if len(cid) !=4 or not cid.isdigit():
            print("Course ID must be " + TextColors.CYAN_BOLD + "4 numerical digits." + TextColors.RESET +
                  TextColors.RED_BOLD + "\nPlease try again\n" + TextColors.RESET)
            continue

        if cid in courses:
            print("Course ID" + TextColors.RED_BOLD + " ALREADY EXIST." + TextColors.RESET +
                  TextColors.RED_BOLD + "\nPlease try again\n" + TextColors.RESET)
            return
        break

    while True:
        cname = input("Enter Course Name: ").strip()

        # Check if name is empty or contains only whitespace
        if not cname or cname.isspace():
            print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                  "Course name " + TextColors.CYAN_BOLD + "cannot be empty." + TextColors.RESET +
                  TextColors.RED_BOLD + "\nPlease try again." + TextColors.RESET)
            continue

        # Check if name contains only numbers
        if cname.replace(" ", "").isdigit():
            print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                  "Course name "+ TextColors.CYAN_BOLD + "cannot be only numbers." + TextColors.RESET +
                  TextColors.RED_BOLD + "\nPlease try again." + TextColors.RESET)
            continue

        # Check if name contains any letters (at least one non-digit character)
        if not any(char.isalpha() for char in cname):
            print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                  "Course name must contain " + TextColors.CYAN_BOLD + "at least one letter." + TextColors.RESET +
                  TextColors.RED_BOLD + "\nPlease try again." + TextColors.RESET)
            continue

        # This allows spaces, hyphens, and apostrophes
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'1234567890")
        if not all(char in allowed_chars for char in cname):
            print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
                  "Course name contains " + TextColors.CYAN_BOLD + "invalid characters." + TextColors.RESET +
                  TextColors.RED_BOLD + "\nPlease try again." + TextColors.RESET)
            continue
        break

    with open(COURSES_FILE, "a") as f:
        f.write(f"{cid},{cname}\n")

    print("Course added" + TextColors.GREEN_BOLD + " SUCCESSFULLY." + TextColors.RESET)