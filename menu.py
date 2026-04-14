import os

def read_students(file_name):
	student_data=[]
	file_name="students.txt"
	with open(file_name, "r") as f:
		for line in f:
			data={}
			parts=line.split()
			data["name"]=parts[0]
			data["marks"]=parts[1]
			data["grade"]=parts[2]
			student_data.append(data)
	return student_data


def class_menu():
	student_data=read_students("students.txt")
	while True:
		print("--Main Menu--")
		print(f"{len(student_data)} records were loaded")
		print("1. Write class report")
		print("2. Log honour roll")
		print("3. Compare classes / find absent students")
		print("4. Update student score")
		print("5. Search by student ID")
		print("6. Manage files")
		print("7. Student report card")
		print("0. Exit")
		choice=input("Enter your choice: ")
		match choice:
			case "1":
				print("In development")
			case "2":
				print("In development")
			case "3":
				print("In development")
			case "4":
				print("In development")
			case "5":
				print("In development")
			case "6":
				print("In development")
			case "7":
				print("In development")
			case "0":
				print("exiting program")
				break
			case _:
				print("invalid choice.")


class_menu()