import unittest

class TestSudokuSolverMethods(unittest.TestCase):
    def setUp(self):
        self.solvable_board = SudokuBoard(
            [[1,2,0,0,6,0,7,9,0],
             [0,3,0,0,0,0,0,0,0],
             [4,5,6,0,0,0,0,0,0],
             [8,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [9,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [6,0,0,0,0,0,0,0,0]])

if __name__ == '__main__':
    unittest.main()