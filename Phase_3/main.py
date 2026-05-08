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
		self.score = int(new_score)
		self.grade = self._calculate_grade()

	def log_attendance(self, session):
			self.attendance.append(int(session))
			return self

	def save_to_disk(self, base_folder):
		try:
			folder_path=os.path.join(base_folder, self.name.lower())
			os.makedirs(folder_path, exist_ok=True)

			with open(os.path.join(folder_path, "info.txt"), "w") as f:
				f.write(f"name: {self.name.strip().title()}\n")
				f.write(f"score: {self.score}\n")
				f.write(f"grade: {self.grade}")

			with open(os.path.join(folder_path, "attendance.txt"), "w") as f:
				for session in self.attendance:
					f.write(f"{session}\n")

			with open(os.path.join(folder_path, "notes.txt"), "w") as f:
				f.write(self.note)
			return f"files created successfully"
		except Exception as e:
			return f"error: {e}"

	@classmethod
	def load_from_folder(cls, folder_path):
		try:
			with open(os.path.join(folder_path, "info.txt"), "r") as f:
				lines = f.readlines()
				name = lines[0].split(":")[1].strip()
				score = int(lines[1].split(":")[1].strip())

			attendance = []
			with open(os.path.join(folder_path, "attendance.txt"), "r") as f:
				for line in f:
					attendance.append(int(line.strip()))

			with open(os.path.join(folder_path, "notes.txt"), "r") as f:
				note = f.readline().strip()
			return cls(name, score, attendance, note)

		except Exception as e:
			print(f"Error loading student: {e}")
			return None

# Part 22 — Dunder Methods and the Roster
	def __str__(self):
		return (
			f"Student: {self.name.title()}\n"
			f"Score:   {self.score}  |  Grade: {self.grade}\n"
			f"Attendance:     {sum(self.attendance)} total sessions\n"
			f"Note:    {self.note}\n"
		)

	def __repr__(self):
		return (
			f"Student('{self.name.title()}', "
			f"score={self.score}, "
			f"grade='{self.grade}')"
		)

class Roster:
	def __init__(self):
		self.students=[]

	def add_student(self, student):
		self.students.append(student)

	def get_class_average(self):
		if len(self.students)==0:
			return 0
		total=0
		for student in self.students:
			total+=student.score
		return round(total/len(self.students),2)

	def get_honour_roll(self):
		average=self.get_class_average()
		honor_roll=[]
		for student in self.students:
			if student.score > average and student.grade!="F":
				honor_roll.append(student.name.upper())
		return honor_roll

	def get_top_student(self):
		if len(self.students)==0:
			return None
		top_student = self.students[0]
		for student in self.students:
			if student.score > top_student.score:
				top_student=student
		return top_student

	@classmethod
	def load_all(cls, base_folder):
		roster = cls()
		if not os.path.exists(base_folder):
			return roster
		for folder in os.listdir(base_folder):
			if folder != "__pycache__":
				folder_path = os.path.join(base_folder, folder)
				if os.path.isdir(folder_path):
					student = Student.load_from_folder(folder_path)
					if student is not None:
						roster.add_student(student)
		return roster

	@classmethod
	def create_from_data(cls, student_list, base_folder):
		roster = cls()
		for data in student_list:

			student = Student(
				data["name"],
				data["score"],
				data["attendance"],
				data["note"]
			)

			student.save_to_disk(base_folder)
			roster.add_student(student)
		return roster

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
	roster = Roster.load_all("Phase_3")
	title=str("Student Record System").strip().upper().center(40)
	while True:
		print(f"{title}\n")
		for idx, option in enumerate(options, 1):
			print(f"{idx}. {option}")
		print("0. exit program")
		choice=input(f"Select an ption (1-{len(options)}): ").strip()
		if not choice.isdigit():
			print("invalid input. please try again")
			continue

		match choice:
			case "1":
				print(f"Class Average: {roster.get_class_average()}")
				print("Honour Roll:")
				for student in roster.get_honour_roll():
					print(student)

			case "2":
				top_student = roster.get_top_student()
				if top_student:
					print(top_student)
				else:
					print("No students loaded.")

			case "3":
				name=input("Enter student name: ").strip().lower()
				new_score=int(input("Enter student score: ").strip())
				for student in roster.students:
					if student.name == name:
						student.update_score(new_score)
						student.save_to_disk("Phase_3")
						print("score updated")
						break
				else:
					print("student not found")

			case "4":
				name=input("Enter student name: ").strip().lower()
				session=int(input("Enter student attendance: ").strip())
				for student in roster.students:
					if student.name == name:
						student.log_attendance(session)
						student.save_to_disk("Phase_3")
						print("attendance updated")
						break
				else:
					print("student not found")


			case "5":
				name = input("Enter student name: ").strip().lower()
				for student in roster.students:
					if student.name == name:
						print(student)
						break
				else:
					print("student not found")

			case "6":
				name = input("Enter student name: ").strip().lower()
				student = Student.load_from_folder("Phase_3/" + name)
				if student:
					print(student)
				else:
					print("student not found")

			case "7":
				roster = Roster.load_all("Phase_3")
				print(f"{len(roster.students)} students loaded.")
			case "0":
				print(f"Exiting {title} menu. Thank you for using the program.")
				break
			case _:
				print("invalid input. please try again")

if __name__ == "__main__":
	Roster.create_from_data(student_list, "Phase_3")
	class_menu()