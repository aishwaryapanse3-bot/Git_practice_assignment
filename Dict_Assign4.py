"""school = {
    "student1": {
        "name": "Aishwarya",
        "marks": {"Math": 88, "Science": 92, "English": 85},
        "city": "Solapur"
    },
    "student2": {
        "name": "Isha",
        "marks": {"Math": 78, "Science": 81, "English": 74},
        "city": "Pune"
    }
}
print(school)

print("------------------------------------")

# sum of students marks or  total marks.


print("------------------------------------")

school["student3"] = {
    "name": "Neha",
    "marks": {"Math": 90, "Science": 85, "English": 88},
    "city": "Mumbai"
}
print(school["student3"])

print("------------------------------------")

school["student2"].pop("marks")
print(school["student2"])

print("------------------------------------")

print(school)"""



a, b = 5, 10
a, b = b, a
print(a, b)

word = "Python"
length = len(word)
print("Length of the word:", length)
