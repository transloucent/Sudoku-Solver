from model.sudoku import SudokuBoard
from PyQt6.QtWidgets import QApplication 
import view.sudokuview as view
import controller.sudokucontroller as control

def run():
    # Establishes PyQt
    app = QApplication([])
    
    # Creates the model and view for the board
    model = SudokuBoard()
    window = view.SudokuView()
    
    # Hands the model and view to the controller, registers view's buttons
    controller = control.SudokuController(model, window)
    controller.register_buttons()
    
    # Shows the view
    window.show()
    
    # Launches the application
    app.exec()

if __name__ == '__main__':
    run()