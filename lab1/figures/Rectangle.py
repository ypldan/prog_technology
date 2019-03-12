from figures.Figure2Points import Figure2Points
from tkinter import Canvas


class Rectangle(Figure2Points):

    def draw(self, canvas: Canvas):
        if self.drawn is not None:
            canvas.coords(self.drawn, self.get_location()[2:])
        else:
            self.drawn = canvas.create_rectangle(self.get_location()[2:], fill=self.fill,
                                                 outline=self.color, width=self.width)
