from model.sudoku import SudokuBoard
from PyQt6.QtWidgets import QApplication 
import view.sudokuview as view
import controller.sudokucontroller as control

def run():
    # Creates the model for the board
    model = SudokuBoard()
    
    # Creates the view by handing it the model
    app = QApplication([])
    window = view.SudokuView(model)
    
    # Hands the model and view to the controller
    controller = control.SudokuController(model, window)
    controller.register_buttons()
    
    # Shows the view
    window.show()
    
    # Launches the application
    app.exec()

if __name__ == '__main__':
    run()