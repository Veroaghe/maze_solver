from maze import Maze
from graphics import Window


def main():
    win = Window(800, 600)

    cell_width = cell_height = 40
    cols = rows = 10
    grid_x = (win.width - (cell_width * cols)) / 2
    grid_y = (win.height - (cell_height * rows)) / 2


    maze = Maze(win, grid_x, grid_y, cols, rows, cell_width, cell_height)
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()