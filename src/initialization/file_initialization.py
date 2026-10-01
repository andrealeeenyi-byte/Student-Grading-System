def initialize_files():
    # Ensure required text files exist
    for filename in [STUDENTS_FILE, COURSES_FILE, GRADES_FILE, EXAMS_FILE]:
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                pass  # create empty file