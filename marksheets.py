
def calculate_marksheet(subject_marks):
    total_marks = sum(subject_marks)
    average_marks = total_marks / len(subject_marks)

    if average_marks >= 90:
        grade = 'A'
    elif average_marks >= 80:
        grade = 'B'
    elif average_marks >= 70:
        grade = 'C'
    elif average_marks >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return total_marks, average_marks, grade

subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))
subject5 = float(input("Enter marks for subject 5: "))

marks = [subject1, subject2, subject3, subject4, subject5]

total, average, grade = calculate_marksheet(marks)

print("\n------- Marksheet -------")
print("Subject 1:", subject1)
print("Subject 2:", subject2)
print("Subject 3:", subject3)
print("Subject 4:", subject4)
print("Subject 5:", subject5)
print("-------------------------")
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
