employees = {
    "emp1": {"name": "Rahul", "department": "HR", "salary": 40000},
    "emp2": {"name": "Sneha", "department": "IT", "salary": 50000},
    "emp3": {"name": "Aman", "department": "Finance", "salary": 45000}
}

print(employees)

print("----------------------------------------")

# another method for this 

print(employees["emp1"]["name"],  employees["emp1"]["department"])
print(employees["emp2"]["name"],  employees["emp2"]["department"])
print(employees["emp3"]["name"],  employees["emp3"]["department"])

print("----------------------------------------")

employees["emp2"]["salary"] = 60000
print(employees)

print("----------------------------------------")

employees["emp1"]["experience"] = 3
employees["emp2"]["experience"] = 5
employees["emp3"]["experience"] = 2

print(employees)

print("----------------------------------------")

employees.pop("emp3")
print(employees)

print("----------------------------------------")

