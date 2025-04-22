from cell import Cell
import time, random

class Maze:
    def __init__(self, win, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, seed = None):
        self._win = win
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
    
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
        if cell._win is None:
            return
        cell.draw()
        self._animate()
    
    def _animate(self, sleep_time=0.03):
        self._win.redraw()
        time.sleep(sleep_time)
    
    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        top_left_cell.has_left_wall = False
        bottom_right_cell = self._cells[-1][-1]
        bottom_right_cell.has_right_wall = False
        self._draw_cell(top_left_cell)
        self._draw_cell(bottom_right_cell)
    
    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            if i > 0:
                if not self._cells[i-1][j].visited:
                    to_visit.append((i-1, j,))
            if j > 0:
                if not self._cells[i][j-1].visited:
                    to_visit.append((i, j-1,))
            if i < self.num_cols - 1:
                if not self._cells[i+1][j].visited:
                    to_visit.append((i+1, j,))
            if j < self.num_rows - 1:
                if not self._cells[i][j+1].visited:
                    to_visit.append((i, j+1,))
            
            if len(to_visit) == 0:
                self._draw_cell(current_cell)
                return

            dir_num = random.randrange(len(to_visit))
            direction = to_visit.pop(dir_num)
            new_i = direction[0]
            new_j = direction[1]
            other_cell = self._cells[new_i][new_j]

            if i > new_i:
                current_cell.has_left_wall = False
                other_cell.has_right_wall = False
            elif i < new_i:
                current_cell.has_right_wall = False
                other_cell.has_left_wall = False
            elif j > new_j:
                current_cell.has_top_wall = False
                other_cell.has_bottom_wall = False
            elif j < new_j:
                current_cell.has_bottom_wall = False
                other_cell.has_top_wall = False

            self._break_walls_r(new_i, new_j)
    
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
    
    def solve(self):
        self._reset_cells_visited()
        # return self._depth_first_solve_r()
        return self._random_dir_solve_r()
    
    def _depth_first_solve_r(self, i=0, j=0):
        self._animate(0.07)
        current_cell = self._cells[i][j]
        current_cell.visited = True

        if current_cell == self._cells[-1][-1]:
            return True
        
        # Right Side Cell
        if i + 1 < self.num_cols and not current_cell.has_right_wall and not self._cells[i+1][j].visited:
            current_cell.draw_move(self._cells[i+1][j])
            if self._depth_first_solve_r(i+1, j):
                return True
            else:
                current_cell.draw_move(self._cells[i+1][j], True)
        # Bottom Side Cell
        if j + 1 < self.num_rows and not current_cell.has_bottom_wall and not self._cells[i][j+1].visited:
            current_cell.draw_move(self._cells[i][j+1])
            if self._depth_first_solve_r(i, j+1):
                return True
            else:
                current_cell.draw_move(self._cells[i][j+1], True)
        # Left Side Cell
        if i - 1 >= 0 and not current_cell.has_left_wall and not self._cells[i-1][j].visited:
            current_cell.draw_move(self._cells[i-1][j])
            if self._depth_first_solve_r(i-1, j):
                return True
            else:
                current_cell.draw_move(self._cells[i-1][j], True)
        # Top Side Cell
        if j - 1 >= 0 and not current_cell.has_top_wall and not self._cells[i][j-1].visited:
            current_cell.draw_move(self._cells[i][j-1])
            if self._depth_first_solve_r(i, j-1):
                return True
            else:
                current_cell.draw_move(self._cells[i][j-1], True)
        
        return False
    
    def _random_dir_solve_r(self, i=0, j=0):
        self._animate(0.07)
        current_cell = self._cells[i][j]
        current_cell.visited = True

        if current_cell == self._cells[-1][-1]:
            return True
        
        directions = ["right", "bottom", "left", "top"]
        random.shuffle(directions)
        for direction in directions:
            # Right Side Cell
            if direction == "right" and i + 1 < self.num_cols and not current_cell.has_right_wall and not self._cells[i+1][j].visited:
                current_cell.draw_move(self._cells[i+1][j])
                if self._random_dir_solve_r(i+1, j):
                    return True
                else:
                    current_cell.draw_move(self._cells[i+1][j], True)
            # Bottom Side Cell
            if direction == "bottom" and j + 1 < self.num_rows and not current_cell.has_bottom_wall and not self._cells[i][j+1].visited:
                current_cell.draw_move(self._cells[i][j+1])
                if self._random_dir_solve_r(i, j+1):
                    return True
                else:
                    current_cell.draw_move(self._cells[i][j+1], True)
            # Left Side Cell
            if direction == "left" and i - 1 >= 0 and not current_cell.has_left_wall and not self._cells[i-1][j].visited:
                current_cell.draw_move(self._cells[i-1][j])
                if self._random_dir_solve_r(i-1, j):
                    return True
                else:
                    current_cell.draw_move(self._cells[i-1][j], True)
            # Top Side Cell
            if direction == "top" and j - 1 >= 0 and not current_cell.has_top_wall and not self._cells[i][j-1].visited:
                current_cell.draw_move(self._cells[i][j-1])
                if self._random_dir_solve_r(i, j-1):
                    return True
                else:
                    current_cell.draw_move(self._cells[i][j-1], True)
            
        return False

