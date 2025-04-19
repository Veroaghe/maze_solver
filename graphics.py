# tkinter packer: https://docs.python.org/3/library/tkinter.html#the-packer
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.title = "Maze Solver"

        self.__cvs = Canvas(self.__root, bg="white", width=self.width, height=self.height)
        self.__cvs.pack(fill=BOTH, expand=1)

        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def draw_line(self, line, fill_color="black"):
        '''line is an instance of Line'''
        line.draw(self.__cvs, fill_color)
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Maze Solver Closed...")
    
    def close(self):
        self.__running = False


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        ''' Takes 2 instances of Point as its arguments'''
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, cvs, fill_color):
        x1 = self.p1.x
        y1 = self.p1.y
        x2 = self.p2.x
        y2 = self.p2.y
        cvs.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
        )