from abc import ABC, abstractmethod
from tkinter import Canvas
from figures.Point2D import Point2D


class Figure(ABC):

    def __init__(self, color: str, fill: str, width: int, *points):
        if len(points) != 0:
            self.points = points
            self.center = points[0]
        self.color = color
        self.fill = fill
        self.width = width
        self.drawn = None

    def move(self, new_center: Point2D, canvas=None):
        dx, dy = Point2D.offset(self.center, new_center)
        for point in self.points:
            point.x += dx
            point.y += dy
        self.center = new_center
        if self.is_drawn() and canvas is not None:
            canvas.coords(self.drawn, self.get_location()[2:])

    def get_location(self):
        return self.points

    def is_drawn(self) -> bool:
        return self.drawn is not None

    def update(self, canvas: Canvas):
        canvas.delete(self.drawn)
        self.drawn = None
        self.draw(canvas)

    @abstractmethod
    def draw(self, canvas: Canvas):
        pass
