from abc import ABC, abstractmethod
from tkinter import Canvas
from math import copysign as copysign_f
import numpy as np


def copysign(x, y) -> int:
    return int(copysign_f(x, y))


class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def mid_point(p1, p2):
        return Point2D(min(p1.x, p2.x) + int(abs(p1.x - p2.x) / 2),
                       min(p1.y, p2.y) + int(abs(p1.y - p2.y) / 2))

    @staticmethod
    def distance(p1, p2):
        return int((abs(p1.x - p2.x) ** 2 + abs(p1.y - p2.y) ** 2) ** 0.5)

    @staticmethod
    def offset(p1, p2):
        return p2.x - p1.x, p2.y - p1.y


class Figure(ABC):

    def __init__(self, color: str, fill: str, width: int, p1: Point2D, p2: Point2D):
        self.center = Point2D.mid_point(p1, p2)
        self.color = color
        self.fill = fill
        self.width = width
        self.p1 = p1
        self.p2 = p2
        self.drawn = None

    def __set_center(self, new_center: Point2D):
        self.center = new_center

    def move(self, new_center: Point2D, canvas: Canvas) -> None:
        dx, dy = Point2D.offset(self.center, new_center)
        self.p1.x += dx
        self.p2.x += dx
        self.p1.y += dy
        self.p2.y += dy
        self.center = new_center
        if self.drawn is not None:
            canvas.coords(self.drawn, self.get_location()[2:])

    def get_location(self) -> tuple:
        return self.center.x, self.center.y, self.p1.x, self.p1.y, self.p2.x, self.p2.y

    def move_points(self, p1: Point2D, p2: Point2D, canvas=None):
        self.p1 = p1
        self.p2 = p2
        self.center = Point2D.mid_point(p1, p2)
        if canvas is not None and self.drawn is not None:
            canvas.coords(self.drawn, self.get_location()[2:])

    def is_drawn(self) -> bool:
        return self.drawn is not None

    def update(self, canvas: Canvas):
        canvas.delete(self.drawn)
        self.drawn = None
        self.draw(canvas)

    @abstractmethod
    def draw(self, canvas: Canvas):
        pass


class Rectangle(Figure):

    def draw(self, canvas: Canvas):
        if self.drawn is not None:
            canvas.coords(self.drawn, self.get_location()[2:])
        else:
            self.drawn = canvas.create_rectangle(self.get_location()[2:], fill=self.fill,
                                                 outline=self.color, width=self.width)


class Square(Rectangle):

    def __init__(self, color: str, fill: str, width: int, p1: Point2D, p2: Point2D):
        super().__init__(color, fill, width, p1, p2)
        self.move_points(p1, p2)

    def move_points(self, p1: Point2D, p2: Point2D, canvas=None):
        dx, dy = Point2D.offset(p1, p2)
        self.p1 = p1
        self.p2 = p2
        if abs(dy) < abs(dx):
            self.p2.y = p1.y + copysign(dx, dy)
        elif abs(dy) > abs(dx):
            self.p2.x = p1.x + copysign(dy, dx)
        self.center = Point2D.mid_point(self.p1, self.p2)
        if canvas is not None and self.drawn is not None:
            canvas.coords(self.drawn, self.get_location()[2:])


class Ellipse(Figure):

    def draw(self, canvas: Canvas):
        if self.drawn is not None:
            canvas.coords(self.drawn, self.get_location()[2:])
        else:
            self.drawn = canvas.create_oval(self.get_location()[2:], fill=self.fill,
                                            outline=self.color, width=self.width)


class Circle(Ellipse):

    def __init__(self, color: str, fill: str, width: int, p1: Point2D, p2: Point2D):
        super().__init__(color, fill, width, p1, p2)
        self.move_points(p1, p2)

    def move_points(self, p1: Point2D, p2: Point2D, canvas=None):
        dx, dy = Point2D.offset(p1, p2)
        self.p1 = p1
        self.p2 = p2
        if abs(dy) < abs(dx):
            self.p2.y = p1.y + copysign(dx, dy)
        elif abs(dy) > abs(dx):
            self.p2.x = p1.x + copysign(dy, dx)
        self.center = Point2D.mid_point(self.p1, self.p2)
        if canvas is not None and self.drawn is not None:
            canvas.coords(self.drawn, self.get_location()[2:])


class Triangle(Figure):

    def draw(self, canvas: Canvas):
        if self.drawn is not None:
            canvas.coords(self.drawn, self.get_location()[2:])
        else:
            self.drawn = canvas.create_polygon(self.get_location()[2:], fill=self.fill,
                                               outline=self.color, width=self.width)

    def get_location(self):
        dx, dy = Point2D.offset(self.p1, self.p2)
        return (self.center.x, self.center.y,
                self.p1.x + dx // 2, self.p1.y,
                self.p1.x, self.p2.y,
                self.p2.x, self.p2.y)


class Rhombus(Triangle):

    def get_location(self):
        dx, dy = Point2D.offset(self.p1, self.p2)
        return (self.center.x, self.center.y,
                self.p1.x + dx // 2, self.p1.y,
                self.p2.x, self.p1.y + dy // 2,
                self.p1.x + dx // 2, self.p2.y,
                self.p1.x, self.p1.y + dy // 2)


class Segment(Figure):

    def draw(self, canvas: Canvas):
        if self.drawn is not None:
            canvas.coords(self.drawn, self.get_location()[2:])
        else:
            self.drawn = canvas.create_line(self.get_location()[2:], fill=self.color, width=self.width)


class Ray(Segment):

    def __init__(self, color: str, fill: str, width: int, p1: Point2D, p2: Point2D):
        super().__init__(color, fill, width, p1, p2)
        self.move_points(p1, p2)

    def move_points(self, p1: Point2D, p2: Point2D, canvas=None):
        dx, dy = Point2D.offset(p1, p2)
        tan = abs(dy / dx) if dx != 0 else np.inf
        self.p1 = p1
        self.p2.x = self.p1.x + 10000 if p1.x < p2.x else self.p1.x -10000
        if p1.y < p2.y:
            self.p2.y = p1.y + int(abs(self.p2.x) * tan)
        elif p1.y > p2.y:
            self.p2.y = p1.y - int(abs(self.p2.x) * tan)
        self.center = p1
        if canvas is not None and self.drawn is not None:
            canvas.coords(self.drawn, self.get_location()[2:])


class Line(Ray):

    def move_points(self, p1: Point2D, p2: Point2D, canvas=None):
        dx, dy = Point2D.offset(p1, p2)
        tan = abs(dy / dx) if dx != 0 else np.inf
        self.center = Point2D.mid_point(p1, p2)
        if p1.x > p2.x:
            self.p1.x = self.center.x + 10000
            self.p2.x = self.center.x - 10000
        elif p1.x < p2.x:
            self.p1.x = self.center.x - 10000
            self.p2.x = self.center.x + 10000
        if p1.y < p2.y:
            self.p2.y = self.center.y + 10000 * tan
            self.p1.y = self.center.y - 10000 * tan
        elif p1.y > p2.y:
            self.p2.y = self.center.y - 10000 * tan
            self.p1.y = self.center.y + 10000 * tan
        if canvas is not None and self.drawn is not None:
            canvas.coords(self.drawn, self.get_location()[2:])
