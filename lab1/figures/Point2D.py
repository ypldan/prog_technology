class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def mid_point(p1, p2):
        return Point2D(min(p1.x, p2.x) + int(abs(p1.x - p2.x) / 2),
                       min(p1.y, p2.y) + int(abs(p1.y - p2.y) / 2))

    @staticmethod
    def distance(p1, p2):
        return int((abs(p1.x - p2.x) ** 2 + abs(p1.y - p2.y) ** 2) ** 0.5)

    @staticmethod
    def offset(p1, p2):
        return p2.x - p1.x, p2.y - p1.y
