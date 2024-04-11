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
        
    Methods
    -------
    register_buttons()
        Allows the buttons on the board to be clicked
    
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
    
    def register_buttons(self):
        """Allows the buttons on the board to be clicked
        """
        
        self.view.get_validate_button().clicked.connect(self.view_to_model_board)
        self.view.get_solve_button().clicked.connect(self.model.solve_board)
        self.view.get_quit_button().clicked.connect(self.view.shutdown)
    
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
        row, col = 0, 0
        offset_row, offset_col = 0, 0
        for square in range(len(condensed)):
            offset_row = 3 * (square // 3)
            for num in range(len(condensed)):
                offset_col = 3 * (square % 3)
                row = offset_row + (num // 3)
                col = offset_col + (num % 3)
                if condensed[square].get_list()[num].text() == "":
                    board[row].append(0)
                else:
                    board[row].append(int(condensed[square].get_list()[num].text()))
            offset_col = 0
                 
        # Assigns translated items to the board   
        self.model.set_board(board)