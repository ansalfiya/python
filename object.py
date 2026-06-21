# Define a class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print("Car Details:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)


# Create an object (instance of the class)
car1 = Car("Toyota", "Corolla", 2020)

# Print using method
car1.display_info()

# You can also print directly attributes
print("\nDirect Access:")
print(car1.brand)
print(car1.model)
print(car1.year)