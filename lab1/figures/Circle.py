from figures.Ellipse import Ellipse
from figures.Point2D import Point2D
from figures.utils import copysign


class Circle(Ellipse):

    def __init__(self, color: str, fill: str, width: int, p1: Point2D, p2: Point2D):
        super().__init__(color, fill, width, p1, p2)
        self.move_points(p1, p2)

    def move_points(self, *points, canvas=None):
        if len(points) != 2:
            raise Exception('Number of points is not 2')
        p1 = points[0]
        p2 = points[1]
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
