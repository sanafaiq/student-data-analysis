import csv

# Open the CSV file
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    total_students = 0
    total_marks = 0
    highest_avg = 0
    lowest_avg = 100
    top_student = ""
    low_student = ""

    print("Student Results:\n")

    for row in reader:
        name = row["Name"]
        math = int(row["Math"])
        science = int(row["Science"])
        english = int(row["English"])

        average = (math + science + english) / 3
        total_students += 1
        total_marks += average

        if average >= 50:
            result = "Pass"
        else:
            result = "Fail"

        print(f"{name} - Average: {average:.2f} - {result}")

        if average > highest_avg:
            highest_avg = average
            top_student = name

        if average < lowest_avg:
            lowest_avg = average
            low_student = name


    class_average = total_marks / total_students

    print("\n--- Summary ---")
    print(f"Class Average: {class_average:.2f}")
    print(f"Top Student: {top_student} ({highest_avg:.2f})")
    print(f"Lowest Student: {low_student} ({lowest_avg:.2f})")

