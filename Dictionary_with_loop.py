#Dictionary with loop

contacts = {
    "Friend1": {"number": 123445, "city": "Bwp"},
    "Friend2": {"number": 4234545, "city": "Lhr"},
    "Friend3": {"number": 87947, "city": "ISB"}
}

for name, detailes in contacts.items():
    print(name, "ka number: ", detailes["number"], "hai aur woh" , detailes["city"], "se hai." )


Garage = {
    "Toyota": {
        "Model": "LandCrusier", 
        "Color" : "White",
        "Number" : "P7"
        },
     "Nissan": {
         "Model":"NissanPetrol",
         "Color":"Black",
         "Number": 387
     },
     "LandRover" :{
         "Model" : "Defender",
         "Color" : "Grey",
         "Number": "D90"
     },
     "Landrover" : {
         "Model" : "RangerRover Autobiograpy",
         "Color" : "White",
         "Number" : "Y88"
     }
}     

for Cars, details in Garage.items():
    print(Cars, details["Model"], details["Color"], details["Number"])

# for prtinting keys of list (means toyota, nissan etc.) 

for x in Garage:
    print("Keys:", x)

# for printing specific item in list

for toyota, details in Garage.items():
    print(toyota, details["Model"])

for list, details in Garage.items():
    print("The color of my cars is: ", details["Color"])

# adding new list in dictionary

Garage["Suzuki"] = {
    "Model" : "Jimny",
    "Color" : "Mustard",
    "Number" : "BWp-4818"
}
# print(Garage)

# adding a item in each list
 
Garage["Toyota"] = {
    "Model": "LandCrusier", 
    "Color" : "White",
    "Number" : "P7",
    "Registration Year" : 2024 
    }

# changing color of toyota
Garage["Toyota"]["Color"]= "Black"

# changing color with .update

Garage["Toyota"].update({"color" : "White", "Number" : "P9"})

# adding a item in all list at once

for car, details in Garage.items():
    details["Regesteration Year"] = 2026

print(Garage)




