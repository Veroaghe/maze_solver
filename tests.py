import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(None, 0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
    
    def test_maze_entry_and_exit(self):
        num_cols = 2
        num_rows = 2
        m1 = Maze(None, 0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False
        )
        self.assertEqual(
            m1._cells[-1][-1].has_right_wall,
            False
        )
    
    def test_reset_visited(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(None, 0, 0, num_rows, num_cols, 10, 10)

        for i in range(m1.num_cols):
            for j in range(m1.num_rows):
                self.assertEqual( # On maze creation, every cell should be visited
                    m1._cells[i][j].visited,
                    True
                )

        m1._reset_cells_visited()
        for i in range(m1.num_cols):
            for j in range(m1.num_rows):
                self.assertEqual( # On maze creation, every cell should be visited
                    m1._cells[i][j].visited,
                    False
                )

if __name__ == "__main__":
    unittest.main()