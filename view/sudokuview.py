from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize, Qt

class SudokuTile(QPushButton):
    """
    A class used to represent a SudokuTile object

    ...
    
    Methods
    -------
    keyPressEvent(event)
        Registers the numbers 1-9 on key press

    mousePressEvent(event)
        Highlights the current tile position 
    
    __str__()
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
        
        Parameters
        ----------
        event : QMouseEvent
            A mouse click
        """
        
        key = event.key()
        if 49 <= key <= 57:  # ASCII values for digits 1-9
            digit = chr(key)
            self.setText(digit)

    def mousePressEvent(self, event):
        """Highlights the current tile position
        
        Parameters
        ----------
        event : QMouseEvent
            A mouse click
        """
        
        if self.hasFocus:
            self.clearFocus()  # Clear focus to remove highlight
            self.hasFocus = False
        else:
            self.setFocus()  # Set focus to highlight
            self.hasFocus = True
        super().mousePressEvent(event)
    
    def __str__(self):
        """String representation of the SudokuTile object
        
        Returns:
            A string of the SudokuTile
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
    get_list()
        Returns the list of SudokuTiles inside the SudokuSquare
    
    __str__()
        String representation of the SudokuSquare object
    """
    
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(156, 156))  # Adjust the size to fit 3x3 SudokuTile widgets plus spacing

        # Establishes the layout of the SudokuSquare object
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
        
        Returns:
            A list of SudukoTiles
        """
        
        return self.square
    
    def __str__(self):
        """String representation of the SudokuSquare object
        
        Returns:
            A string of the current SudokuSquare object
        """
        
        return " ".join([f"{self.square[tile]}" if self.square[tile].text() != "" else "0" for tile in range(len(self.square))])


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
    get_squares()
        Returns a 2D list of SudokuSquares
        
    get_validate_button()
        Gets the validate button
    
    get_solve_button()
        Gets the solve button
    
    get_quit_button()
        Gets the quit button
    
    shutdown()
        Executes the shutdown process
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
    
    def shutdown(self):
        """Executes the shutdown process
        """
        
        reply = QMessageBox.question(self, 'Quit Sudoku?',
                                     "Are you sure to quit?", QMessageBox.StandardButton.Yes | 
                                     QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
         
        if reply == QMessageBox.StandardButton.Yes:
            self.close()
            print('Window closed')