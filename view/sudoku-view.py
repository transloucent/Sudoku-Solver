from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
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

class SudokuSquare(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(156, 156))  # Adjust the size to fit 3x3 SudokuTile widgets plus spacing

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(2)  # Minimal spacing between tiles for visual separation

        # Initialize and add SudokuTile widgets to the layout
        for j in range(3):
            for k in range(3):
                self.layout.addWidget(SudokuTile(), j, k)


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
        for i in range(3):
            for j in range(3):
                self.grid_layout.addWidget(self.squares[i][j], i, j)

if __name__ == "__main__":
    app = QApplication([])
    window = SudokuBoard()
    window.show()
    app.exec()
