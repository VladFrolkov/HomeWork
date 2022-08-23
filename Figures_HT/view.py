from circle import Circle
from rectangle import Rectangle
from triangle import Triangle

rectangle_1 = Rectangle([2, 3])
circle_1 = Circle(3)
triangle_1 = Triangle([4, 3, 5])


def rectangle_dict():
    return {'Rectangle': {'square': rectangle_1.square_rec(), 'perimetr': rectangle_1.perimetr_rec()}}


def triangle_dict():
    return {'Triangle': {'square': triangle_1.square_tr(), 'perimetr': triangle_1.perimetr_tr()}}


def circle_dict():
    return {'Circle': {'square': circle_1.square_c(), 'perimetr': circle_1.perimetr_c()}}


print(rectangle_dict())
print(triangle_dict())
print(circle_dict())





