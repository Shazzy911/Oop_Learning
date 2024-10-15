class Vehicle:
    def __init__(self,brand, model):
        self._brand = brand
        self._model = model

    def display_info(self):
        print(f"Brand:{self._brand} Model:{self.__model}")

class Car(Vehicle):
    def __init__(self, brand, model, year):
        # super().__init__(brand,model)
        super().__init__(brand, model)
        self.year = year

    def display_info(self):
        print(f"Brand:{self._brand} Model:{self._model} Year:{self.year}")



data = Car("bmw", "ferrari", 2024)

data.display_info()