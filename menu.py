import os
class_a = ['Amit', 'anisha ', 'KAVYA', 'pratham']
class_b = [' Pooja', 'Varsha', 'kavya', 'Rahul']
full_roll = {'Amit', ' Anisha ', 'KAVYA', 'Pratham', 'Pooja', 'Varsha', 'Shubham', 'Virat', 'Shiva'}



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
				data["marks"]=int(parts[1])
				data["grade"]=str(parts[2]).strip().upper()
				students.append(data)

	except FileNotFoundError:
		print("students.txt not found")
	return students

# Part 3 — Score Analysis
def total_marks(students):
	total=0
	for student in students:
		total+=student["marks"]
	return total

def average_marks(students):
	return round(total_marks(students)/len(students),2)

def highest_marks(students):
	highest_marks=students[0]["marks"]
	for student in students:
		if student["marks"] > highest_marks:
			highest_marks=student["marks"]
	return highest_marks

def lowest_marks(students):
	lowest_marks=students[0]["marks"]
	for student in students:
		if student["marks"] < lowest_marks:
			lowest_marks=student["marks"]
	return lowest_marks

def above_average_students(students):
	average= average_marks(students)
	above_average=[]
	for student in students:
		if student["marks"] > average:
			data={"name": student["name"], "marks": student["marks"]}
			above_average.append(data)
	return above_average

def count_range(students, low, high):
	count=0
	for student in students:
		if low <= student["marks"] <= high:
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
	for student in students:
		if student["marks"] > average:
			name=student["name"].strip().capitalize()
			honour_roll.append(name)
	return honour_roll

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
				print("in development")
			case "3":
				data=input("Enter names (comma separated): ")
				present=data.split(",")
				print(find_absent_students(set(present), full_roll))

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