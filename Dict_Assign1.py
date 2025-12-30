student = {
    "name": "Aishwarya",
    "age": 22,
    "course": "Computer Science",
    "city": "Solapur"
}

print(student)

#Each key value pair 

print ("-----------------------------------")

student["grade"] = "A"
print(student)

print ("-----------------------------------")

student["city"] = "Pune"
print(student)

print ("-----------------------------------")

student.pop("age")
print(student)