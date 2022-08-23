import math


class Triangle:
    def __init__(self, side_list: list[int]):
        self.side_list = side_list
        for _ in side_list:
            if sorted(self.side_list)[0] + sorted(self.side_list)[1] < sorted(self.side_list)[2]:
                print('Triangle cannot exist')
                exit(0)
            elif _ < 0:
                print('Negative number cannot be used')
                exit(0)
            else:
                self.side_list = side_list

    def perimetr_tr(self):
        perimetr = self.side_list[0] + self.side_list[1] + self.side_list[2]
        return perimetr

    def square_tr(self):
        p = (self.side_list[0] + self.side_list[1] + self.side_list[2])/2
        square = math.sqrt(p*(p - self.side_list[0])*(p - self.side_list[1])*(p - self.side_list[2]))
        return square



