import statistics


def display_course_summary():
    print("\n=== Course Performance Summary ===")
    students = load_students()
    courses = load_courses()
    grades = load_grades()

    if not courses:
        print("Course record" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
              ". Please" + TextColors.CYAN_BOLD + " SELECT 2 " + TextColors.RESET +
              "to add courses first.")
        return

    print("\nAvailable Courses:")
    i = 1
    for cid_key, cname in courses.items():
      print(f"{i:3}. Course ID: {cid_key}\n     Course Name: {cname}")
      print()
      i  += 1

    while True:
        cid = input("Enter Course ID (or 'Q' to quit): ").strip().upper()

        if cid == 'Q':
            print(TextColors.RED_BOLD + "Operation cancelled." + TextColors.RESET)
            return

        if cid not in courses:
            print("Course ID" + TextColors.RED_BOLD + " NOT FOUND" + TextColors.RESET +
                  ". Please enter a " + TextColors.CYAN_BOLD + "valid Course ID" + TextColors.RESET +
                  " or " + TextColors.CYAN_BOLD + "'Q' to quit" + TextColors.RESET + "." )
            continue
        break

    course_records = [g for g in grades if g["course_id"] == cid]

    print("=" * 95)
    print(f"Course: {courses[cid]} ({cid})")
    print("=" * 95)

    if not course_records:
        print(TextColors.RED_BOLD + "No grades recorded " + TextColors.RESET + "for this course.")
        return

    # Function to get color based on percentage
    def get_marks_color(percentage):
        if percentage >= 70:
            return TextColors.GREEN_BOLD
        elif percentage >= 40:
            return TextColors.YELLOW_BOLD
        else:
            return TextColors.RED_BOLD

    # Group records by student
    student_records = {}
    for rec in course_records:
        sid = rec["student_id"]
        if sid not in student_records:
            student_records[sid] = []
        student_records[sid].append(rec)

    # Print table header
    print(f"{'Student ID':12} {'Student Name':20} {'Test Name':20} {'Marks':>10} {'Percentage':>15} {'Grade':>10}")
    print("-" * 95)

    student_totals = []  # Store each student's total performance

    # Process each student
    for sid_index, (sid, records) in enumerate(student_records.items()):
        sname = students.get(sid, {}).get("name", "Unknown Student")

        # Initialize totals for this student
        total_actual = 0
        total_max = 0
        is_first_test = True

        # Display each test for this student
        for rec_index, rec in enumerate(records):
            test_name = rec.get("test_name", "General")
            marks_str = rec["marks_display"]
            grade = rec["grade"]

            # Calculate totals
            if '/' in marks_str:
                try:
                    actual_str, max_str = marks_str.split('/')
                    actual_marks = float(actual_str)
                    max_marks = float(max_str)
                    total_actual += actual_marks
                    total_max += max_marks
                except (ValueError, ZeroDivisionError):
                    pass

            # Print student info only for first test
            if is_first_test:
                print(f"{sid:12} {sname:20} {test_name:20} {marks_str:>10} {'':>15} {'':>10}")
                is_first_test = False
            else:
                # For subsequent tests, leave student ID and name blank with indentation
                print(f"{'':12} {'':20} {test_name:20} {marks_str:>10} {'':>15} {'':>10}")

        # Calculate student's total percentage and grade
        if total_max > 0:
            total_percentage = (total_actual / total_max) * 100
            total_color = get_marks_color(total_percentage)
            total_grade = calculate_grade(total_percentage)

            # Store for course statistics
            student_totals.append({
                "sid": sid,
                "name": sname,
                "total_actual": total_actual,
                "total_max": total_max,
                "percentage": total_percentage,
                "grade": total_grade
            })

            # Print student's total line
            print("-" * 95)
            total_marks_str = f"{int(total_actual)}/{int(total_max)}"
            print(f"{'':12} "
                  f"{'':20} "
                  f"{'Total':20} "
                  f"{total_marks_str:>10} "
                  f"{total_color}{f'{total_percentage:.1f}%':>15}{TextColors.RESET} "
                  f"{total_grade:>20}")

        # Add separator between students (but not after last student)
        if sid_index < len(student_records) - 1:
            print("_" * 95)

    print("_" * 95)

    # Calculate and display course statistics
    if student_totals:
        # Calculate average of students' total percentages
        total_percentages = [student["percentage"] for student in student_totals]
        course_avg = statistics.mean(total_percentages)
        avg_color = get_marks_color(course_avg)

        # Find highest and lowest student totals
        highest_student = max(student_totals, key=lambda x: x["percentage"])
        lowest_student = min(student_totals, key=lambda x: x["percentage"])

        highest_color = get_marks_color(highest_student["percentage"])
        lowest_color = get_marks_color(lowest_student["percentage"])

        print("\nCOURSE STATISTICS")
        print("=" * 20)

        print(f"AVERAGE MARKS: {avg_color}{course_avg:.1f}%{TextColors.RESET}")
        print(f"HIGHEST MARKS: {highest_color}{highest_student['percentage']:.1f}%{TextColors.RESET}")
        print(f"LOWEST MARKS: {lowest_color}{lowest_student['percentage']:.1f}%{TextColors.RESET}")

    else:
        print(f"\n{TextColors.RED_BOLD}No valid marks to calculate statistics.{TextColors.RESET}")