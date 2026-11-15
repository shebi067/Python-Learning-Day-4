Student = {                     # Dictionary
    "Name" : "Ali",
    "Age" : 21,
    "Roll No" : 1182,    
}

print(Student ["Name"])
Student["Profession"] = "Dev"

Student ["Age"] = 23
print(Student)

del Student ["Profession"]
print(Student)

print(Student.keys())
print(Student.values())

print(Student.get("Color"))

    #task1
car = {
        "Brand" : "Toyota",
        "Model": "Land Crusier",
        "Year" : 2025
    }

car ["Color"] = "White"
car ["Model"] = "Fortuner"

print(car)

# task 2

contacts = {
    "Friend1" : {
       "number" : 123445,
        "city" : "Bwp"
    },
    "Friend2" : {
           "number" : 4234545,
            "city" : "Lhr"
        }
}

print(contacts["Friend1"]["number"])

contacts["Friend3"] = {"number" : 87947, "city": "ISB"}
print(contacts)

