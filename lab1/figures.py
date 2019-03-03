from abc import ABC, abstractmethod
from tkinter import Canvas


class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Drawable(ABC):

    def __init__(self, color: str, fill: str, width: int):
        self.color = color
        self.fill = fill
        self.width = width

    @abstractmethod
    def draw(self, canvas: Canvas):
        pass


class Movable(ABC):

    @abstractmethod
    def move(self, coordinates: tuple, canvas: Canvas):
        pass

    @abstractmethod
    def get_location(self, canvas: Canvas):
        pass


class Figure(Drawable, Movable):

    def __init__(self, center: Point2D, color: str, fill: str, width: int):
        Drawable.__init__(self, color, fill, width)
        self.center = center

    def move(self, coordinates: tuple, canvas: Canvas):
        self.center = Point2D(coordinates[0], coordinates[1])

    def get_location(self, canvas: Canvas):
        return self.center


class Line(Drawable):

    def __init__(self, point1: Point2D, point2: Point2D, color: str, fill: str, width: int):
        Drawable.__init__(self, color, fill, width)
        self.__p1 = point1
        self.__p2 = point2


class Ray(Line):

    def __init__(self, center: Point2D, point: Point2D, color: str, fill: str, width: int):
        Line.__init__(self, center, point, color, fill, width)


class Segment(Ray):

    def __init__(self, point1: Point2D, point2: Point2D, color: str, fill: str, width: int):
        Ray.__init__(self, point1, point2, color, fill, width)

    def draw(self, canvas: Canvas):
        canvas.create_line(self.__p1.x, self.__p1.y,
                           self.__p2.x, self.__p2.y,
                           fill=self.fill, outline=self.color, width=self.width)


class Rectangle(Figure):

    def __init__(self, center: Point2D, color: str, fill: str, width: int,
                 a: int, b=None):
        Figure.__init__(self, center, color, fill, width)
        self.a = a
        self.b = a if b is None else b

    def draw(self, canvas: Canvas):
        x1 = self.center.x - self.a // 2
        y1 = self.center.y - self.b // 2
        x2 = self.center.x + self.a // 2
        y2 = self.center.y + self.b // 2
        canvas.create_rectangle(x1, y1, x2, y2, fill=self.fill, outline=self.color, width=self.width)


class Square(Rectangle):

    def __init__(self, center: Point2D, color: str, fill: str, width: int,
                 a: int):
        Rectangle.__init__(self, center, color, fill, width, a)


class Ellipse(Rectangle):

    def __init__(self, center: Point2D, color: str, fill: str, width: int,
                 a: int, b=None):
        Rectangle.__init__(self, center, color, fill, width, a, b)

    def draw(self, canvas: Canvas):
        x1 = self.center.x - self.a // 2
        y1 = self.center.y - self.b // 2
        x2 = self.center.x + self.a // 2
        y2 = self.center.y + self.b // 2
        canvas.create_oval(x1, y1, x2, y2, fill=self.fill, outline=self.color, width=self.width)


class Circle(Ellipse):

    def __init__(self, center: Point2D, color: str, fill: str, width: int,
                 radius: int):
        Ellipse.__init__(self, center, color, fill, width, radius)


class Rhombus(Figure):

    def __init__(self, center: Point2D, color: str, fill: str, width: int,
                 diag_length1: int, diag_length2: int):
        Figure.__init__(self, center, color, fill, width)
        self.d1 = diag_length1
        self.d2 = diag_length2
