from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt6.QtCore import QSize, Qt
from view.sudoku_tile import SudokuTile

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
        self.setFixedSize(QSize(156, 156))

        # Establishes the layout of the SudokuSquare object
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(2)
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
