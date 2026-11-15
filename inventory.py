# Store inventory management task with help of dictionaries

inventory = {
        "Laptops": {
                "HP": {
                    "Model": "EliteBook",
                    "Color": "Silver",
                    "Price": 76000,
                    "Stock": 21,
                    "Category":"Electronics"
                    },
                    "Dell": {
                        "Model": "Latitude 7390",
                        "Color": "Black",
                        "Price": 98000,
                        "Stock": 24,
                        "Category":"Electronics"
                    }
            },
            "Mobile": {
                "Apple": {
                    "Model": "Iphone 18",
                    "Color": "Blue",
                    "Price": 129000,
                    "Stock": 23,
                    "Category":"Electronics"
                },
            "Google Pixel": {
                "Model": "Google Pixel 10xl",
                "Color": "White",
                "Price": 150000,
                "Stock": 43,
                "Category":"Electronics"
                }
            },
            "Airpods": {
                "Samsung": {
                    "Model": "Samsung Buds 2 pro",
                    "Color": "Black",
                    "Price": 25000,
                    "Stock": 29,
                    "Category":"Electronics"
                    },
                    "Apple": {
                        "Model": "Apple Airpods Pro Gen 3",
                        "Color": "White",
                        "Price": 30000,
                        "Stock": 98,
                        "Category":"Electronics"
                        },
                    "Xiaomi": {
                        "Model": "Xiaomi buds 8 pro",
                        "Color": "Grey",
                        "Price": 12000,
                        "Stock": 34,
                        "Category":"Electronics"
                        }
                },
                "Gaming PC": {
                    "Corsair": {
                    "Model": "Corsair hydra gen 4",
                    "Ram": "16 GB",
                    "Storage": "2TB Samsung SSD",
                    "GPU": "Nvidia RTX 4090Ti",
                    "Processor": "Intel i13 Gen 12",
                    "Stock": 9,
                    "Category":"Electronics",
                    "Price" : 240000
                    },
                    "RazerBlade": {
                        "Model": "Razerblade gen 8",
                        "Ram": "32 GB",
                        "Storage": "4TB Samsung SSD",
                        "GPU": "Nvidia RTX 5090Ti",
                        "Processor": "Intel i10 Gen 12",
                        "Stock": 12,
                        "Category":"Electronics",
                        "Price" : 200000
                          },
                 },
    }


for category, brands in inventory.items():
    for brand, details in brands.items():
        print(brand, "Catgory:",  details["Category"], "Price:",  details["Price"], "Stock:",  details["Stock"])



for color, brands in inventory.items():
    for brand, details in brands.items():
        print(brand, "Name", details["Model"], "      Price", details["Price"])


for color, model in inventory.items():
    for models, details in model.items():
        print(models,"                             Price", details["Price"])