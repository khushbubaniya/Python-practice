# creating a dictionary.............

student = {
    "name":"John",
    "age" :15,
    "grade":"A+"
}
print (student)

# acessing values from above 
print ("Student name:",student["name"])
print ("student age:",student["age"])

# deleting key value pairs
student = {"employee_name":'krit','depart':'marketing','age':24,'adress':'rupandehi'}
del student['adress']
print (student)

# checking if a key exists from above quetion...........

if "depart" in student:
    print ('department key exists')
    
else:
    print ('department is not exists')
    
    
# merging dictionaries

dict1 = {"a": 5, "b": 8}
dict2 = {"c": 11, "d": 14}
 
merged_dict = {**dict1, **dict2}
 
print(merged_dict)

# Summing Values

expenses = {"food": 100, "rent": 5000, "transport": 120, "entertainment": 60}
 
total_expenses = sum(expenses.values())
print("Total expenses:", total_expenses)

# Nested Dictionaries

student_records = {
    10: {"name": "hari", "age": 21, "grade": "A"},
    12: {"name": "ram", "age": 18, "grade": "B"},
    13: {"name": "Chaitanya", "age": 19, "grade": "A"},
}
print(student_records)
