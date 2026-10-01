def add_exam_details():
  print("\n==== Add Exam Details ====")

  courses = load_courses()
  if not courses:
    print(TextColors.RED_BOLD + "No courses found. " + TextColors.RESET +
          "Please " + TextColors.CYAN_BOLD + "SELECT 2 " + TextColors.RESET + "to add courses first")
    return

  exams = load_exams()

  print("\nAvailable Courses:")
  i = 1
  for cid_key, cname in courses.items():
    print(f"{i:3}. Course ID: {cid_key}\n     Course Name: {cname}")
    print()
    i  += 1

  while True:
    cid = input("Enter Course ID (or 'Q' to quit): ").strip()

    if cid.upper() == "Q":
      print(TextColors.RED_BOLD + "Operation cancelled. " + TextColors.RESET)
      return

    if cid in courses:
      break

    if cid not in courses:
      print("Course ID" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Course ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit" + TextColors.RESET + ".")
      continue

  if cid in exams:
    print("\nExisting tests for this course:")
    for exam in exams[cid]:
        print(f"- {exam['test_name']}({exam['marks_ratio']}%) ")
        continue


  while True:
    test_name = input("Enter test name: ").strip().upper()

    # Check if test name is empty or contains only whitespace
    if not test_name or test_name.isspace():
        print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
              "Test name " + TextColors.CYAN_BOLD + "cannot be empty." + TextColors.RESET +
              TextColors.RED_BOLD + "\nPlease try again." + TextColors.RESET)

    # Check if name contains only numbers
    if test_name.replace(" ", "").isdigit():
        print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
              "Test name "+ TextColors.CYAN_BOLD + "cannot be only numbers." + TextColors.RESET +
              TextColors.RED_BOLD + "\nPlease try again." + TextColors.RESET)
        continue

    # Check if name contains any letters (at least one non-digit character)
    if not any(char.isalpha() for char in test_name):
        print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
              "Test name must contain " + TextColors.CYAN_BOLD + "at least one letter." + TextColors.RESET +
              TextColors.RED_BOLD + "\nPlease try again." + TextColors.RESET)
        continue

    # This allows spaces, hypens, and apostrophes
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'1234567890")
    if not all(char in allowed_chars for char in test_name):
        print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
              "Test name contains " + TextColors.CYAN_BOLD + "invalid characters." + TextColors.RESET +
              TextColors.RED_BOLD + "\nPlease try again." + TextColors.RESET)
        continue

    # Check if exam name already exists in this course
    exam_names = [exam['test_name'] for exam in exams.get(cid,[])]
    if test_name in exam_names:
        print(TextColors.RED_BOLD + "Invalid name! " + TextColors.RESET +
              "Test name: " + TextColors.CYAN_BOLD + f"'{test_name}'" + TextColors.RESET +
              " already exists in this course.")
        continue

    break

  while True:
    try:
      marks_ratio = float(input(f"Enter marks ratio for {test_name} (0 - 100): "))
      if 0 < marks_ratio <= 100:
        break
      else:
        print("Marks ratio must be between " + TextColors.CYAN_BOLD + "0 and 100." + TextColors.RESET)
    except ValueError:
      print(TextColors.RED_BOLD + "Invalid marks ratio" + TextColors.RESET +
            ". Please " + TextColors.CYAN_BOLD + "enter a number." + TextColors.RESET)

  if cid not in exams:
    exams[cid] = []
  exams[cid].append({
      "test_name": test_name,
      "marks_ratio": float(marks_ratio)
  })
  save_exams(exams)

  print("Exam details added" + TextColors.GREEN_BOLD + " SUCCESSFULLY." + TextColors.RESET)