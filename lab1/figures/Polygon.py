from tkinter import Canvas

from figures.FigurePolyPoints import FigurePolyPoints


class Polygon(FigurePolyPoints):

    def draw(self, canvas: Canvas):
        if self.is_drawn():
            canvas.coords(self.drawn, self.get_location())
        else:
            self.drawn = canvas.create_polygon(self.get_location(), fill=self.fill,
                                               outline=self.color, width=self.width)
