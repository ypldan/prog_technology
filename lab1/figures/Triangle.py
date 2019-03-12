from tkinter import Canvas
from figures.Figure import Figure
from figures.Point2D import Point2D


class Triangle(Figure):

    def draw(self, canvas: Canvas):
        if self.drawn is not None:
            canvas.coords(self.drawn, self.get_location()[2:])
        else:
            self.drawn = canvas.create_polygon(self.get_location()[2:], fill=self.fill,
                                               outline=self.color, width=self.width)

    def get_location(self):
        dx, dy = Point2D.offset(self.p1, self.p2)
        return (self.center.x, self.center.y,
                self.p1.x + dx // 2, self.p1.y,
                self.p1.x, self.p2.y,
                self.p2.x, self.p2.y)
