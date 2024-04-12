from time import sleep
from PyQt6.QtCore import pyqtSignal

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
    get_board()
        Returns the board
    
    set_board(board)
        Sets the board
        
    advance(row, col)
        Advances the row and column along the board
    
    decrement(row, col)
        Decrements the row and column along the board
        
    validate_nums(row=-1, column=-1)
        Validates if all the numbers in the row/column are unique
        
    check_row(row)
        Checks the row for having unique values
    
    check_column(column)
        Checks the column for having unique values
    
    check_square(square)
        Validates if all the numbers in the square are unique
    
    def check_board()
        Validates that the board is a correct Sudoku board
    
    is_solved()
        Validates that the board is completely solved
    
    solve_board(row=0, col=0)
        Solves the board using backtracking
        
    __str__()
        String representation of the SudokuBoard
    """
    
    dataChanged = pyqtSignal(int)  # Signal to emit when data changes
    
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
        """Returns the board

        Returns:
            A list of lists of integers
        """
        
        return self.board
    
    def set_board(self, board):
        """Sets the board
        """
        
        self.board = board
        
    def advance(self, row, col):
        """Advances the row and column along the board

        Returns:
            The advanced row and column
        """
        
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
        """Decrements the row and column along the board

        Returns:
            The decremented row and column
        """
        
        if col == 0 and row != 0:
            col = 8
            row -= 1
        else:
            col -= 1
            
        return row, col
        
    def validate_nums(self, row=-1, column=-1):
        """Validates if all the numbers in the row/column are unique
        
        Parameters
        ----------
        row : integer, optional
            The row to check for validation
        column : integer, optional
            The column to check for validation

        Returns:
            A boolean for whether or not the numbers in the row/column are unique
        """
        
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
        """Checks the row for having unique values

        Returns:
            The boolean of whether the row is all unique
        """
        
        return self.validate_nums(row=row)
    
    def check_column(self, column):
        """Checks the column for having unique values

        Returns:
            The boolean of whether the column is all unique
        """
        
        return self.validate_nums(column=column)
    
    def check_square(self, square):
        """Validates if all the numbers in the square are unique
        
        Parameters
        ----------
        square : integer
            The numbered square (1 - 9) to check

        Returns:
            A boolean for whether or not the numbers in the square are unique
        """
        
        check = [0,0,0,0,0,0,0,0,0]
        
        for i in range(self.square_size):
            # Calculates the row to use:
            #   i : The current index
            #   square : The square we are checking
            #   square_size : The length/width of a Sudoku square (3)
            row = i + (((square - 1) // self.square_size) * self.square_size)
            
            for j in range(self.square_size):
                # Calculates the row to use:
                #   j : The current index
                #   square : The square we are checking
                #   square_size : The length/width of a Sudoku square (3)
                column = j + self.square_size * (((square - 1) % self.square_size))
                
                num = self.board[row][column]
                
                # Checks to see if a number exists in the check array
                # Continues or assigns a number if empty
                # Returns False if otherwise
                if num == 0:
                    continue
                elif num != check[num - 1]:
                    check[num - 1] = num
                else:
                    return False
            
        return True
    
    def check_board(self):
        """Validates that the board is a correct Sudoku board

        Returns:
            A boolean for whether or not the board is valid
        """
        
        for i in range(self.row_col_len):
            check = self.check_row(i) and self.check_column(i) and self.check_square(i)
            if not check:
                return False
        return True
    
    def is_solved(self):
        """Validates that the board is completely solved

        Returns:
            A boolean for whether or not the board is solved
        """
        
        for i in range(self.row_col_len):
            if 0 in self.board[i]:
                return False
        return True
    
    def translate_tile_to_view(self, row, column):
        """Translates the row, column pair in the model to the correct location in the view

         Parameters
        ----------
        row : int
            The model's row 
        column : int
            The model's column 
            
        Returns:
            The square's row/column within the view and the tile's position in the list
        """
        
        # Retrives the row/col position in the 2D list in the view
        square_row, square_col = row // self.square_size, column // self.square_size
        
        # Gets the position of the tile in the square
        pos = self.square_size * (row % self.square_size) + (column % self.square_size)
        
        return square_row, square_col, pos
    
    def solve_board(self, row=0, col=0):
        """Solves the board using backtracking
        
        Parameters
        ----------
        row : integer, optional
            The current row being checked
        column : integer, optional
            The current column being checked
        """
        
        # Checks if the board is not solved
        if not self.is_solved():
            # Checks if the row, col pair has an existing number
            if self.board[row][col] == 0:
                # Checks numbers 1 - 9 in each square
                for num in range(1, 10):
                    # Updates the board so a human can visualize it
                    self.board[row][col] = num
                    self.update_view(row, col, num)
                    #sleep(0.5)
                
                    # If the board is valid, advance the row, 
                    # solve through backtracking, and 
                    # check if the board is solved
                    if self.check_board():
                        row, col = self.advance(row, col)
                        self.solve_board(row, col)
                        row, col = self.decrement(row, col)
                        
                        if self.is_solved():
                            break
                
                # If the board is not solved, set the row, col to 0
                if not self.is_solved():
                    self.board[row][col] = 0
              
            # Performed if there's a non-zero number exists in the board   
            else:
                row, col = self.advance(row, col)
                self.solve_board(row, col)
                
    def set_view(self, view):
        """Adds a view to the model to be updated directly

         Parameters
        ----------
        view : SudukoView
            A view to be used to display updates to the model
        """
        
        self.view = view
                
    def update_view(self, row, column, value):
        """Displays updates in the model to the view

         Parameters
        ----------
        row : int
            The model's row 
        column : int
            The model's column 
        value : int
            The value to be displayed
        """
        
        square_row, square_col, pos = self.translate_tile_to_view(row, column)
        self.view.update_tile(square_row, square_col, pos, value)
            
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