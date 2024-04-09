from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize, Qt

class SudokuTile(QPushButton):
    def __init__(self):
        super().__init__()
        self.setFixedSize(50, 50)  # Fixed size for each tile
        self.setText("")  # Start with an empty text
        self.hasFocus = False  # Flag to track focus state
        # Style adjustments for better clarity
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
        key = event.key()
        if 49 <= key <= 57:  # ASCII values for digits 1-9
            digit = chr(key)
            self.setText(digit)

    def mousePressEvent(self, event):
        if self.hasFocus:
            self.clearFocus()  # Clear focus to remove highlight
            self.hasFocus = False
        else:
            self.setFocus()  # Set focus to highlight
            self.hasFocus = True
        super().mousePressEvent(event)  # Call base class's mousePressEvent method
    
    def __str__(self):
        return self.text()

class SudokuSquare(QWidget):
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
        return self.square
    
    def get_list_pos(self, num):
        return self.square[num]
    
    def __str__(self):
        return " ".join([f"{self.square[tile]}" if self.square[tile].text() != "" else "0" for tile in range(len(self.square))])


class SudokuBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sudoku Solver")
        self.setFixedSize(550, 550)  # Adjusted for spacing and margins

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.setSpacing(10)  # Spacing between the 3x3 Sudoku squares

        # Create and add 9 SudokuSquare widgets to form the entire 9x9 board
        self.squares = [[SudokuSquare() for _ in range(3)] for _ in range(3)]
        self.board = []
        for i in range(3):
            for j in range(3):
                self.grid_layout.addWidget(self.squares[i][j], i, j)
                
        self.check_valid_button = QPushButton("Validate Board")
        self.check_valid_button.clicked.connect(self.__str__)
        self.grid_layout.addWidget(self.check_valid_button)
    
    def adjust_board(self):
        # Condenses the board to a 1D list of SudokuSquare objects
        condensed = []
        for j in range(3):
            for k in range(3):
                condensed.append(self.squares[j][k])
                
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
                    board[row].append(condensed[square].get_list()[num].text())
            offset_col = 0
                 
        # Assigns translated items to the board   
        self.board = board
                
    def __str__(self):
        self.adjust_board()
        print(self.board)

