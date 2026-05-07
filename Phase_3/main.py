import os
from Phase_1.main import write_report
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


# Part 21 — The Student Class
class Student:
	def __init__(self, name, score, attendance, note):
		self.name=name.strip().lower()
		self.score=int(score)
		self.attendance=attendance
		self.note=note
		self.grade = self._calculate_grade()


	def _calculate_grade(self):
		if self.score >= 90 and self.score <= 100:
			return "A"
		elif self.score >= 75:
			return "B"
		elif self.score >= 60:
			return "C"
		elif self.score >= 50:
			return "D"
		else:
			return "F"

	def update_score(self, new_score):
		self.score = new_score
		self.grade = self._calculate_grade()

	def log_attendance(self, session):
			self.attendance.append(int(session))

	def save_to_disk(self, base_folder):
		try:
			folder_path=os.path.join(base_folder, self.name.lower())
			os.makedirs(folder_path, exist_ok=True)

			with open(os.path.join(folder_path, "info.txt"), "w") as f:
				f.write(f"name: {self.name.strip().title()}\n")
				f.write(f"score: {self.score}\n")

			with open(os.path.join(folder_path, "attendance.txt"), "w") as f:
				for session in self.attendance:
					f.write(str(session)+"\n")

			with open(os.path.join(folder_path, "notes.txt"), "w") as f:
				f.write(self.note)
			return f"files created successfully"
		except Exception as e:
			return f"error: {e}"

	@classmethod
	def load_from_folder(cls, folder_path):
		try:
			lines={}
			with open(os.path.join(folder_path, "info.txt"), "r") as f:
				for line in f:
					parts=line.split(":")
					if len(parts) >2:
						key=parts[0].strip().lower()
						value=parts[1].strip()
						lines[key]=value
			attendance=[]
			with open(os.path.join(folder_path, "attendance.txt"), "r") as f:
				for line in f:
					attendance.append(line)
					lines["attendance"]=attendance
			with open(os.path.join(folder_path, "notes.txt"), "r") as f:
				lines["note"]=f.readline()
			return cls(lines["name"], lines["score"], lines["attendance"], lines["note"])
		except Exception as e:
			return f"error: {e}"

# Part 22 — Dunder Methods and the Roster
	def __str__(self):
		return f"name: {self.name}\n score: {self.score}\n grade: {self._calculate_grade()}\n attendance: {self.attendance}\n note: {self.note}"

	def __repr__(self):
		return f"{self.name} {self.score} {self._calculate_grade()} {self.attendance} {self.note}"

# Part 20 — The Phase 3 Menu
def class_menu():
	options=[
		"Class statistics",
		"Top student report",
		"Update student score",
		"Log attendance session",
		"View student report card",
		"Reload individual student from disk",
		"Reload full roster"
	]
	S1=Student("amit", 88, [17, 22, 3], "Well Done")
	title=str("Student Record System").strip().upper().center(40)
	while True:
		print(f"{title}\n")
		for idx, option in enumerate(options, 1):
			print(f"{idx}. {option}")
		print("0. exit program")
		choice=input(f"Select an ption (1-{len(options)}): ").strip()
		match choice:
			case "1":
				print(f"{options[int(choice)-1]} in {title} menu in development.")
			case "2":
				print(f"{options[int(choice)-1]} in {title} menu in development.")
			case "3":
				new_score=int(input("Enter student score: ").strip())
				S1.update_score(new_score)

			case "4":
				name=input("Enter student name: ").strip().lower()
				session=int(input("Enter student attendance: ").strip())
				S1.log_attendance(session)
				S1.save_to_disk("Phase_3")

			case "5":
				print(f"{options[int(choice)-1]} in {title} menu in development.")
			case "6":
				name=input("Enter student name: ").strip().lower()
				Student.load_from_folder("Phase_3/"+name)

			case "7":
				print(f"{options[int(choice)-1]} in {title} menu in development.")
			case "0":
				print(f"Exiting {title} menu. Thank you for using the program.")
				break
			case _:
				if not (1 <= int(choice) <= len(options)) and choice.isalpha():
					print("invalid input. please try again")


if __name__ == "__main__":
	class_menu()
