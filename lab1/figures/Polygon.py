from tkinter import Canvas

from figures.FigurePolyPoints import FigurePolyPoints


class Polygon(FigurePolyPoints):

    def __init__(self, color: str, fill: str, width: int, *points):
        super().__init__(color, fill, width, *points)

    def draw(self, canvas: Canvas):
        if self.is_drawn():
            canvas.coords(self.drawn, self.get_location())
        else:
            self.drawn = canvas.create_polygon(self.get_location(), fill=self.fill,
                                  outline=self.color, width=self.width)
