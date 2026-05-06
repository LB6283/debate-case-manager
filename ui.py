# All UI stuff goes here, all database logic belongs in backend.py
import backend
import sys
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QTabWidget,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
)


class DebateApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Debate Case Manager")

        self.resize(1000, 800)

    # PLAN FOR APP:
    # It will have the following tabs:
    # Add Case
    # Edit Citations to case
    # Remove Case
    # Export Case To PDF
    # Add contention to a case
    # (The tabs will probably not be in this order)


app = QApplication()
window = DebateApp()
window.show()
sys.exit(app.exec())
