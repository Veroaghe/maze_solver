from graphics import Point, Line

class Cell:
    def __init__(self, win, x1, y1, x2, y2):
        '''
        x1, y1 = top left coordinates of the cell
        x2, y2 = bottom right coordinates of the cell
        '''

        if x1 > x2 or y1 > y2:
            raise ValueError("Coordinates are invalid: (x1, y1) must be the top-left and (x2, y2) must be the bottom-right.")

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.p1 = Point(x1, y1) # top left
        self.p2 = Point(x2, y1) # top right
        self.p3 = Point(x2, y2) # bottom right
        self.p4 = Point(x1, y2) # bottom left

        center_x = x2 - ((x2 - x1) / 2)
        center_y = y2 - ((y2 - y1) / 2)
        self.center = Point(center_x, center_y)

        self.top_line = Line(self.p1, self.p2)
        self.right_line = Line(self.p2, self.p3)
        self.bottom_line = Line(self.p3, self.p4)
        self.left_line = Line(self.p4, self.p1)

        self._win = win

        self.visited = False
    
    def draw(self):
        if self.has_top_wall:
            self._win.draw_line(self.top_line)
        else:
            self._win.draw_line(self.top_line, "white")
        
        if self.has_right_wall:
            self._win.draw_line(self.right_line)
        else:
            self._win.draw_line(self.right_line, "white")

        if self.has_bottom_wall:
            self._win.draw_line(self.bottom_line)
        else:
            self._win.draw_line(self.bottom_line, "white")

        if self.has_left_wall:
            self._win.draw_line(self.left_line)
        else:
            self._win.draw_line(self.left_line, "white")
    
    def draw_move(self, other, undo=False):
        if undo:
            color = "blue"
        else:
            color = "red"
        
        self._win.draw_line(Line(self.center, other.center), color)
    