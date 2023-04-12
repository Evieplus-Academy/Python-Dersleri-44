student1 = ("Ali", "Demir", 85)
student2 = ("Mehmet", "Yılmaz", 85)
student3 = ("Ayşe", "Kara", 100)

classroom = [student1, student2, student3]

student_count = len(classroom)

grades = set()
for student in classroom:
    grades.add(student[2])

student_information = {}
for student in classroom:
    name_surname = f"{student[0]} {student[1]}"
    student_information[name_surname] = student[2]

print("Öğrenci listesi")
for student in classroom:
    print(f"{student[0]} {student[1]} - notu: {student[2]}")

print("Sınıfın aldığı notlar")
print(grades)

print("Öğrenci bilgileri")
for name_surname, grade in student_information.items():
    print(f"{name_surname} - notu: {grade}")

print(f"Sınıfımız mevcudu {student_count} öğrencidir.")
