from Point2D import Point2D
from Segment import Segment


class Ray(Segment):

    def __init__(self, color: str, fill: str, width: int, p1: Point2D, p2: Point2D):
        super().__init__(color, fill, width, p1, p2)
        self.move_points(p1, p2)

    def move_points(self, p1: Point2D, p2: Point2D, canvas=None):
        dx, dy = Point2D.offset(p1, p2)
        tan = abs(dy / dx) if dx != 0 else 0
        self.p1 = p1
        self.p2.x = self.p1.x + 10000 if p1.x < p2.x else self.p1.x -10000
        if p1.y < p2.y:
            self.p2.y = p1.y + int(abs(self.p2.x) * tan)
        elif p1.y > p2.y:
            self.p2.y = p1.y - int(abs(self.p2.x) * tan)
        self.center = p1
        if canvas is not None and self.drawn is not None:
            canvas.coords(self.drawn, self.get_location()[2:])
