# Importing necessary libraries
import numpy as np

# Prompting user to enter number of students and subjects
num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

# Initializing empty lists for storing grades and names
grades = []
names = []

# Looping through each student and subject to get their grades
for i in range(num_students):
    name = input("Enter the name of student {}: ".format(i+1))
    names.append(name)
    student_grades = []
    for j in range(num_subjects):
        grade = float(input("Enter the grade for subject {}: ".format(j+1)))
        while grade < 0 or grade > 100:
            grade = float(input("Invalid grade. Enter the grade for subject {}: ".format(j+1)))
        student_grades.append(grade)
    grades.append(student_grades)

# Converting grades list to numpy array for easier calculations
grades = np.array(grades)

# Calculating average grade for each student
avg_grades = np.mean(grades, axis=1)

# Determining letter grade for each student based on average grade
letter_grades = []
for avg_grade in avg_grades:
    if avg_grade >= 90:
        letter_grades.append("A")
    elif avg_grade >= 80:
        letter_grades.append("B")
    elif avg_grade >= 70:
        letter_grades.append("C")
    elif avg_grade >= 60:
        letter_grades.append("D")
    else:
        letter_grades.append("F")

# Displaying the average grade and letter grade for each student
for i in range(num_students):
    print("Name: {}, Average Grade: {:.2f}, Letter Grade: {}".format(names[i], avg_grades[i], letter_grades[i]))

# Calculating class average grade
class_avg_grade = np.mean(avg_grades)
print("Class Average Grade: {:.2f}".format(class_avg_grade))
