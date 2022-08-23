class Rectangle:
    def __init__(self, side_list: list[int]):
        self.side_list = side_list
        for _ in side_list:
            if _ < 0:
                print('Negative number cannot be used')
                exit(0)
            else:
                self.side_list = side_list

    def perimetr_rec(self):
        perimetr = 2 * (self.side_list[0] + self.side_list[1])
        return perimetr

    def square_rec(self):
        square = self.side_list[0] * self.side_list[1]
        return square

