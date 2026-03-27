print("TASK 1 - Data Parsing & Profile Cleaning")
print()


raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA", "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ", "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:

    # Step 1: clean the name
    name = student["name"].strip().title()

    # Step 2: change roll number into integer
    roll = int(student["roll"])

    # Step 3: split marks and convert into integer list
    marks_text = student["marks_str"].split(", ")
    marks = []

    for mark in marks_text:
        marks.append(int(mark))

    # Step 4: check if name is valid
    words = name.split()
    valid_name = True

    for word in words:
        if word.isalpha() == False:
            valid_name = False

    # Step 5: save cleaned student data
    new_student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    cleaned_students.append(new_student)

    # Step 6: print profile card
    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")

    if valid_name == True:
        print("✓ Valid name")
    else:
        print("✗ Invalid name")

    print("================================")

# Step 7: find roll number 103 and print name in uppercase and lowercase
for student in cleaned_students:
    if student["roll"] == 103:
        print(student["name"].upper())
        print(student["name"].lower())

# Task 1
# clean the student data
# fix name, roll number and marks
# check if name is valid
# print student details

print()
print()
print()
print("TASK 2 - Marks Analysis Using Loops and Conditionals")
print()


student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("Student Name:", student_name)
print()

# print subject, marks and grade
for i in range(5):
    print("Subject:", subjects[i])
    print("Marks:", marks[i])

    if marks[i] >= 90:
        print("Grade: A+")
    elif marks[i] >= 80:
        print("Grade: A")
    elif marks[i] >= 70:
        print("Grade: B")
    elif marks[i] >= 60:
        print("Grade: C")
    else:
        print("Grade: F")

    print()

# total marks
total = 0
for m in marks:
    total = total + m

print("Total marks:", total)

# average marks
average = total / len(marks)
print("Average marks:", round(average, 2))
print()

# highest subject
high_marks = marks[0]
high_subject = subjects[0]

for i in range(5):
    if marks[i] > high_marks:
        high_marks = marks[i]
        high_subject = subjects[i]

print("Highest scoring subject:", high_subject, "-", high_marks)

# lowest subject
low_marks = marks[0]
low_subject = subjects[0]

for i in range(5):
    if marks[i] < low_marks:
        low_marks = marks[i]
        low_subject = subjects[i]

print("Lowest scoring subject:", low_subject, "-", low_marks)
print()

# adding new subjects
count = 0

while True:
    subject = input("Enter subject name: ")

    if subject == "done":
        break

    mark = input("Enter marks: ")

    if mark.isdigit():
        mark = int(mark)

        if mark >= 0 and mark <= 100:
            subjects.append(subject)
            marks.append(mark)
            count = count + 1
            print("Added")
        else:
            print("Marks should be between 0 and 100")
    else:
        print("Invalid input")

    print()

# updated average
new_total = 0
for m in marks:
    new_total = new_total + m

new_average = new_total / len(marks)

print("New subjects added:", count)
print("Updated average:", round(new_average, 2))

# Task 2
# print subject, marks and grade
# find total and average marks
# find highest and lowest subject
# add new subjects using while loop