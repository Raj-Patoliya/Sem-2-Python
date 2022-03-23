cars = ["Toyota", "Hyundai", "Maruti", "Tesla", "Tata", "Honda"]
cars = list(map(lambda x : x.replace("Maruti","Mahindra"),cars))
print(cars)
