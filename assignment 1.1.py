# Question 1
a = int(input("Enter first number = "))
b = int(input("Enter second number = "))
c = int(input("Enter third number = "))
print("The average of numbers is ", (a+b+c)/3)

# Question 2
gross_income = int(input("Enter your gross income"))
standard_deduction = 10000
dependent_deduction = 3000
no_of_dependents = int(input("Enter total no. of dependents"))
taxable_income = gross_income - standard_deduction - (dependent_deduction * no_of_dependents)
tax = taxable_income * 0.5
print(taxable_income)
print(tax)

# Question 3
SID = int(input("Enter your SID"))
Name = input("Enter your name")
Gender = input("Enter your Gender ")
Course_name = input("Enter your course name")
CGPA = float(input("Enter your CGPA"))
STUDENT = [SID, Name, Gender, Course_name, CGPA]
print(STUDENT)

# Question 4
marks = []
for i in range(5):
    marks.append(input("Enter marks"))
marks.sort()
print(marks)

# Question 5
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.remove(color[3])
print("Part 'a' : ", color)

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5] = ['Purple']
print("Part 'b' :", color)