from tkinter import *
from tkinter.colorchooser import askcolor
import tkinter.font as tkfont
from figures import *
from enum import Enum


class Mode(Enum):
    DRAW = 1
    MOVE = 2


class MainWindow(object):
    __MENU_FONT = None
    __DEFAULT_COLOR = 'black'

    def __init__(self):
        self.__current = None
        self.__mode = Mode.DRAW
        self.__line_width = 5
        self.__figure = Square(self.__DEFAULT_COLOR, self.__DEFAULT_COLOR, 5, Point2D(20, 20), Point2D(100, 100))
        self.root = Tk()
        self.root.title('Paint')
        self.__MENU_FONT = tkfont.Font(family="fangsong ti", size=16)
        self.__create_menu()
        self.c = Canvas(self.root, bg='white', width=800, height=500)
        self.c.bind('<Button-1>', self.press_button)
        self.c.bind('<ButtonRelease-1>', self.release_button)
        self.c.bind('<B1-Motion>', self.move_mouse)
        self.c.pack(fill=BOTH, expand=True)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.mainloop()

    def __create_menu(self):
        self.menu = Menu(self.root)
        self.figures_menu = Menu(self.menu, tearoff=0)
        self.__create_figure_menu()
        self.menu.add_cascade(label="Create", menu=self.figures_menu, font=self.__MENU_FONT)
        self.__create_settings_menu()
        self.menu.add_cascade(label='Settings', menu=self.settings_menu, font=self.__MENU_FONT)
        self.root.config(menu=self.menu)

    def __create_figure_menu(self):
        self.figures_menu = Menu(self.menu, tearoff=0)
        create_menu = [
            {'label': 'Segment', 'command': self.__set_segment},
            {'label': 'Ray', 'command': self.__set_ray},
            {'label': 'Line', 'command': self.__set_line},
            {'label': 'Circle', 'command': self.__set_circle},
            {'label': 'Ellipse', 'command': self.__set_ellipse},
            {'label': 'Triangle', 'command': self.__set_triangle},
            {'label': 'Rectangle', 'command': self.__set_rectangle},
            {'label': 'Square', 'command': self.__set_square},
            {'label': 'Rhombus', 'command': self.__set_rhombus}
        ]
        for config in create_menu:
            config['font'] = self.__MENU_FONT
            self.figures_menu.add_radiobutton(config)

    def __create_settings_menu(self):
        self.settings_menu = Menu(self.menu, tearoff=0)
        settings_menu = [
            {'label': 'Choose line color', 'command': self.__set_line_color},
            {'label': 'Choose fill color', 'command': self.__set_fill_color},
            {'label': 'Clear', 'command': self.__clear_canvas}
        ]
        for config in settings_menu:
            config['font'] = self.__MENU_FONT
            self.settings_menu.add_command(config)

    def __set_fill_color(self):
        self.__figure.fill = askcolor(color=self.__figure.fill)[1]
        if self.__figure.is_drawn():
            self.__figure.update(self.c)

    def __set_line_color(self):
        self.__figure.color = askcolor(color=self.__figure.color)[1]
        if self.__figure.is_drawn():
            self.__figure.update(self.c)

    def __set_figure(self, figure: Figure):
        self.__figure = figure
        self.__mode = Mode.DRAW

    def __set_circle(self):
        self.__set_figure(Circle(self.__figure.color,
                                 self.__figure.fill,
                                 self.__line_width,
                                 Point2D(20, 20),
                                 Point2D(100, 100)))

    def __set_square(self):
        self.__set_figure(Square(self.__figure.color,
                                 self.__figure.fill,
                                 self.__line_width,
                                 Point2D(20, 20),
                                 Point2D(100, 100)))

    def __set_rectangle(self):
        self.__set_figure(Rectangle(self.__figure.color,
                                    self.__figure.fill,
                                    self.__line_width,
                                    Point2D(20, 20),
                                    Point2D(100, 150)))

    def __set_ellipse(self):
        self.__set_figure(Ellipse(self.__figure.color,
                                  self.__figure.fill,
                                  self.__line_width,
                                  Point2D(20, 20),
                                  Point2D(100, 150)))

    def __set_rhombus(self):
        self.__set_figure(Rhombus(self.__figure.color,
                                  self.__figure.fill,
                                  self.__line_width,
                                  Point2D(20, 20),
                                  Point2D(100, 150)))

    def __set_triangle(self):
        self.__set_figure(Triangle(self.__figure.color,
                                   self.__figure.fill,
                                   self.__line_width,
                                   Point2D(20, 20),
                                   Point2D(100, 150)))

    def __set_segment(self):
        self.__set_figure(Segment(self.__figure.color,
                                  self.__figure.fill,
                                  self.__line_width,
                                  Point2D(20, 20),
                                  Point2D(100, 150)))

    def __set_ray(self):
        self.__set_figure(Ray(self.__figure.color,
                              self.__figure.fill,
                              self.__line_width,
                              Point2D(20, 20),
                              Point2D(100, 150)))

    def __set_line(self):
        self.__set_figure(Line(self.__figure.color,
                               self.__figure.fill,
                               self.__line_width,
                               Point2D(20, 20),
                               Point2D(100, 150)))

    def __clear_canvas(self):
        self.c.delete('all')
        self.__figure.drawn = None

    def release_button(self, event):
        if self.__mode == Mode.DRAW:
            self.__figure.move_points(self.__current, Point2D(event.x, event.y))
            if not self.__figure.is_drawn():
                self.__figure.draw(self.c)
            self.__mode = Mode.MOVE
            self.__current = None

    def move_mouse(self, event):
        if self.__mode == Mode.DRAW:
            self.__figure.move_points(self.__current, Point2D(event.x, event.y), self.c)
            if not self.__figure.is_drawn():
                self.__figure.draw(self.c)

    def press_button(self, event):
        if self.__mode == Mode.DRAW:
            self.__current = Point2D(event.x, event.y)
        elif self.__mode == Mode.MOVE:
            self.__figure.move(Point2D(event.x, event.y), self.c)


if __name__ == '__main__':
    MainWindow()
