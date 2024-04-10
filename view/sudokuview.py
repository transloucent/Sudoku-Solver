from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize, Qt

class SudokuTile(QPushButton):
    """
    A class used to represent a SudokuTile object

    ...
    
    Methods
    -------
    keyPressEvent(event):
        Registers the numbers 1-9 on key press

    def mousePressEvent(event)
        Highlights the current tile position 
    
    def __str__()
        String representation of the SudokuTile object
    """
    def __init__(self):
        super().__init__()
        self.setFixedSize(50, 50)  # Fixed size for each tile
        self.setText("")  # Start with an empty text
        self.hasFocus = False  # Flag to track focus state
        
        # Style adjustments
        self.setStyleSheet("""
            QPushButton {
                border: 1px solid black;
                font-size: 16px;
            }
            QPushButton:focus {
                background-color: #81CFED;
                color: white;
            }
        """)

    def keyPressEvent(self, event):
        """Registers the numbers 1-9 in Tile cell on key press
        """
        key = event.key()
        if 49 <= key <= 57:  # ASCII values for digits 1-9
            digit = chr(key)
            self.setText(digit)

    def mousePressEvent(self, event):
        """Highlights the current tile position
        """
        if self.hasFocus:
            self.clearFocus()  # Clear focus to remove highlight
            self.hasFocus = False
        else:
            self.setFocus()  # Set focus to highlight
            self.hasFocus = True
        super().mousePressEvent(event)  # Call base class's mousePressEvent method
    
    def __str__(self):
        """String representation of the SudokuTile object
        """
        return self.text()

class SudokuSquare(QWidget):
    """
    A class used to represent a SudokuSquare object

    ...

    Attributes
    ----------
    square: list
        A collection of SudokuTile objects
    
    Methods
    -------
    get_list():
        Returns the list of SudokuTiles inside the SudokuSquare
    
    def __str__()
        String representation of the SudokuSquare object
    """
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(156, 156))  # Adjust the size to fit 3x3 SudokuTile widgets plus spacing

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(2)  # Minimal spacing between tiles for visual separation
        self.square = []

        # Initialize and add SudokuTile widgets to the layout
        for j in range(3):
            for k in range(3):
                tile = SudokuTile()
                self.square.append(tile)
                self.layout.addWidget(tile, j, k)
    
    def get_list(self):
        """Returns the list of SudokuTiles inside the SudokuSquare
        """
        return self.square
    
    def __str__(self):
        """String representation of the SudokuSquare object
        """
        return " ".join([f"{self.square[tile]}" if self.square[tile].text() != "" else "0" for tile in range(len(self.square))])


class SudokuBoard(QMainWindow):
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
    get_squares():
        Returns a 2D list of SudokuSquares
    """
    def __init__(self, board):
        """
        Parameters
        ----------
        board: list
            A list of lists of integers from the model
        """
        
        super().__init__()
        self.setWindowTitle("Sudoku Solver")
        self.setFixedSize(550, 550)  # Adjusted for spacing and margins

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.setSpacing(10)  # Spacing between the 3x3 Sudoku squares

        # Create and add 9 SudokuSquare widgets to form the entire 9x9 board
        self.squares = [[SudokuSquare() for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.grid_layout.addWidget(self.squares[i][j], i, j)
                
        self.validate_button = QPushButton("Validate Board")
        self.grid_layout.addWidget(self.validate_button)
        
        self.solve_button = QPushButton("Solve Board")
        self.grid_layout.addWidget(self.solve_button)
    
    def get_validate_button(self):
        return self.check_valid_button
    
    def get_solve_button(self):
        return self.solve_button
    
    def get_squares(self):
        """
        Returns a 2D list of SudokuSquares
        """
        return self.squares