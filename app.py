# score = int(input("Enter your score: "))
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

# grades = {}

# while True:
#     action = input("Choose an action - Add, Update, Print, or Exit: ").lower()
#     if action == "add":
#         name = input("Enter student name: ")
#         grade = input("Enter grade: ")
#         grades[name] = grade
#     elif action == "update":
#         name = input("Enter student name to update: ")
#         if name in grades:
#             grade = input("Enter new grade: ")
#             grades[name] = grade
#         else:
#             print("Student not found.")
#     elif action == "print":
#         for student, grade in grades.items():
#             print(f"{student}: {grade}")
#     elif action == "exit":
#         break


# with open("output.txt", "w") as file:
#     file.write("Hello, this is a test.\nThis content is written to a file.")

with open("output.txt", "r") as file:
    content = file.read()
    print(content)
