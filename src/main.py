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