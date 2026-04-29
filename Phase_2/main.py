import os
from Phase_1.main import write_report, log_honour_roll, compare_classes, find_absent_students

student_list = [
	{'name':'Amit',   'score':88,'grade':'B','attendance':[18,20,17,19],'note':'Consistent and focused.'},
	{'name':'Anisha', 'score':95,'grade':'A','attendance':[20,20,19,20],'note':'Exceptional work ethic.'},
	{'name':'Kavya',  'score':52,'grade':'F','attendance':[9, 7, 10, 8],'note':'Needs significant support.'},
	{'name':'Pratham','score':73,'grade':'C','attendance':[17,18,16,15],'note':'Steady but can improve.'},
	{'name':'Pooja',  'score':61,'grade':'D','attendance':[14,13,15,12],'note':'Irregular attendance.'},
	{'name':'Varsha', 'score':91,'grade':'A','attendance':[20,20,19,20],'note':'Outstanding performance.'},
	{'name':'Shubham','score':67,'grade':'C','attendance':[16,15,17,14],'note':'Could push harder.'},
	{'name':'Virat',  'score':84,'grade':'B','attendance':[18,19,20,18],'note':'Strong and reliable.'},
	{'name':'Shiva',  'score':78,'grade':'B','attendance':[17,18,16,19],'note':'Good overall progress.'},
]

class_a = ['Amit', 'anisha ', 'KAVYA', 'pratham']
class_b = [' Pooja', 'Varsha', 'kavya', 'Rahul']

# Part 13 — Building the File System
def setup_student_folders(base_folder, student_list):
	os.makedirs(base_folder, exist_ok=True)

	for student in student_list:
		folder_name = student["name"].lower()

		folder_path = os.path.join(base_folder, folder_name)
		os.makedirs(folder_path, exist_ok=True)

		with open(os.path.join(folder_path, "info.txt"), "w") as f:
			f.write(
				f"name: {student['name'].strip().title()}\n"
				f"score: {int(student['score'])}\n"
				f"grade: {student['grade'].strip().upper()}\n"
			)

		with open(os.path.join(folder_path, "attendance.txt"), "w") as f:
			for session in student["attendance"]:
				f.write(f"{session}\n")

		with open(os.path.join(folder_path, "notes.txt"), "w") as f:
			f.write(student["note"] + "\n")
	return "setup complete."

# Part 14 — Reading the File System
def read_student_info(student_folder):
	try:
		student={}
		with open(os.path.join(student_folder, "info.txt"), "r") as f:
			for line in f:
				parts=line.strip().split(":", 1)
				if len(parts)==2:
					key=parts[0].strip()
					value=parts[1].strip()

					if key=="score":
						value=int(value)

					student[key]=value

		return student

	except FileNotFoundError:
		return None

def read_all_students(base_folder):
	folders=[]
	students=[]

	for student in student_list:
		folder_name=student["name"].lower()
		folders.append(folder_name)

	for folder in folders:
		info=read_student_info(os.path.join(base_folder, folder))

		if info is not None:
			students.append(info)
	return students

# Part 15 — Attendance
def write_attendance(student_folder, sessions):
	try:
		with open(student_folder+"/attendance.txt", "a") as f:
			for number in sessions:
				f.write(str(number)+"\n")
		return "success! Attendence updated"
	except FileNotFoundError as e:
		return f"error: Failed! {e}"

def read_attendance(student_folder):
	attendance_list=[]
	try:
		with open(student_folder+"/attendance.txt", "r") as f:
			data=f.readlines()
			for line in data:
				attendance_list.append(int(line))
		return attendance_list
	except:
		return []

def total_attendance(student_folder):
	numbers=read_attendance(student_folder)
	total=0
	for number in numbers:
		total+=number
	return total
# Part 12 — The Phase 2 Menu
def class_menu():

	options=[
		"Rebuild student folders",
		"Write class report",
		"Log honour roll",
		"Record attendance session",
		"Show total attendance",
		"Compare classes and find absent students",
		"Update student score",
		"List student folders",
		"Student report card"
	]

	base_folder="Phase_2/"
	students=read_all_students(base_folder)

	while True:
		print("---Main Menu---")
		print(f"{len(students)} records were loaded")

		for index, option in enumerate(options, start=1):
			print(f"{index}: {option}")

		print("0: exit")

		choice=input("Enter a choice: ").strip()

		match choice:
			case "1":
				print(setup_student_folders(base_folder, student_list))
				students=read_all_students(base_folder)

			case "2":
				print(write_report("report.txt", students))

			case "3":
				print(log_honour_roll("report.txt", student_list))

			case "4":
				print(f"{options[int(choice)-1]} in development")
			case "5":
				print(f"{options[int(choice)-1]} in development")
			case "6":
				print(compare_classes(class_a, class_b))
				present=input("Enter student names, (comma separated): ").split(",")
				full_roll=[]
				for student in students:
					full_roll.append(student["name"])
				print(find_absent_students(set(present), full_roll))

			case "7":
				print(f"{options[int(choice)-1]} in development")
			case "8":
				print(f"{options[int(choice)-1]} in development")
			case "9":
				print(f"{options[int(choice)-1]} in development")
			case "0":
				print("Good bye")
				break

			case _:
				print("invalid choice. Please try again")

if __name__=="__main__":
	class_menu()