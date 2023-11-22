# class Person:
#     def __init__(self, name: str, surname: str) -> None:
#         self._name = name
#         self.__surname = surname

#     def get_name(self) ->str:
#         return


# person = Person(name="Povilas", surname="Tarai")
# print(person.name)
# print(person.surname)
# person.surname = "Kleckas"
# print(person.surname)


# class Vehicle:
#     def mean_of_transport(self) -> str:
#         return "This is vehicle"


# class Car(Vehicle):
#     def __init__(self, brand: str) -> None:
#         self.brand = brand

#     def get_brand(self) -> str:
#         return self.brand


# class Plane(Vehicle):
#     def __init__(self, price: int) -> None:
#         self.price = price

#     def get_price(self) -> int:
#         return self.price


# car = Car(brand="BMW")
# print(car.get_brand())
# print(car.mean_of_transport())

# plane = Plane(price=45544545)
# print(plane.mean_of_transport())


# class Employee:
#     def __init__(self, name: str, surname: str, age: int):
#         self.name = name
#         self.surname = surname
#         self.age = age

#     def get_employees_info(self) -> str:
#         return f"{self.name} {self.surname} is {self.age} years old"


# class Engineers(Employee):
#     def __init__(self, position: str, name: str, surname: str, age: int):
#         super().__init__(name=name, surname=surname, age=age)
#         self.position = position

#     def get_engineer_position(self) -> str:
#         return self.position


# engineers = Engineers(
#     position="Senior Developer", name="Mindaugas", surname="Rudzevicius", age=32
# )
# print(engineers.get_employees_info())


# class Car:
#     def __init__(self, model: str, price: int, year: int) -> None:
#         self.model = model
#         self.price = price
#         self.year = year

#     def get_car_info(self) -> str:
#         return f"{self.model} year is {self.year}, price is {self.price}"


# class BMW(Car):
#     def __init__(self, fuel: str, model: str, price: int, year: int):
#         super().__init__(model=model, price=price, year=year)
#         self.fuel = fuel

#     def get_car_fuel(self) -> str:
#         return self.fuel


# bmw_car = BMW(model="BMW sedan", price=20000, year=2022, fuel="diesel")
# print(bmw_car.get_car_info())


# class Shoes:
#     def __init__(self, shoe_type: str, shoe_size: float, price: int) -> None:
#         self.type = shoe_type
#         self.shoe_size = shoe_size
#         self.price = price

#     def get_shoes_info(self) -> str:
#         return f"{self.type} shoe size is {self.shoe_size}, price is {self.price}"


# class Nike(Shoes):
#     def __init__(self, discount: str, shoe_type: str, shoe_size: float, price: int):
#         super().__init__(shoe_type=shoe_type, shoe_size=shoe_size, price=price)
#         self.discount = discount

#     def get_shoe_discount(self) -> str:
#         return self.discount


# nike_shoe = Nike(
#     shoe_type="Nike Air Force", price=200, shoe_size=42.5, discount="20 Percent"
# )
# print(nike_shoe.get_shoes_info())
# print(f"Discount is: {nike_shoe.get_shoe_discount()}")





# Task Nr1

# Create a base class called Book with attributes like title, author, and publication_year. 
# This class should have a method called display_info that prints basic information about the book.

# Create two subclasses of Book called Fiction and NonFiction. Add an additional attribute to each 
# subclass, such as genre for Fiction and subject for NonFiction.

# Create two more subclasses, Mystery and History, that inherit from Fiction and NonFiction, 
# respectively. Add specific attributes to each of these subclasses (e.g., detective for Mystery and time_period for History).

# Add in each sub class methods to retreive provided data.


class Book:

    def __init__(self,title:str,author:str,publication_year:int) -> None:
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info


