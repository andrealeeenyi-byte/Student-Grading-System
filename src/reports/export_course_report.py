import os
import statistics


def export_course_report():
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

    if not course_records:
        print(TextColors.RED_BOLD + "No grades recorded " + TextColors.RESET + "for this course.")
        return

    base_filename = f"{cid}_course_report.txt"
    filename = base_filename

    counter = 1
    while os.path.exists(filename):
        counter += 1
        name, ext = os.path.splitext(base_filename)
        filename = f"{name}_{counter}{ext}"

    with open(filename, "w") as f:
        # Header
        f.write("=" * 95 + "\n")
        f.write(f"Course: {courses[cid]} ({cid})\n")
        f.write("=" * 95 + "\n\n")

        # Group records by student
        student_records = {}
        #Loop through each record
        for rec in course_records:
            sid = rec["student_id"]
            if sid not in student_records:
                student_records[sid] = []
            student_records[sid].append(rec)

        # Print table header
        f.write(f"{'Student ID':12} {'Student Name':20} {'Test Name':20} {'Marks':>10} {'Percentage':>15} {'Grade':>10}\n")
        f.write("-" * 95 + "\n")

        student_totals = []

        # Process each student
        # sid_index tracks student position and loops through each student and their records
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
                    f.write(f"{sid:12} {sname:20} {test_name:20} {marks_str:>10} {'':>15} {'':>10}\n")
                    is_first_test = False
                else:
                    # For subsequent tests, leave student ID and name blank with indentation
                    f.write(f"{'':12} {'':20} {test_name:20} {marks_str:>10} {'':>15} {'':>10}\n")

            # Calculate student's total percentage and grade
            if total_max > 0:
                total_percentage = (total_actual / total_max) * 100
                total_grade_with_color = calculate_grade(total_percentage)
                total_grade = total_grade_with_color.split(TextColors.RESET)[0][-1]

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
                f.write("-" * 95 + "\n")
                total_marks_str = f"{int(total_actual)}/{int(total_max)}"
                f.write(f"{'':12} "
                      f"{'':20} "
                      f"{'Total':20} "
                      f"{total_marks_str:>10} "
                      f"{f'{total_percentage:.1f}%':>12} "
                      f"{total_grade:>11}\n")

            # Add separator between students (but not after last student)
            if sid_index < len(student_records) - 1:
                f.write("_" * 95 + "\n")

        f.write("_" * 95 + "\n")

        # Calculate and display course statistics
        if student_totals:
            # Calculate average of students' total percentages
            total_percentages = [student["percentage"] for student in student_totals]
            course_avg = statistics.mean(total_percentages)

            # Find highest and lowest student totals
            highest_student = max(student_totals, key=lambda x: x["percentage"])
            lowest_student = min(student_totals, key=lambda x: x["percentage"])

            f.write("\nCOURSE STATISTICS\n")
            f.write("=" * 20 + "\n")

            f.write(f"AVERAGE MARKS: {course_avg:.1f}%\n")
            f.write(f"HIGHEST MARKS: {highest_student['percentage']:.1f}%\n")
            f.write(f"LOWEST MARKS: {lowest_student['percentage']:.1f}%\n")

        else:
            f.write(f"\nNo valid marks to calculate statistics.\n")

    print(f"\n{TextColors.GREEN_BOLD}Course report exported to: {filename}{TextColors.RESET}")