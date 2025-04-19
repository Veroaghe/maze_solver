from random import randrange
from graphics import Window, Point, Line


def main():
    win = Window(800, 600)

    for _ in range(3):
        p1 = Point(randrange(0, win.width), randrange(0, win.height))
        p2 = Point(randrange(0, win.width), randrange(0, win.height))
        line = Line(p1, p2)
        win.draw_line(line, "black")

    win.wait_for_close()


if __name__ == "__main__":
    main()