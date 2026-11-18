# Student Management Module

# Lists to store student details
student_names = []
roll_numbers = []


# Function to add a student
def add_student(name, roll_number):

    if roll_number in roll_numbers:
        print("Roll number already exists!")
        return

    student_names.append(name)
    roll_numbers.append(roll_number)

    print("Student added successfully!")


# Function to display all students
def display_students():

    if len(roll_numbers) == 0:
        print("No student records found!")
        return

    print("\nStudent Details")

    for i in range(len(roll_numbers)):
        print("Name:", student_names[i])
        print("Roll Number:", roll_numbers[i])
        print("--------------------")


# Function to search for a student
def search_student(roll_number):

    if roll_number in roll_numbers:
        index = roll_numbers.index(roll_number)

        print("Student Found!")
        print("Name:", student_names[index])
        print("Roll Number:", roll_numbers[index])

    else:
        print("Student not found!")


# Function to delete a student
def delete_student(roll_number):

    if roll_number in roll_numbers:
        index = roll_numbers.index(roll_number)

        student_names.pop(index)
        roll_numbers.pop(index)

        print("Student deleted successfully!")

    else:
        print("Student not found!")
