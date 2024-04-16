from worker.worker import Worker

class SudokuController:
    """
    A class used to represent a SudokuController

    ...
    Attributes
    ----------
    model : SudokuBoard
        A model to represent the SudokuBoard
    view : SudokuView
        A view to visualize the SudokuBoard
    square_constant : int
        A default value for the square constant
        
    Methods
    -------
    on_model_changed(row, col, pos, value)
        Handles the view update from the model
    
    register_buttons()
        Allows the buttons on the board to be clicked
        
    enable_buttons()
        Enable all buttons
    
    disable_buttons()
        Disable all buttons
        
    validate_board()
        Validates the current board displayed in the view
        
    solve_board()
        Solves the board displayed in the view
    
    view_to_model_board()
        Translates the 2D board from the view to a 2D board for the model
    """
    
    def __init__(self, model, view):
        """
        Parameters
        ----------
        model : SudokuBoard
            A collection of lists of integers
        view : SudokuView
            A view to visualize the SudokuBoard
        """
        
        self.model = model
        self.view = view
        self.square_constant = 3
        
        # Connect signal to change method
        self.model.elementChanged.connect(self.on_model_changed)
        
    def on_model_changed(self, row, col, pos, value):
        """Handles the view update from the model
        
        Parameters
        ----------
        row : int
            Row index of the view's 2D array
        col : int
            Column index of the view's 2D array
        pos : int
            Position in the 1D array to update
        value : int
            Value to replace in the board
        """
        
        self.view.update_tile(row, col, pos, value)
    
    def register_buttons(self):
        """Allows the buttons on the board to be clicked
        """
        
        self.view.get_validate_button().clicked.connect(self.validate_board)
        self.view.get_solve_button().clicked.connect(self.solve_board)
        self.view.get_quit_button().clicked.connect(self.view.shutdown)
        
    def enable_buttons(self):
        """Enable all buttons
        """
        
        self.view.get_validate_button().setDisabled(False)
        self.view.get_solve_button().setDisabled(False)
    
    def disable_buttons(self):
        """Disable all buttons
        """
        
        self.view.get_validate_button().setDisabled(True)
        self.view.get_solve_button().setDisabled(True)
        
    def validate_board(self):
        """Validates the current board displayed in the view
        """
        
        # Creates the board to be used for the model
        board = self.view_to_model_board()
        
        # Assigns translated items to the board   
        self.model.set_board(board)
        
        # Checks if the board is valid
        if self.model.check_board():
            self.view.validation_result_message(True)
        else:
            self.view.validation_result_message(False)
        
    def solve_board(self):
        """Solves the board displayed in the view
        """
        
        # Creates the board to be used for the model
        board = self.view_to_model_board()
        
        # Assigns translated items to the board   
        self.model.set_board(board)
        
        # Displays an error message if the board is not valid
        if not self.model.check_board():
            self.view.validation_result_message(False)
            return

        # Creates and starts a worker thread
        self.worker = Worker(self.model, self)
        self.worker.start()
    
    def view_to_model_board(self):
        """Translates the 2D board from the view to a 2D board for the model
        """
        
        # Condenses the board to a 1D list of SudokuSquare objects
        condensed = []
        for j in range(3):
            for k in range(3):
                condensed.append(self.view.get_squares()[j][k])
                
        # Transforms the board from a list of SudokuSquare objects to a 2D list of numbers
        # Can be used to check if the board is correct or can be used to solve the board
        board = [[] for _ in range(len(condensed))]
        
        # Variables for board translation
        row, col = 0, 0
        offset_row, offset_col = 0, 0
        
        # For loop that determines the offests to use for translating the board
        for square in range(len(condensed)):
            offset_row = self.square_constant * (square // self.square_constant)
            
            for num in range(len(condensed)):
                offset_col = self.square_constant * (square % self.square_constant)
                row = offset_row + (num // self.square_constant)
                col = offset_col + (num % self.square_constant)
                
                # Appends values to the board at the specified index
                if condensed[square].get_list()[num].text() == "":
                    board[row].append(0)
                else:
                    board[row].append(int(condensed[square].get_list()[num].text()))
                    
            offset_col = 0
                 
        return board