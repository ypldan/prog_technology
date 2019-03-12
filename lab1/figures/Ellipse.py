from figures.Figure import Figure
from tkinter import Canvas


class Ellipse(Figure):

    def draw(self, canvas: Canvas):
        if self.drawn is not None:
            canvas.coords(self.drawn, self.get_location()[2:])
        else:
            self.drawn = canvas.create_oval(self.get_location()[2:], fill=self.fill,
                                            outline=self.color, width=self.width)
