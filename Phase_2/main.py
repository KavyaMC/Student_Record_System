import os
from Phase_1.main import (
	write_report,
	log_honour_roll,
	compare_classes,
	find_absent_students,
	honour_roll,
	celebrate_student
	)

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
		return "success! Attendance updated"
	except FileNotFoundError as e:
		return f"error: Failed! {e}"

def read_attendance(student_folder):
	attendance_list=[]
	try:
		with open(student_folder+"/attendance.txt", "r") as f:
			data=f.readlines()
			for line in data:
				attendance_list.append(int(line.strip()))
		return attendance_list
	except:
		return []

def total_attendance(student_folder):
	numbers=read_attendance(student_folder)
	total=0
	for number in numbers:
		total+=number
	return total

def safe_delete(filepath):
	try:
		if os.path.exists(filepath):
			os.remove(filepath)
		return "Success! File deleted."
	except Exception as e:
		return f"Error: {e}"

def list_student_folders(base_folder):
	try:
		current_location = os.getcwd()
		os.chdir(base_folder)
		data=os.listdir()
		folders=[]
		files=[]
		for each in data:
			if os.path.isdir(each):
				folders.append(each)
			else:
				files.append(each)
				if each.startswith("old_"):
					safe_delete(each)
					continue
		os.chdir(current_location)
		return folders
	except Exception as e:
		return f"Error: {e}"

def search_student(students, name):
	index=0
	while index < len(students):
		if name .lower() == students[index]["name"].lower():
			return index
		index+=1
	return -1

def read_student_note(student_folder):
	try:
		with open(student_folder+"/notes.txt", "r") as f:
			return f.readline().strip()
	except FileNotFoundError:
		return "error: file not found"

def read_all_notes(student_folder):
	try:
		lines=[]
		with open(student_folder+"/notes.txt", "r") as f:
			lines.append(f.readline().strip())
			data=f.readlines()
			for line in data:
				lines.append(line.strip())
		return lines
	except:
		return []

def update_student_info(base_folder, name, new_score):
	file_path = os.path.join(base_folder, name.lower())
	student=read_student_info(file_path)
	if student==None:
		return "student not found"
	student["score"]=int(new_score)
	if new_score >= 90:
		student["grade"]="A"
	elif new_score >= 75:
		student["grade"]="B"
	elif new_score >= 60:
		student["grade"]="C"
	elif new_score >= 50:
		student["grade"]="D"
	else:
		student["grade"]="F"

	try:
		with open(os.path.join(file_path, "info.txt"), "w") as f:
			for key in student:
				f.write(f"{key}: {student[key]}\n")
		return "student info updated succesffully!"
	except:
		return "error writing file"

def print_report_card(student, students, base_folder):
	try:
		note=read_student_note(os.path.join(base_folder, student["name"].lower()))
		if note == "error: file not found":
			return "student record incomplete"
		roll=honour_roll(students)
		student["note"]=note
		for name in roll:
			if student["name"].lower() == name.lower():
				student["honour roll"]="on honour roll"
				break
		else:
			student["honour roll"]="not on honour roll"
		return student
	except Exception as e:
		return f"error: {e}"

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
				name=input("Enter student name: ").strip().lower()
				try:
					new_score=int(input("Enter new score (0, 100): "))
				except ValueError:
					return "invalid input"
				message=update_student_info("Phase_2", name, new_score)
				print(message)

			case "8":
				print(list_student_folders("Phase_2"))

			case "9":
				name=input("Enter student name: ").strip().lower()
				student_dict={}
				for student in students:
					if name.lower() == student["name"].lower():
						student_dict=student
				if student_dict == {}:
					print("student not found")
				else:
					result = print_report_card(student_dict, students, "Phase_2")
					print(result)
					print(celebrate_student(student_dict["name"], 0, student_dict["score"], student_dict["grade"]))

			case "0":
				print("Good bye")
				break

			case _:
				print("invalid choice. Please try again")

if __name__=="__main__":
	class_menu()