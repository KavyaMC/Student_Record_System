import os
class_a = ['Amit', 'anisha ', 'KAVYA', 'pratham']
class_b = [' Pooja', 'Varsha', 'kavya', 'Rahul']
full_roll = {'Amit', ' Anisha ', 'KAVYA', 'Pratham', 'Pooja', 'Varsha', 'Shubham', 'Virat', 'Shiva'}
marks_matrix = [[88, 95, 52], [73, 61, 91], [67, 84, 78]]
student_ids = [2101, 2134, 2108, 2147, 2115, 2129, 2156, 2163, 2172]

# Part 2 — The Data Source
def read_students(file_name):
	students=[]

	try:
		with open(file_name, "r") as f:
			for line in f:
				parts=line.split()

				if len(parts) <3:
					continue

				data={}
				data["name"]=str(parts[0]).strip().title()
				data["score"]=int(parts[1])
				data["grade"]=str(parts[2]).strip().upper()
				students.append(data)

	except FileNotFoundError:
		print("students.txt not found")
	return students

# Part 3 — Score Analysis
def total_marks(students):
	total=0
	for student in students:
		total+=student["score"]
	return total

def average_marks(students):
	if len(students)==0:
		return 0
	return round(total_marks(students)/len(students),2)

def highest_marks(students):
	if len(students)==0:
		return 0

	highest_marks=students[0]["score"]
	for student in students:
		if student["score"] > highest_marks:
			highest_marks=student["score"]
	return highest_marks

def lowest_marks(students):
	if len(students)==0:
		return 0

	lowest_marks=students[0]["score"]
	for student in students:
		if student["score"] < lowest_marks:
			lowest_marks=student["score"]
	return lowest_marks

def above_average_students(students):
	average= average_marks(students)
	above_average=[]
	for student in students:
		if student["score"] > average:
			data={"name": student["name"], "score": student["score"]}
			above_average.append(data)
	return above_average

def count_range(students, low, high):
	count=0
	for student in students:
		if low <= student["score"] <= high:
			count+=1
	return count

# Part 4 — Reports
def class_report(students):
	return {
		"Total": total_marks(students),
		"Average": average_marks(students),
		"Highest": highest_marks(students),
		"Lowest": lowest_marks(students),
		"Above Average Count": len(above_average_students(students)),
		"Mid Range Count": count_range(students, 60, 89)
	}

def count_by_grade(students):
	student_grades={"A":  0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
	for grade in student_grades:
		count=0
		for student in students:
			if student["grade"] == grade:
				count+=1
		student_grades[grade] = count
	return student_grades

def top_grade(students):
	grade_count=count_by_grade(students)
	highest_grade=""
	highest_grade_count=0
	for key, value in grade_count.items():
		if value > highest_grade_count:
			highest_grade_count=value
			highest_grade=key
	return f"{highest_grade}: {highest_grade_count} students."

def write_report(filename, students):
	report=class_report(students)
	grade_count=count_by_grade(students)
	Top=top_grade(students)
	grade_parts=[]
	lines=[]

	lines.append("---SCORE SUMMARY---\n")
	for key, value in report.items():
		line=f"{key}: {value}\n"
		lines.append(line)

	lines.append("---GRADE BREAKDOWN---\n")
	for key, value in grade_count.items():
		grade_parts.append(f"{key}: {value}")
		grade_line=", ".join(grade_parts)
	lines.append(f"{grade_line}\n")

	lines.append("---TOP GRADE---\n")
	lines.append(f"{Top}\n")

	try:
		with open(filename, "w") as f:
			f.writelines(lines)
			return f"Report saved in {filename}"

	except OSError as e:
		return f"Error: Report couldn't be stored in {filename} because {e}"

# Part 5 — Sets
def shared_students(list_a, list_b):
	list_a=set(list_a)
	list_b=set(list_b)
	return {
		"in_both": list_a&list_b,
			"only_in_a": list_a-list_b
	}

def compare_classes(list_a, list_b):
	clean_a=set()
	clean_b=set()
	for source, target in [(list_a, clean_a), (list_b, clean_b)]:
		for name in source:
			name=name.strip().lower()
			target.add(name)
	return shared_students(list(clean_a), list(clean_b))

def find_absent_students(present, full_roll):
	result = compare_classes(full_roll, present)
	absent=result["only_in_a"]
	line=", ".join(absent)
	return f"absent students: {line}"

# Part 6 — Honour Roll and Logging
def passing_students(students):
	passing=[]
	for student in students:
		if student["grade"]=="F":
			continue
		passing.append(student)
	return passing

def honour_roll(students):
	passing=passing_students(students)
	average=average_marks(students)
	honour_roll=[]
	for student in passing:
		if student["score"] > average:
			name=student["name"].strip().title()
			honour_roll.append(name)
	return honour_roll

def log_honour_roll(filename, students):
	studentlist=honour_roll(students)
	line= ", ".join(studentlist)
	try:
		with open(filename, "a") as f:
			f.write(line+"\n")
		return "log updated"
	except OSError as e:
		return f"error: log not updated. {e}"

# Part 7 — Nested Lists and the break Keyword
def row_average(matrix):
	AverageList=[]
	for student in matrix:
		total=0
		for score in student:
			total+=score
		average=round(total/len(student),1)
		AverageList.append(average)
	return AverageList

def enforce_pass_threshold(matrix, threshold):
	averagelist=row_average(matrix)
	for index, average in enumerate(averagelist, start=1):
		if average < threshold:
			return f"Row {index} below threshold — stopping."
	else:
		return "All rows meet threshold."

# Part 8 — Updating Records
def update_student_file(filename, name, new_score):
	students=read_students(filename)

	for student in students:

		if student["name"].lower() == name.strip().lower():
			student["score"] = new_score

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
				with open(filename, "w") as f:
					for s in students:
						line= f"{s['name']} {s['marks']} {s['grade']}"
						f.write(line+"\n")
				return "student records changed successfully"

			except OSError as e:
				return f"error: file not updated: {e}"
	return "student record not found"

# Part 9 — The os Module — First Pass
def safe_delete(filename):
	if os.path.isfile(filename):
		os.remove(filename)
		return f"{filename} deleted."
	else:
		return f"{filename} not found."

def list_class_files(directory):
	original = os.getcwd()
	if not os.path.exists("records"):
		os.mkdir("records")
		files=["info.txt", "attendence.txt", "notes.txt", "old_backup.txt", "old_report.txt"]
		for name in files:
			path = os.path.join("records", name)
			with open(path, "w") as f:
				f.write("Sample content\n")

	try:
		os.chdir(directory)
		data = os.listdir()
		text_files = []

		for f in data:
			if os.path.isfile(f) and f.endswith(".txt"):
				if f.startswith("old_"):
					print(safe_delete(f))
				else:
					text_files.append(f)

	except FileNotFoundError:
		return "Directory not found."

	finally:
		os.chdir(original)
	return text_files

#Part 10 — While Loops and Input Validation
def search_by_id(student_ids, target_id):
	counter=0
	while counter < len(student_ids):
		if student_ids[counter]==target_id:
			return counter
		counter+=1
	return -1

def get_valid_integer(prompt, low, high):
	while True:
		try:
			num=int(input(prompt))
			if low <= num <= high:
				return num
			else:
				print(f"Value must be between {low} and {high}.")

		except ValueError:
			print("Invalid input, please try again.")

# Part 11 — The Report Card
def read_summary_lines(filename):
	report={}
	with open(filename, "r") as f:
		report["first_line"]=f.readline().strip()
		report["remaining_lines"]=f.readlines()
	return report

def print_report_card(student, students):
	data=read_summary_lines("report.txt")
	print(data["first_line"]+"\n")
	name=student["name"].strip().title()
	honour_names=honour_roll(students)
	if name in honour_names:
		status="HONOUR ROLL"
	else:
		status="STANDARD"
	print("-------------------------")
	print(f"Student: {name}")
	print(f"Score:   {student['marks']}")
	print(f"Grade:   {student['grade']}")
	print(f"Status:  {status}")
	print("-------------------------")

def celebrate_student(name, streak, score, grade):
	new_streak = streak + 1
	stars="*"*new_streak
	unit="day" if streak==1 else "days"
	opening="WELL DONE" if score>=75 else "KEEP GOING"
	name=name.strip().title()
	message=(
		f"{stars} {opening}, {name}! "
		f"Score: {score} | "
		f"Grade: {grade} | "
		f"Streak: {new_streak} {unit}."
	)
	return message

# Part 1 — The Interactive Menu
def class_menu():
	students=read_students("students.txt")
	while True:
		print("--Main Menu--")
		print(f"{len(students)} records were loaded")
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

				print(f"---CLASS REPORT---")
				for key, value in class_report(students).items():
					print(f"{key}: {value}")

				print(f"---GRADE SHEET---")
				for key, value in count_by_grade(students).items():
					print(f"{key}: {value}")

				print(f"---TOP GRADE---")
				print(top_grade(students)+"\n")

				print(write_report("report.txt", students))

			case "2":
				print(log_honour_roll("report.txt", students))
			case "3":
				data=input("Enter names (comma separated): ")
				present=data.split(",")
				print(find_absent_students(set(present), full_roll))

			case "4":
				name=input("Enter student name: ")
				new_score=int(input("Enter revised student marks: "))
				result = update_student_file("students.txt", name, new_score)
				print(result)
				students = read_students("students.txt")

			case "5":
				id_value = get_valid_integer(		"Enter student ID: ", 2000, 3000)
				position = search_by_id(student_ids, id_value)
				if position == -1:
					print("Student ID not found.")
				else:
					print(f"Student ID found at position {position}.")

			case "6":
				print(list_class_files("records"))
				print(safe_delete("old_report.txt"))
			case "7":
					name = input("Enter student name: ")
					for student in students:
						if student["name"].lower() == name.strip().lower():
							print_report_card(student, students)
							print(				celebrate_student(student["name"], 0, student["score"], student["grade"]))
							break
					else:
						print("Student not found.")
			case "0":
				print(enforce_pass_threshold(marks_matrix, 76.5))
				input("Press enter to continue")
				print("exiting program")
				break
			case _:
				print("invalid choice.")
