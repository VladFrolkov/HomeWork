class User:
    def __init__(self, age: int, country, name, surname, gender, _profession: str):
        self.age = age
        self.country = country
        self.name = name
        self.surname = surname
        self.gender = gender
        self._profession = _profession
        self.birth_year = 2022 - self.age
        self.email = f'{self.name}{self.surname}{self.age}@gmail.com'

    def doctor(self):
        self._profession = 'doctor'

    def police_officer(self):
        self._profession = 'police_officer'

    def teacher(self):
        self._profession = 'teacher'

    def __str__(self):
        return f'{self.name, self.surname, self.age, self.country, self.gender, self._profession}'


person_1 = User(20, 'Bel', 'Bill', 'Gilbert', 'M', 'cooker')
print(person_1)
person_1.doctor()
print(person_1)
