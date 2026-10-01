from pathlib import Path


SOURCE_ROOT = Path(__file__).parent
SOURCE_FILES = [
    SOURCE_ROOT / "file_management" / "file_management.py",
    SOURCE_ROOT / "initialization" / "font_initialization.py",
    SOURCE_ROOT / "initialization" / "file_initialization.py",
    SOURCE_ROOT / "helper_load_functions" / "load_students",
    SOURCE_ROOT / "helper_load_functions" / "load_courses",
    SOURCE_ROOT / "helper_load_functions" / "load_grades",
    SOURCE_ROOT / "helper_load_functions" / "load_exams",
    SOURCE_ROOT / "helper_load_functions" / "save_grades",
    SOURCE_ROOT / "helper_load_functions" / "save_exams",
    SOURCE_ROOT / "grading" / "grade_calculation.py",
    SOURCE_ROOT / "student" / "add_student.py",
    SOURCE_ROOT / "student" / "update_delete_student.py",
    SOURCE_ROOT / "course" / "add_course.py",
    SOURCE_ROOT / "course" / "update_delete_course.py",
    SOURCE_ROOT / "exam" / "add_exam_details.py",
    SOURCE_ROOT / "exam" / "update_delete_exam_details.py",
    SOURCE_ROOT / "marks" / "record_student_marks.py",
    SOURCE_ROOT / "marks" / "update_delete_grade_records.py",
    SOURCE_ROOT / "performance" / "display_individual_performance.py",
    SOURCE_ROOT / "performance" / "display_c ourse_performance.py",
    SOURCE_ROOT / "reports" / "export_student_report.py",
    SOURCE_ROOT / "reports" / "export_course_report.py",
    SOURCE_ROOT / "reports" / "export_performance_report.py",
]

for source_file in SOURCE_FILES:
    source_code = source_file.read_text(encoding="utf-8")
    exec(compile(source_code, str(source_file), "exec"), globals())


TextColors = globals()["TextColors"]
initialize_files = globals()["initialize_files"]
add_student = globals()["add_student"]
add_course = globals()["add_course"]
add_exam_details = globals()["add_exam_details"]
record_student_marks = globals()["record_student_marks"]
display_individual_performance = globals()["display_individual_performance"]
display_course_summary = globals()["display_course_summary"]
export_performance_report = globals()["export_performance_report"]
update_student_details = globals()["update_student_details"]
delete_student = globals()["delete_student"]
update_course = globals()["update_course"]
delete_course = globals()["delete_course"]
update_exam_details = globals()["update_exam_details"]
delete_exam_details = globals()["delete_exam_details"]
update_grade_record = globals()["update_grade_record"]
delete_grade_record = globals()["delete_grade_record"]


# Main menu for the Student Grading System
def main_menu():
    initialize_files()

    while True:
        print("\n==============================")
        print("  Student Grading System")
        print("==============================")
        print("1. Add a new student")
        print("2. Add a new course")
        print("3. Add exam details")
        print("4. Record student marks")
        print("5. Display individual student performance")
        print("6. Display course performance summary")
        print("7. Export performance report")
        print("8. Update a student details")
        print("9. Delete a student record")
        print("10. Update a course details")
        print("11. Delete a course")
        print("12. Update existing exam details")
        print("13. Delete an exam details")
        print("14. Update existing grade")
        print("15. Delete a grade record")
        print("16. Exit")
        choice = input("Enter your choice (1-16): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            add_course()
        elif choice == "3":
            add_exam_details()
        elif choice == "4":
            record_student_marks()
        elif choice == "5":
            display_individual_performance()
        elif choice == "6":
            display_course_summary()
        elif choice == "7":
            export_performance_report()
        elif choice == "8":
            update_student_details()
        elif choice == "9":
            delete_student()
        elif choice == "10":
            update_course()
        elif choice == "11":
            delete_course()
        elif choice == "12":
            update_exam_details()
        elif choice == "13":
            delete_exam_details()
        elif choice == "14":
            update_grade_record()
        elif choice == "15":
            delete_grade_record()
        elif choice == "16":
            print("You have exit the program.")
            break
        else:
            print(TextColors.RED_BOLD + "Invalid choice" + TextColors.RESET +
                  ". Please enter a number from " + TextColors.CYAN_BOLD + "1 to 16" + TextColors.RESET + ".")


if __name__ == "__main__":
    main_menu()