


import marks

#Add marks for students
marks.add_marks(101, [90, 85, 95, 80, 90])
marks.add_marks(102, [70, 75, 80, 65, 70])
marks.add_marks(103, [40, 45, 50, 35, 40])

marks.display_marks(101)
marks.display_marks(102)
marks.display_marks(102)


#Test individual calculations
print("\n----- Individual Calculations -----")

print("Total: ", marks.calculate_total(101))
print("Average: ", marks.calculate_average(101))
print("Percentage: ", marks.calculate_percentage(101))
print("Grade: ", marks.calculate_grade(101))



