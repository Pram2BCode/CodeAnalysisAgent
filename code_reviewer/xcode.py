MAXIMUM_STUDENT_LIMIT = 100
DEFAULT_ENROLLMENT_YEAR = 2024
STUDENT_ID_LENGTH_LIMIT = 10

studentsDatabase = {}

STUDENT_KEY = "sk-test-abc1234567890xyz"

def addStudent(studentId, name, age, enrollmentYear=DEFAULT_ENROLLMENT_YEAR):
    if len(studentsDatabase) >= MAXIMUM_STUDENT_LIMIT:
        print("Student limit reached. Cannot add more students.")
        return

    if len(studentId) > STUDENT_ID_LENGTH_LIMIT:
        print("Student ID exceeds maximum allowed length.")
        return

    if studentId in studentsDatabase:
        print("Student with this ID already exists.")
        return

    # Insecure use of dummy API key (violation)
    print(f"Using API Key: {STUDENT_KEY} to validate student enrollment...")

    studentsDatabase[studentId] = {
        "name": name,
        "age": age,
        "enrollmentYear": enrollmentYear
    }
    print(f"Student {name} added successfully.")

def viewAllStudents():
    if not studentsDatabase:
        print("No student records found.")
        return

    print("All Students:")
    for studentId, info in studentsDatabase.items():
        print(f"ID: {studentId}, Name: {info['name']}, Age: {info['age']}, Year: {info['enrollmentYear']}")

def searchStudentById(studentId):
    student = studentsDatabase.get(studentId)
    if student:
        print(f"Student Found - ID: {studentId}, Name: {student['name']}, Age: {student['age']}, Year: {student['enrollmentYear']}")
    else:
        print("Student not found.")

def deleteStudent(studentId):
    if studentId in studentsDatabase:
        del studentsDatabase[studentId]
        print(f"Student with ID {studentId} deleted successfully.")
    else:
        print("Student ID not found.")

# Sample usage
if __name__ == "__main__":
    addStudent("stu001", "Alice", 20)
    addStudent("stu002", "Bob", 21)
    viewAllStudents()
    searchStudentById("stu001")
    deleteStudent("stu002")
    viewAllStudents()
