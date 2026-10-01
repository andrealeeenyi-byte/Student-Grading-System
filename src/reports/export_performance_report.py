def export_performance_report():
    print("\n=== Export Performance Report ===")
    print("1. Export individual student performance")
    print("2. Export course performance summary")

    while True:
      choice = input("Select an option (1 or 2 or 'Q' to quit): ").strip()

      if choice.upper() == 'Q':
          print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
          return
      if choice == "1":
          export_student_report()
          return
      if choice == "2":
          export_course_report()
          return
      else:
          print(TextColors.RED_BOLD + "Invalid choice! " + TextColors.RESET +
                "Please enter " + TextColors.CYAN_BOLD + "'1'" + TextColors. RESET +
                " or " + TextColors.CYAN_BOLD + "'2'" + TextColors.RESET +
                " or " + TextColors.CYAN_BOLD + "'Q' to quit" + TextColors.RESET + ".")
