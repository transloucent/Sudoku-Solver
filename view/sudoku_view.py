from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QGridLayout, QMessageBox
from PyQt6.QtGui import QIcon
from view.sudoku_square import SudokuSquare

class SudokuView(QMainWindow):
    """
    A class used to represent a SudokuBoard view

    ...

    Attributes
    ----------
    squares: list
        A collection of lists of SudokuSquare objects
    board : list
        A collection of lists of integers representing the rows on a SudokuBoard
    
    Methods
    -------
    init_ui()
        Initializes the UI for the Sudoku board
    
    get_validate_button()
        Gets the validate button
    
    get_solve_button()
        Gets the solve button
    
    get_quit_button()
        Gets the quit button
    
    get_squares()
        Gets a 2D list of SudokuSquares
    
    update_tile(square_row, square_col, pos, value)
        Updates the current tile text with the provided value
    
    validation_result_message(result)
        Displays a message indicating the result of the validation check
    
    shutdown()
        Executes the shutdown process
    """
    
    def __init__(self):
        """
        Parameters
        ----------
        board: list
            A list of lists of integers from the model
        """
        
        # Establishes board and UI
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        """Initializes the UI for the Sudoku board
        """
        
        # Establishes window elements
        self.setWindowIcon(QIcon('../assets/sudoku_icon.png'))
        self.setWindowTitle("Sudoku Solver")
        self.setFixedSize(550, 550)  # Adjusted for spacing and margins

        # Establishes the layout of the board
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.setSpacing(10)  # Spacing between the 3x3 Sudoku squares

        # Create and add 9 SudokuSquare widgets to form the 9x9 board
        self.squares = [[SudokuSquare() for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.grid_layout.addWidget(self.squares[i][j], i, j)
                
        # Sets up buttons on the main board
        self.validate_button = QPushButton("Validate Board")
        self.grid_layout.addWidget(self.validate_button)
        
        self.solve_button = QPushButton("Solve Board")
        self.grid_layout.addWidget(self.solve_button)
        
        self.quit_button = QPushButton("Quit")
        self.grid_layout.addWidget(self.quit_button)
    
    def get_validate_button(self):
        """Gets the validate button
        
        Returns:
            The validate button
        """
        
        return self.validate_button
    
    def get_solve_button(self):
        """Gets the solve button
        
        Returns:
            The solve button
        """
        
        return self.solve_button
    
    def get_quit_button(self):
        """Gets the quit button
        
        Returns:
            The quit button
        """
        
        return self.quit_button
    
    def get_squares(self):
        """Gets a 2D list of SudokuSquares
        
        Returns:
            A collection of lists of SudokuSquares
        """
        
        return self.squares
    
    def update_tile(self, square_row, square_col, pos, value):
        """Updates the current tile text with the provided value

        Parameters:
        -----------
            square_row : int
                The SudokuSquare row location
            square_col : int
                The SudokuSquare column location
            pos : int
                The position in the SudokuSquare list
            value : int
                The value to update the SudokuTile with
        """
        
        if value == 0:
            self.squares[square_row][square_col].get_list()[pos].set_text("")
        else:
            self.squares[square_row][square_col].get_list()[pos].set_text(str(value))
    
    def validation_result_message(self, result):
        """Displays a message indicating the result of the validation check
        
        Parameters
        ----------
        result : boolean
            The result of the validation
        """
        
        if result:
            QMessageBox.information(self, "Success!", "This is a valid Sudoku board",
                                    QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.critical(self, "Error!", "This is not a valid Sudoku board. Please correct it before moving forward.",
                                    QMessageBox.StandardButton.Ok)
        
    
    def shutdown(self):
        """Executes the shutdown process
        """
        
        reply = QMessageBox.question(self, 'Quit Sudoku?',
                                     "Are you sure to quit?", QMessageBox.StandardButton.Yes | 
                                     QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
         
        if reply == QMessageBox.StandardButton.Yes:
            self.close()