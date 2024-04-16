from PyQt6.QtWidgets import QPushButton

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
    
    def set_text(self, text):
        """Sets the text of the tile

        Parameters
        ----------
        text : str
            The value to set as the text of the tile
        """
        
        self.setText(text)

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