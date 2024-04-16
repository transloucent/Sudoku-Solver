from PyQt6.QtCore import QThread, pyqtSignal

class Worker(QThread):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def run(self):
        self.model.solve_board()