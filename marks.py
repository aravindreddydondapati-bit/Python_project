

#Marks Management Module

student_marks = {}

#Add marks
def add_marks(roll_number, marks):
    if roll_number in student_marks:
        print("Marks already exist for this student!")
        return
    if len(marks) != 5:
        printf("Please enter marks for exactly 5 subjects!")
        return
    for mark in marks:
        if mark < 0 or mark > 100:
            print("Marks must be between 0and 100!")
            return

    student_marks[roll_number] = marks

    print("Marks added successfully!")


#calculate Tool Marks
def calculate_total(roll_number):
    if roll_number not in student_marks:
        print("Marks not found!")
        return None
    total = 0

    for mark in student_marks[roll_number]:
        total += mark
    return total



# Calculate Average
def calculate_average(roll_number):

    total = calculate_total(roll_number)

    if total is None:
        return None

    average = total / 5

    return average


# Calculate Percentage
def calculate_percentage(roll_number):

    total = calculate_total(roll_number)

    if total is None:
        return None

    percentage = (total / 500) * 100

    return percentage





# Calculate Grade
def calculate_grade(roll_number):

    percentage = calculate_percentage(roll_number)

    if percentage is None:
        return None

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "Fail"




# Display Marks
def display_marks(roll_number):

    if roll_number not in student_marks:
        print("Marks not found!")
        return

    total = calculate_total(roll_number)
    average = calculate_average(roll_number)
    percentage = calculate_percentage(roll_number)
    grade = calculate_grade(roll_number)

    print("\n----- Student Marks -----")
    print("Roll Number:", roll_number)
    print("Subject Marks:", student_marks[roll_number])
    print("Total Marks:", total, "/ 500")
    print("Average:", average)
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
