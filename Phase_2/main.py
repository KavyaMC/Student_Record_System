import os
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
	os.chdir(base_folder)
	for student in student_list:
		folder_name=student["name"].lower()
		try:
			os.makedirs(folder_name, exist_ok=True)
		except FileExistsError:
			pass

		os.chdir(folder_name)
		with open("info.txt", "w") as f:
			f.write(
				f"name: {student['name'].strip().title()}\n"
				f"marks: {int(student['score'])}\n"
				f"grade: {student['grade'].strip().upper()}\n"
			)

		with open("attendance.txt", "w") as f:
			for session in student["attendance"]:
				f.write(f"{session}\n")

		with open("notes.txt", "w") as f:
			f.write(student["note"])

		os.chdir(base_folder)
	return "setup complete"

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
	while True:
		print("---Main Menu---")
		for index, option in enumerate(options, start=1):
			print(f"{index}: {option}")

		print("0: exit")
		choice=input("Enter a choice: ").strip()
		match choice:

			case "1":
				print(setup_student_folders(r"C:\Users\admin\Documents\GitHub\Student_Record_System\Phase_2", student_list))
			case "2":
				print(f"{options[int(choice)-1]} in development")
			case "3":
				print(f"{options[int(choice)-1]} in development")
			case "4":
				print(f"{options[int(choice)-1]} in development")
			case "5":
				print(f"{options[int(choice)-1]} in development")
			case "6":
				print(f"{options[int(choice)-1]} in development")
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