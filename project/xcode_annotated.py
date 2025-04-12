MAXIMUM_STUDENT_LIMIT = 100
# REVIEW [CR004]: Line length exceeds 80-120 characters. -> SUGGESTION: Break the line into multiple lines or shorten variable names.
DEFAULT_ENROLLMENT_YEAR = 2024
# REVIEW [CR004]: Line length exceeds 80-120 characters. -> SUGGESTION: Break the line into multiple lines or shorten variable names.
STUDENT_ID_LENGTH_LIMIT = 10
# REVIEW [CR004]: Line length exceeds 80-120 characters. -> SUGGESTION: Break the line into multiple lines or shorten variable names.

# REVIEW [CR001]: Constant name exceeds 10 characters. -> SUGGESTION: Rename to STUDENT_LIMIT
# REVIEW [CR005]: Missing docstring for global variable `studentsDatabase`. -> SUGGESTION: Add a docstring explaining the purpose and usage of `studentsDatabase`, e.g.,  `studentsDatabase = {}  # Dictionary to store student data.`
studentsDatabase = {}
# REVIEW [CR001]: Constant name exceeds 10 characters. -> SUGGESTION: Rename to DEFAULT_YEAR

# REVIEW [CR005]: Missing docstring for global variable `STUDENT_KEY`. -> SUGGESTION: Add a docstring explaining the purpose and usage of `STUDENT_KEY`, e.g., `STUDENT_KEY = "sk-test-abc1234567890xyz"  # Placeholder API key (for demonstration only).` or better yet, remove the hardcoded key.
STUDENT_KEY = "sk-test-abc1234567890xyz"
# REVIEW [CR001]: Variable name should use snake_case. -> SUGGESTION: Rename to students_database
# REVIEW [CR004]: Line length exceeds 80-120 characters. -> SUGGESTION: Break the line into multiple lines.

def addStudent(studentId, name, age, enrollmentYear=DEFAULT_ENROLLMENT_YEAR):
# REVIEW [CR001]: Constant name exceeds 10 characters and should be uppercase. -> SUGGESTION: Rename to STUDENT_API_KEY
# REVIEW [CR005]: Missing docstring for function `addStudent`. -> SUGGESTION: Add a docstring describing the function's purpose, parameters, and return value.  Example: `def addStudent(studentId, name, age, enrollmentYear=DEFAULT_ENROLLMENT_YEAR):
    """Adds a new student to the database.

    Args:
        studentId: The student's ID.
        name: The student's name.
        age: The student's age.
        enrollmentYear: The student's enrollment year (defaults to DEFAULT_ENROLLMENT_YEAR).
    """
    if len(studentsDatabase) >= MAXIMUM_STUDENT_LIMIT:
    # REVIEW [CR002]: Hardcoded API key -> SUGGESTION: Load the API key from an environment variable using `os.getenv('API_KEY')` or a secrets management service.
        print("Student limit reached. Cannot add more students.")
        # REVIEW [CR001]: Function name should use snake_case. -> SUGGESTION: Rename to add_student
        return

    if len(studentId) > STUDENT_ID_LENGTH_LIMIT:
        print("Student ID exceeds maximum allowed length.")
        # REVIEW [CR007]: Insecure use of hardcoded API key -> SUGGESTION: Use environment variables or a secure secrets management system to store and access the API key.  Remove the key from the codebase.
        return
        # REVIEW [CR002]: Printing API key -> SUGGESTION: Remove the print statement.  Never log or print sensitive information.

    if studentId in studentsDatabase:
    # REVIEW [CR009]: Insecure logging of API key -> SUGGESTION: Remove the printing of the API key.  Consider using a logging system that allows for different log levels and filtering sensitive information.
    # REVIEW [CR010]: Use of print() for logging and insecure logging of API key -> SUGGESTION: Replace print() with proper logging using the logging module.  Do not log secrets like API keys. Consider using environment variables to store sensitive information.
        print("Student with this ID already exists.")
        return

    # Insecure use of dummy API key (violation)
    print(f"Using API Key: {STUDENT_KEY} to validate student enrollment...")

    studentsDatabase[studentId] = {
        "name": name,
        # REVIEW [CR005]: Missing docstring for function `viewAllStudents`. -> SUGGESTION: Add a docstring describing the function's purpose and behavior. Example: `def viewAllStudents():
    """Displays all student records in the database."""`
        # REVIEW [CR010]: Use of print() for logging -> SUGGESTION: Replace print() with proper logging using the logging module.
        "age": age,
        "enrollmentYear": enrollmentYear
    }
    print(f"Student {name} added successfully.")

def viewAllStudents():
    if not studentsDatabase:
        print("No student records found.")
        # REVIEW [CR001]: Function name should use snake_case. -> SUGGESTION: Rename to view_all_students
        # REVIEW [CR010]: Use of print() for logging -> SUGGESTION: Replace print() with proper logging using the logging module.
        return
        # REVIEW [CR005]: Missing docstring for function `searchStudentById`. -> SUGGESTION: Add a docstring describing the function's purpose, parameter, and return value (implicitly None). Example: `def searchStudentById(studentId):
    """Searches for a student by ID and prints their information.

    Args:
        studentId: The ID of the student to search for.
    """`

    print("All Students:")
    for studentId, info in studentsDatabase.items():
        print(f"ID: {studentId}, Name: {info['name']}, Age: {info['age']}, Year: {info['enrollmentYear']}")

def searchStudentById(studentId):
    student = studentsDatabase.get(studentId)
    # REVIEW [CR010]: Use of print() for logging -> SUGGESTION: Replace print() with proper logging using the logging module.
    if student:
        print(f"Student Found - ID: {studentId}, Name: {student['name']}, Age: {student['age']}, Year: {student['enrollmentYear']}")
        # REVIEW [CR001]: Function name should use snake_case. -> SUGGESTION: Rename to search_student_by_id
        # REVIEW [CR005]: Missing docstring for function `deleteStudent`. -> SUGGESTION: Add a docstring describing the function's purpose, parameter, and return value (implicitly None). Example: `def deleteStudent(studentId):
    """Deletes a student from the database.

    Args:
        studentId: The ID of the student to delete.
    """`
    else:
        print("Student not found.")
        # REVIEW [CR004]: Line length exceeds 80-120 characters. -> SUGGESTION: Break the line into multiple lines.

def deleteStudent(studentId):
# REVIEW [CR010]: Use of print() for logging -> SUGGESTION: Replace print() with proper logging using the logging module.
    if studentId in studentsDatabase:
        del studentsDatabase[studentId]
        # REVIEW [CR004]: Line length exceeds 80-120 characters. -> SUGGESTION: Break the line into multiple lines.
        print(f"Student with ID {studentId} deleted successfully.")
    else:
        print("Student ID not found.")

# REVIEW [CR001]: Function name should use snake_case. -> SUGGESTION: Rename to delete_student
# REVIEW [CR010]: Use of print() for logging -> SUGGESTION: Replace print() with proper logging using the logging module.
# Sample usage
if __name__ == "__main__":
    addStudent("stu001", "Alice", 20)
    addStudent("stu002", "Bob", 21)
    viewAllStudents()
    searchStudentById("stu001")
    deleteStudent("stu002")
    viewAllStudents()