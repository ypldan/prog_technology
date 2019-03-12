from abc import ABC, abstractmethod
from tkinter import Canvas
from figures.Point2D import Point2D


class Figure(ABC):

    @abstractmethod
    def __init__(self, color: str, fill: str, width: int, *points):
        pass

    @abstractmethod
    def move(self, new_center: Point2D, canvas=None):
        pass

    @abstractmethod
    def get_location(self):
        pass

    def is_drawn(self) -> bool:
        return self.drawn is not None

    def update(self, canvas: Canvas):
        canvas.delete(self.drawn)
        self.drawn = None
        self.draw(canvas)

    @abstractmethod
    def move_points(self, *points, canvas=None):
        pass

    @abstractmethod
    def draw(self, canvas: Canvas):
        pass
