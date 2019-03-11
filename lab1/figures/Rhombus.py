from Point2D import Point2D
from Triangle import Triangle


class Rhombus(Triangle):

    def get_location(self):
        dx, dy = Point2D.offset(self.p1, self.p2)
        return (self.center.x, self.center.y,
                self.p1.x + dx // 2, self.p1.y,
                self.p2.x, self.p1.y + dy // 2,
                self.p1.x + dx // 2, self.p2.y,
                self.p1.x, self.p1.y + dy // 2)
