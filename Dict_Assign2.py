laptop = {
    "brand": "HP",
    "model": "Pavilion 15",
    "price": 60000,
    "RAM": "16GB"
}

print(laptop)

print("-----------------------------------------")

laptop["storage"] = "512GB SSD"
print(laptop)

print("-----------------------------------------")

laptop["price"] = 58000
print(laptop)

print("-----------------------------------------")

laptop.pop("RAM")
print(laptop)

print("-----------------------------------------")

print(laptop)