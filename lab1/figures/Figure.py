from figures.Point2D import Point2D
from abc import ABC, abstractmethod
from tkinter import Canvas


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
