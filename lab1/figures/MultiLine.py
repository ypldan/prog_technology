from tkinter import Canvas
from figures.FigurePolyPoints import FigurePolyPoints


class MultiLine(FigurePolyPoints):
    def draw(self, canvas: Canvas):
        if self.is_drawn():
            canvas.coords(self.drawn, self.get_location())
        else:
            self.drawn = canvas.create_line(self.get_location(), fill=self.color, width=self.width)
