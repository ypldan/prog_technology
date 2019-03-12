from figures.Figure import Figure
from figures.Point2D import Point2D
from abc import ABC


class FigurePolyPoints(Figure, ABC):

    def __init__(self, color: str, fill: str, width: int, *points):
        super().__init__(color, fill, width, *points)
        self.points = list(points)
        self.center = Point2D(0, 0)
        if len(points) != 0:
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
            canvas.coords(self.drawn, self.get_location())

    def get_location(self):
        result = []
        for point in self.points:
            result.append(point.x)
            result.append(point.y)
        return tuple(result)

    def move_points(self, *points, canvas=None):
        if len(self.points) != len(points):
            raise Exception('Number of points is not equal')
        for i in range(len(points)):
            self.points[i] = points[i]
        if self.is_drawn():
            canvas.coords(self.drawn, self.get_location())

    def add_point(self, point: Point2D, canvas=None):
        self.points.append(point)
        if len(self.points) == 1:
            self.center = point
        if self.is_drawn() and canvas is not None:
            self.update(canvas)
