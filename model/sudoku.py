class SudokuBoard:
    """
    A class used to represent a SudokuBoard

    ...
    Attributes
    ----------
    board : list
        A collection of lists of integers
    square_size : int
        The width/length of 1 square
    row_col_len : int
        The size of a row/column
        
    Methods
    -------
    advance(self, row, col)
    
    __str__()
        String representation of the SudokuBoard
    """
    def __init__(self, unsolved_board=[[0,0,0,0,0,0,0,0,0],
                                       [0,0,0,0,0,0,0,0,0],
                                       [0,0,0,0,0,0,0,0,0],
                                       [0,0,0,0,0,0,0,0,0],
                                       [0,0,0,0,0,0,0,0,0],
                                       [0,0,0,0,0,0,0,0,0],
                                       [0,0,0,0,0,0,0,0,0],
                                       [0,0,0,0,0,0,0,0,0],
                                       [0,0,0,0,0,0,0,0,0]]):
        """
        Parameters
        ----------
        board : list, optional
            A collection of lists of integers
        """

        self.board = unsolved_board
        self.square_size = 3
        self.row_col_len = 9
        
    def get_board(self):
        return self.board
    
    def set_board(self, board):
        self.board = board
    
    def insert_value(self, row, column, value):
        self.board[row][column] = value
        
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
        """String representation of the SudokuBoard
        """
        built_string = ""
        
        # For loop that builds the rows of the board
        # Adds dashes ( - ) to separate each 1/3rd of the board
        for i in range(len(self.board)):
            if i % self.square_size == 0:
                built_string += " - - - - - - - - - - \n"
            
            built_string += " | "
            
            # For loop that tracks each column
            for j in range(self.row_col_len):
                built_string += f"{self.board[i][j]}"
                
                # Adds pipe ( | ) to separate each square
                if (j + 1) % self.square_size == 0:
                    built_string += " | "
            
            # Drops to the next line       
            built_string += "\n"
            
        built_string += " - - - - - - - - - - \n"
            
        return f"FORMATTED BOARD: \n{built_string}"