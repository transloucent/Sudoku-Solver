import sys
import time

class recursionlimit:
    def __init__(self, limit):
        self.limit = limit

    def __enter__(self):
        self.old_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)

class SudokuBoard:
    
    def __init__(self, unsolved_board):
        self.board = unsolved_board
        self.square_size = 3
        self.row_col_len = 9
        
    def advance(self, row, col):
        if row == 8 and col == 8:
            col = 8
            row = 8
        elif col == 8:
            col = 0
            row += 1
        else:
            col += 1
            
        return row, col
    
    def decrement(self, row, col):
        if col == 0 and row != 0:
            col = 8
            row -= 1
        else:
            col -= 1
            
        return row, col
        
    def validate_nums(self, row=-1, column=-1):
        check = [0,0,0,0,0,0,0,0,0]
        
        for i in range(self.row_col_len):
            if row == -1:
                num = self.board[i][column - 1]
            else:
                num = self.board[row - 1][i]
            
            if num == 0:
                continue
            elif num != check[num - 1]:
                check[num - 1] = num
            else:
                return False
        return True
        
    def check_row(self, row):
        return self.validate_nums(row=row)
    
    def check_column(self, column):
        return self.validate_nums(column=column)
    
    def check_square(self, square):
        check = [0,0,0,0,0,0,0,0,0]
        
        for i in range(self.square_size):
            row = i + (((square - 1) // self.square_size) * self.square_size)
            
            for j in range(self.square_size):
                column = j + self.square_size * (((square - 1) % self.square_size))
                
                num = self.board[row][column]
                
                if num == 0:
                    continue
                elif num != check[num - 1]:
                    check[num - 1] = num
                else:
                    return False
            
        return True
    
    def check_board(self):
        for i in range(self.row_col_len):
            check = self.check_row(i) and self.check_column(i) and self.check_square(i)
            if not check:
                return False
        return True
    
    def is_solved(self):
        for i in range(self.row_col_len):
            if 0 in self.board[i]:
                return False
        return True
    
    def solve_board(self, row=0, col=0):
        if not self.is_solved():
            if self.board[row][col] == 0:
                for num in range(1, 10):
                    self.board[row][col] = num
                
                    if self.check_board():
                        row, col = self.advance(row, col)
                        self.solve_board(row, col)
                        row, col = self.decrement(row, col)
                        
                        if self.is_solved():
                            break
                        
                if not self.is_solved():
                    self.board[row][col] = 0
                    
            else:
                row, col = self.advance(row, col)
                self.solve_board(row, col)
            
    def __str__(self):
        built_string = ""
        
        for i in range(len(self.board)):
            if i % self.square_size == 0:
                    built_string += " - - - - - - - - - - \n"
            
            built_string += " | "
            
            for j in range(self.row_col_len):
                built_string += f"{self.board[i][j]}"
                
                if (j + 1) % self.square_size == 0:
                    built_string += " | "
                    
            built_string += "\n"
            
        built_string += " - - - - - - - - - - \n"
            
        return f"FORMATTED BOARD: \n{built_string}"


def run():
    test_case = [[1,2,0,0,6,0,7,9,0],
                 [0,3,0,0,0,0,0,0,0],
                 [4,5,6,0,0,0,0,0,0],
                 [8,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [9,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [6,0,0,0,0,0,0,0,0]]
    
    board = SudokuBoard(test_case)
    board.solve_board()
    print(board)

if __name__ == '__main__':
    run()