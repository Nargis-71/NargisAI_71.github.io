#============================
#QUESTION 01: STUDENT MARKS
#=========================

hours = float(input("Enter hours worked:"))
rate = float(input("Enter hourly rate:"))

if hours <= 40:
    pay = hours * rate
else:
    pay = (40 * rate) + ((hours - 40) * rate * 1.5)

print("Total Pay:", pay)


#============================
#QUESTION 02: CALCULATOR
#=========================


name=input("Enter student`s name:")
roll_no= input("Enter roll number:")

marks1= float(input("Enter marks for Subject 1:"))
marks2= float(input("Enter marks for Subject 2:"))
marks3= float(input("Enter marks for Subject 3:"))
marks4= float(input("Enter marks for Subject 4:"))
marks5= float(input("Enter marks for Subject 5:"))
total= marks1 + marks2 + marks3 + marks4 + marks5
percentage = (total/500) * 100

if percentage >= 80:
     grade = "A+"
elif percentage >= 70:
     grade = "A+"
elif percentage >= 60:
     grade = "B+"
elif percentage >= 50:
     grade = "C+"
elif percentage >= 40:
     grade = "D+"
else:
     grade = "F"

if (marks1 < 40 or marks2 < 40 or marks3 < 40 or
         marks4 < 40 or marks5 < 40):  result = "Fail"

else:
   result = "Passed"

print("\n----- MARKSHEET -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Subject 1:", marks1)
print("Subject 2:", marks2)
print("Subject 3:", marks3)
print("Subject 4:", marks4)
print("Subject 5:", marks5)
print("Total Marks:", total)
print("Percentage:", percentage,"%")
print("Grade:", grade)
print("Result:", result) 