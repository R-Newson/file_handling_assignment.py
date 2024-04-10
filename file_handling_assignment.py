# File Reading and Calculation
try:
    with open("student_grades.csv", "r") as csv_file:
        lines = csv_file.readlines()
        header, *data = [line.strip().split(",") for line in lines]

        # Calculate average grades
        averages = {}
        for row in data:
            name, math, science, english = row
            total_score = int(math) + int(science) + int(english)
            average_score = total_score / 3
            averages[name] = average_score

except FileNotFoundError:
    print("Error: File 'student_grades.csv' not found.")
except PermissionError:
    print("Error: Permission denied.")

# File Writing
try:
    with open("average_grades.txt", "w") as txt_file:
        txt_file.write("Student Name\tAverage Grade\n")
        for name, avg in averages.items():
            txt_file.write(f"{name}\t\t{avg:.2f}\n")

except FileNotFoundError:
    print("Error: File 'average_grades.txt' not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File writing completed.")
