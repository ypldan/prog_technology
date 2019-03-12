from abc import ABC

from figures.Figure import Figure
from figures.Point2D import Point2D


class Figure2Points(Figure, ABC):

    def __init__(self, color: str, fill: str, width: int, p1: Point2D, p2: Point2D):
        super().__init__(color, fill, width)
        self.points = None
        self.p1 = p1
        self.p2 = p2
        self.center = Point2D.mid_point(p1, p2)
        self.color = color
        self.fill = fill
        self.width = width
        self.drawn = None

    def move(self, new_center: Point2D, canvas=None):
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
