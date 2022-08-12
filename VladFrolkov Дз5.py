class Car:
    def __init__(self, year: int, color: str, type: str):
        self.year = year
        self.color = color
        self.type = type

    def start(self):
        return print('Car is started!')

    def turnoff(self):
        return print('Car is turned off!')

    def __str__(self):
        return f'Year: {self.year}, Color: {self.color}, Type: {self.type}.'

car1 = Car(16, 'yellow', 'BMW')
print(car1)
car1.start()
car1.turnoff()


