class Vehicle:
    def __init__(self, kind: str, year: int):
        self.year = year
        self.kind = kind

    def __str__(self):
        return f"Класс: {self.kind} \nГод: {self.year}."

    def __repr__(self):
        return f'{self.kind, self.year}'

    @classmethod
    def move(cls):
        return print('Vehicle is moving!')


class Auto(Vehicle):
    def __init__(self, kind: str, year: int, color: str, number_of_seats: int):
        Vehicle.__init__(self, kind, year)
        self.color = color
        self.number_of_seats = number_of_seats

    def __str__(self):
        return f"Класс: {self.kind} \nГод: {self.year} \nЦвет: {self.color} \nКоличество мест: {self.number_of_seats}."

    def __repr__(self):
        return f'{self.kind, self.year, self.color, self.number_of_seats}'

    @staticmethod
    def start():
        return print('Car is started!')

    @staticmethod
    def finish():
        return print('Car is finished!')


class Truck(Vehicle):
    def __init__(self, kind: str, year: int, transported_volume: float):
        Vehicle.__init__(self, kind, year)
        self.transported_volume = transported_volume

    def __str__(self):
        return f"Класс: {self.kind} \nГод: {self.year} \nПеревозимый объем: {self.transported_volume}."

    @staticmethod
    def unload_cargo():
        print('Груз выгружен!')


class Tipper(Truck):

    def __init__(self, kind: str, year: int, transported_volume: float, cost_hour: float):
        Truck.__init__(self, kind, year, transported_volume)
        self.cost_hour = cost_hour

    def __str__(self):
        return f"Год: {self.year} \nПеревозимый объем: {self.transported_volume} \nСтоимость в час: {self.cost_hour}."

    @staticmethod
    def buy_on_day():
        print('Забронирован на день!')

    def __repr__(self):
        return f'{self.kind, self.year, self.transported_volume, self.cost_hour}'


class Ship:
    def __init__(self, length: float, speed_hour: float):
        self.length = length
        self.speed_hour = speed_hour

    def __str__(self):
        return f'Длина: {self.length} \nСкорость: {self.speed_hour}'


class Boat(Ship, Vehicle):
    def __init__(self, length, speed_hour, year, kind, motor_volume):
        Vehicle.__init__(self, kind, year)
        Ship.__init__(self, length, speed_hour)
        self.motor_volune = motor_volume

    def __str__(self):
        return f'Кл:{self.kind} \nГ:{self.year} \nДл:{self.length} \nV/h:{self.speed_hour} \nV_mot{self.motor_volune}'

    @staticmethod
    def launch():
        print('Катер спущен на воду!')

    @staticmethod
    def honk():
        print('Тууу-тууууууу!')

print('---------')
vehicle_1 = Vehicle('automobile', 5)
print(vehicle_1)
vehicle_1.move()
print('---------')
Auto_1 = Auto('automobile', 4, 'yellow', 5)
print(Auto_1)
Auto_1.finish()
Auto_1.start()
Auto_1.move()
print('---------')
truck_1 = Truck('Truck', 12, 200)
print(truck_1)
truck_1.move()
truck_1.unload_cargo()
print('---------')
tipper_1 = Tipper('Tipper', 13, 300, 6000)
print(tipper_1)
tipper_1.buy_on_day()
print('---------')
ship_1 = Ship(100, 90)
print(ship_1)
print('---------')
boat_1 = Boat(3, 70, 2, 'boat', 4)
print(boat_1)
boat_1.honk()
boat_1.launch()
print('---------')









