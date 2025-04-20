from cell import Cell
import time

class Maze:
    def __init__(self, win, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y):
        self._win = win
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y

        self._create_cells()
    
    def _create_cells(self):
        self._cells = []
        for col in range(self.num_cols):
            column = []
            for row in range(self.num_rows):
                x1 = self._x1 + (self.cell_size_x * col)
                y1 = self._y1 + (self.cell_size_y * row)
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                cell = Cell(self._win, x1, y1, x2, y2)
                column.append(cell)
                self._draw_cell(cell)
            self._cells.append(column)
        
    def _draw_cell(self, cell):
        cell.draw()
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)