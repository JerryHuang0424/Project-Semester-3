#This file is used to store the students whose last name are all Evans
#Author :Jerry Huang
#First create a list stored some of the students.

# Create a list
StudentsList = ["Lisa", "Liam", "Leo", "Larry", "Linda"]

for i in range(0,len(StudentsList)):
	print(StudentsList[i] + " " + "Evans")

newName = input("Please enter the new name: ")

StudentsList.append(newName)

for i in range(0, len(StudentsList)):
	print(StudentsList[i] + " " + "Evans")
