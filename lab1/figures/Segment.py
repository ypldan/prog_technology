from tkinter import Canvas
from figures.Figure2Points import Figure2Points


class Segment(Figure2Points):

    def draw(self, canvas: Canvas):
        if self.drawn is not None:
            canvas.coords(self.drawn, self.get_location()[2:])
        else:
            self.drawn = canvas.create_line(self.get_location()[2:], fill=self.color, width=self.width)
