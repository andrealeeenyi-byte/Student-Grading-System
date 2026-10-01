def export_student_report():
    students = load_students()
    courses = load_courses()
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
        i += 1

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

    student_records = [g for g in grades if g["student_id"] == sid]

    if not student_records:
        print(TextColors.RED_BOLD + "No grades recorded " + TextColors.RESET + "for this student.")
        return

    base_filename = f"{sid}_student_report.txt"
    filename = base_filename

    counter = 1
    while os.path.exists(filename):
        counter += 1
        name, ext = os.path.splitext(base_filename)
        filename = f"{name}_{counter}{ext}"

    with open(filename, "w") as f:
        # Header
        f.write("=" * 95 + "\n")
        f.write(f"Student: {students[sid]['name']} ({sid})\n")
        f.write(f"Email : {students[sid]['email']}\n")
        f.write("=" * 95 + "\n")

        # Write table header
        f.write(f"{'Course ID':<10} {'Course Name':<25} {'Test Name':<15} {'Marks':>10} {'Percentage':>15} {'Grade':>10}\n")
        f.write("-" * 95 + "\n")

        course_percentages = []
        current_course = None
        course_total_actual = 0
        course_total_max = 0
        is_first_course_entry = True

        for rec in student_records:
            cid = rec["course_id"]
            cname = courses.get(cid, "Unknown Course")
            test_name = rec.get("test_name", "-")
            marks_str = rec["marks_display"]

            # Check if we've moved to a new course
            if current_course != cid:
                # If there was a previous course, process it
                if current_course is not None:
                    course_percentage = (course_total_actual / course_total_max) * 100
                    course_percentages.append(course_percentage)

                    # Get grade without color
                    grade_with_color = calculate_grade(course_percentage)
                    course_grade = grade_with_color.split(TextColors.RESET)[0][-1]

                    f.write("-" * 95 + "\n")
                    f.write(f"{'':<10} {'':<25} {'TOTAL':<15} "
                          f"{f'{course_total_actual:.0f}/{course_total_max:.0f}':>10} "
                          f"{course_percentage:>7.1f}% "
                          f"\t{course_grade:>7}\n")
                    f.write("_" * 95 + "\n")

                # Reset for new course
                current_course = cid
                course_total_actual = 0
                course_total_max = 0
                is_first_course_entry = True

            # Add to course totals
            if '/' in marks_str:
                try:
                    actual, max_val = map(float, marks_str.split('/'))
                    course_total_actual += actual
                    course_total_max += max_val
                except ValueError:
                    pass

            # Display test entry
            if is_first_course_entry:
                f.write(f"{cid:<10} {cname:<25} {test_name:<15} {marks_str:>10} {'':>15} {'':>10}\n")
                is_first_course_entry = False
            else:
                f.write(f"{'':<10} {'':<25} {test_name:<15} {marks_str:>10} {'':>15} {'':>10}\n")

        # Process the last course
        if current_course is not None and course_total_max > 0:
            course_percentage = (course_total_actual / course_total_max) * 100
            course_percentages.append(course_percentage)

            # Get grade without color
            grade_with_color = calculate_grade(course_percentage)
            #\033[1;91mC\033[0m
            course_grade = grade_with_color.split(TextColors.RESET)[0][-1]

            f.write("-" * 95 + "\n")
            f.write(f"{'':<10} {'':<25} {'TOTAL':<15} "
                  f"{f'{course_total_actual:.0f}/{course_total_max:.0f}':>10} "
                  f"{course_percentage:>7.1f}% "
                  f"\t{course_grade:>7}\n")
            f.write("_" * 95 + "\n")

        # Calculate and display overall average
        if course_percentages:
            try:
                avg = statistics.mean(course_percentages)

                if avg >= 70:
                    avg_color = TextColors.GREEN_BOLD
                elif avg >= 40:
                    avg_color = TextColors.YELLOW_BOLD
                else:
                    avg_color = TextColors.RED_BOLD

                f.write(f"\nOverall Average Marks: {avg:.2f}%\n")

            except statistics.StatisticsError:
                f.write(f"\nCannot calculate overall average.\n")
        else:
            f.write(f"\nNo valid numeric marks to calculate overall average.\n")

    print(f"\n{TextColors.GREEN_BOLD}Student report exported to: {filename}{TextColors.RESET}")
