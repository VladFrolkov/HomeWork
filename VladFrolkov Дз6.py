class Triangle:
    def __init__(self, sides: list[int or float]):
        for side in sides:
            if isinstance(side, int or float):
                self.sides = sides
            else:
                print('input correct value (int or float).')
                exit(0)

    def is_possible(self):
        if sorted(self.sides)[0] + sorted(self.sides)[1] > sorted(self.sides)[2]:
            print('triangle is possible')
        else:
            print('Triangle is impossible')

    def __str__(self):
        return f"{self.sides}"


sides_1 = [3, 10, 12]
sides_2 = [10, 3, 5]

tri_1 = Triangle(sides_1)
tri_2 = Triangle(sides_2)

tri_1.is_possible()
tri_2.is_possible()

