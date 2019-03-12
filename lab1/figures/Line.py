from figures.Point2D import Point2D
from figures.Ray import Ray


class Line(Ray):

    def move_points(self, *points, canvas=None):
        if len(points) != 2:
            raise Exception('Number of points is not 2')
        p1 = points[0]
        p2 = points[1]
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
