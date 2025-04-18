# tkinter packer: https://docs.python.org/3/library/tkinter.html#the-packer
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.__root = Tk()
        self.__root.title = "Maze Solver"

        self.__cvs = Canvas(self.__root, width=self.__width, height=self.__height)
        self.__cvs.pack()

        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Maze Solver Closed...")
    
    def close(self):
        self.__running = False