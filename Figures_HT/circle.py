class Circle:
    def __init__(self, r: int):
        self.r = r
        if r < 0:
            print('Negative number cannot be used')
            exit(0)
        else:
            self.r = r

    def perimetr_c(self):
        perimetr = 2 * 3.14 * self.r
        return perimetr

    def square_c(self):
        square = 3.14 * (self.r ** 2)
        return square
