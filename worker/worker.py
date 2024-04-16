from PyQt6.QtCore import QThread, pyqtSignal

class Worker(QThread):
    """
    A class used to represent a Worker thread

    ...
    Attributes
    ----------
    model : SudokuBoard
        The model being adjusted
    controller : SudokuController
        The controller handling user decisions
        
    Methods
    -------
    run()
        Runs the worker thread
    """
    
    def __init__(self, model, controller):
        """
        Parameters
        ----------
        model : SudokuBoard
            The model being adjusted
        controller : SudokuController
            The controller handling user decisions
        """
        
        super().__init__()
        self.model = model
        self.controller = controller

    def run(self):
        """Runs the worker thread
        """
        
        # Disables buttons on the board until the board is solved
        self.controller.disable_buttons()
        
        # Solves the board
        self.model.solve_board()
        
        # Enables buttons once the board is solved
        self.controller.enable_buttons()