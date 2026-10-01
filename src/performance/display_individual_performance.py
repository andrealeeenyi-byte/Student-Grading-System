def display_individual_performance():
    print("\n=== Individual Student Performance ===")
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

    student_records = [g for g in grades if g["student_id"] == sid]

    print('=' * 100)
    print(f"Student: {students[sid]['name']} ({sid})")
    print(f"Email : {students[sid]['email']}")
    print("=" * 100)

    if not student_records:
        print(TextColors.RED_BOLD + "No grades recorded" + TextColors.RESET + " for this student.")
        return

    print(f"{'Course ID':<10} {'Course Name':<25} {'Test Name':<20} {'Marks':>10} {'Percentage':>15} {'Grade':>10}")
    print("-" * 100)

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

                # Calculate course_percentage BEFORE using it
                if course_percentage >= 70:
                    marks_color = TextColors.GREEN_BOLD
                elif course_percentage >= 40:
                    marks_color = TextColors.YELLOW_BOLD
                else:
                    marks_color = TextColors.RED_BOLD

                course_grade = calculate_grade(course_percentage)
                print("-" * 100)
                print(f"{'':<10} {'':<30} {'TOTAL':<15} "
                      f"{f'{course_total_actual:.0f}/{course_total_max:.0f}':>10} "
                      f"{marks_color}{course_percentage:>15.1f}%{TextColors.RESET} "
                      f"\t{course_grade:>15}")
                print("_" * 100)

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
            print(f"{cid:<10} {cname:<25} {test_name:<20} {marks_str:>10} {'':>15} {'':>10}")
            is_first_course_entry = False
        else:
            print(f"{'':<10} {'':<25} {test_name:<20} {marks_str:>10} {'':>15} {'':>10}")

    # Process the last course
    if current_course is not None and course_total_max > 0:
        course_percentage = (course_total_actual / course_total_max) * 100
        course_percentages.append(course_percentage)

        # Determine color for the last course's total
        if course_percentage >= 70:
            marks_color = TextColors.GREEN_BOLD
        elif course_percentage >= 40:
            marks_color = TextColors.YELLOW_BOLD
        else:
            marks_color = TextColors.RED_BOLD

        course_grade = calculate_grade(course_percentage)
        print("-" * 100)
        print(f"{'':<10} {'':<30} {'TOTAL':<15} "
              f"{f'{course_total_actual:.0f}/{course_total_max:.0f}':>10} "
              f"{marks_color}{course_percentage:>15.1f}%{TextColors.RESET} "
              f"\t{course_grade:>15}")
        print("_" * 100)

    # Calculate and display overall average
    if course_percentages:
        try:
            avg = statistics.mean(course_percentages)
            overall_grade = calculate_grade(avg)

            # Determine color for average
            if avg >= 70:
                avg_color = TextColors.GREEN_BOLD
            elif avg >= 40:
                avg_color = TextColors.YELLOW_BOLD
            else:
                avg_color = TextColors.RED_BOLD

            print(f"\nOverall Average Marks: {avg_color}{avg:.2f}%{TextColors.RESET}")
        except statistics.StatisticsError:
            print(f"\n{TextColors.RED_BOLD}Cannot calculate overall average.{TextColors.RESET}")
    else:
        print(f"\n{TextColors.RED_BOLD}No valid numeric marks to calculate overall average.{TextColors.RESET}")