from abc import ABC, abstractmethod


class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Color:

    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b


class Drawable(ABC):

    def __init__(self, color: Color, fill: Color):
        self.__color = color
        self.__fill = fill

    @abstractmethod
    def draw(self):
        pass


class Figure(ABC, Drawable):

    def __init__(self, center: Point2D, color: Color, fill: Color):
        Drawable.__init__(self, color, fill)
        self.center = center

    @abstractmethod
    def move(self, coordinates: tuple):
        pass

    @abstractmethod
    def get_location(self):
        pass


class Line(Drawable):

    def __init__(self, point1: Point2D, point2: Point2D, color: Color,
                 fill: Color):
        Drawable.__init__(self, color, fill)
        self.__p1 = point1
        self.__p2 = point2


class Ray(Line):

    def __init__(self, center: Point2D, point: Point2D, color: Color,
                 fill: Color):
        Line.__init__(self, center, point, color, fill)


class Segment(Ray):

    def __init__(self, point1: Point2D, point2: Point2D, color: Color,
                 fill: Color):
        Ray.__init__(self, point1, point2, color, fill)


class Rectangle(Figure):

    def __init__(self, center: Point2D, color: Color, fill: Color,
                 a: int, b=None):
        Figure.__init__(self, center, color, fill)
        self.a = a
        self.b = a if b is None else b


class Square(Rectangle):

    def __init__(self, center: Point2D, color: Color, fill: Color,
                 a: int):
        Rectangle.__init__(self, center, color, fill, a)


class Ellipse(Figure):

    def __init__(self, center: Point2D, color: Color, fill: Color,
                 radius1: int, radius2=None):
        Figure.__init__(self, center, color, fill)
        self.r1 = radius1
        self.r2 = radius1 if radius2 is None else radius2


class Circle(Ellipse):

    def __init__(self, center: Point2D, color: Color, fill: Color,
                 radius: int):
        Ellipse.__init__(self, center, color, fill, radius)


class Rhombus(Figure):

    def __init__(self, center: Point2D, color: Color, fill: Color,
                 diag_length1: int, diag_length2: int):
        Figure.__init__(self, center, color, fill)
        self.d1 = diag_length1
        self.d2 = diag_length2
