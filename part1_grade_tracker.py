print()
print()
print()
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
    print("================================")

# Step 7: find roll number 103 and print name in uppercase and lowercase
for student in cleaned_students:
    if student["roll"] == 103:
        print(student["name"].upper())
        print(student["name"].lower())


# clean the student data.
# fix name, roll number and marks.
# check if name is valid.
# print student details.

print("========================================")

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


# print subject, marks and grade.
# find total and average marks.
# find highest and lowest subject.
# add new subjects using while loop.

print("========================================")

# Task 3
# class report

print()
print()
print()
print("TASK 3 - Class Performance Summary")
print()

class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma", [55, 68, 49, 72, 61]),
    ("Priya Nair", [91, 85, 88, 94, 79]),
    ("Karan Mehta", [40, 55, 38, 62, 50]),
    ("Sneha Pillai", [75, 80, 70, 68, 85])
]

print("Name | Average | Status")
print("------------------------")
print("------------------------")

pass_count = 0
fail_count = 0

top_name = ""
top_average = 0

sum_of_averages = 0

for item in class_data:
    name = item[0]
    marks = item[1]

    total = 0
    for m in marks:
        total = total + m

    average = total / len(marks)
    average = round(average, 2)

    if average >= 60:
        status = "Pass"
        pass_count = pass_count + 1
    else:
        status = "Fail"
        fail_count = fail_count + 1

    print(name, "|", average, "|", status)

    sum_of_averages = sum_of_averages + average

    if average > top_average:
        top_average = average
        top_name = name

class_avg = sum_of_averages / len(class_data)
class_avg = round(class_avg, 2)

print()
print("Passed:", pass_count)
print("Failed:", fail_count)
print("Topper:", top_name, "-", top_average)
print("Class average:", class_avg)

# find average and pass/fail.
# print class report.
# find pass count, fail count, topper and class average.

print("========================================")

# Task 4
# string operations on essay

print()
print()
print("TASK 4 - String Manipulation Utility")
print()

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# step 1
clean_essay = essay.strip()
print("Step 1:")
print(clean_essay)
print()

print("____________________________________________________________________________________________________________________________________________________________________________")
# step 2
print("Step 2:")
print(clean_essay.title())
print()

print("____________________________________________________________________________________________________________________________________________________________________________")
# step 3
count_python = clean_essay.count("python")
print("Step 3:")
print(count_python)
print()

print("____________________________________________________________________________________________________________________________________________________________________________")
# step 4
changed_essay = clean_essay.replace("python", "Python 🐍")
print("Step 4:")
print(changed_essay)
print()

print("____________________________________________________________________________________________________________________________________________________________________________")
# step 5
sentence_list = clean_essay.split(". ")
print("Step 5:")
print(sentence_list)
print()

print("____________________________________________________________________________________________________________________________________________________________________________")
# step 6
print("Step 6:")
num = 1

for sentence in sentence_list:
    if sentence.endswith(".") == False:
        sentence = sentence + "."
    print(str(num) + ".", sentence)
    num = num + 1

 
# string work on essay
# clean text and print each step
print("========================================")