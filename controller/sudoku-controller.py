from model.sudoku import SudokuBoard
from PyQt6.QtWidgets import QApplication 
import view.sudokuview as view

def run():
    # Creates the model for the board
    model = SudokuBoard()
    
    app = QApplication([])
    window = view.SudokuBoard()
    window.show()
    app.exec()

if __name__ == '__main__':
    run()