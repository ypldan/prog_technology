from Point2D import Point2D
from Ray import Ray


class Line(Ray):

    def move_points(self, p1: Point2D, p2: Point2D, canvas=None):
        dx, dy = Point2D.offset(p1, p2)
        tan = abs(dy / dx) if dx != 0 else 0
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
