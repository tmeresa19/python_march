student = {
    "first_name":"Alex",
    "last_name": "Miller"
}

for items in student:
    print(student["last_name"])

print(student)
student["age"]=25

del student["last_name"]
student.pop("first_name")

for key in student:
    print(key, student[key])