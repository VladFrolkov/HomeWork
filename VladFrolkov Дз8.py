from dataclasses import dataclass

@dataclass
class User:
    age: int
    country: str
    name: str
    surname: str
    gender: str
    __profession: str
    birth_year: str = None
    email: str = None

    def email_add(self):
        self.email = f'{self.name}{self.surname}{self.age}@mail.com'
        return self.email

    def birth_day_set(self):
        self.birth_year = f'2022 - {self.age}'
        return self.birth_year

    @staticmethod
    def doctor():
        doctor = User(23, 'Bel', 'Bill', 'Gilbert', 'M', 'doctor')
        return doctor

    @staticmethod
    def police_officer():
        police_officer = User(23, 'Bel', 'Bill', 'Gilbert', 'M', 'police_officer')
        return police_officer

    @staticmethod
    def teacher():
        teacher = User(23, 'Bel', 'Bill', 'Gilbert', 'M', 'teacher')
        return teacher


person_1 = User(20, 'Bel', 'Bill', 'Gilbert', 'M', 'cooker')
print(person_1)


