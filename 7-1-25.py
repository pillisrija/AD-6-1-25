students = {
    1: {"name": "google", "age": 20},
    2: {"name": "Dell", "age": 21},
    3: {"name": "pwc", "age": 22},
    4: {"name": "eee", "age": 23}
}
for student_id,details in students.items():
    print(f"StudentID: {student_id}, Name: {details['name']}, Age: {details['age']}")