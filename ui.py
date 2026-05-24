# All UI stuff goes here, all database logic belongs in backend.py
import backend
import sys
from PySide6.QtWidgets import (
    QApplication,
    QBoxLayout,
    QCheckBox,
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

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.add_case = QWidget()
        self.remove_case = QWidget()
        self.add_citation = QWidget()
        self.remove_citation = QWidget()
        self.add_contention = QWidget()
        self.remove_contention = QWidget()
        self.export = QWidget()

        self.tabs.addTab(self.add_case, "Add a case")
        self.tabs.addTab(self.remove_case, "Delete a case")
        self.tabs.addTab(self.add_citation, "Add a citation")
        self.tabs.addTab(self.remove_citation, "Remove a citation")
        self.tabs.addTab(self.add_contention, "Add a contention")
        self.tabs.addTab(self.remove_contention, "Remove a contention")
        self.tabs.addTab(self.export, "Export a case to PDF")

        self.setup_add_case()

    def setup_add_case(self):
        layout = QVBoxLayout()
        layout1 = QHBoxLayout()

        enter_name = QLineEdit()
        submit_btn = QPushButton("Add Case")
        debate_type = QCheckBox()

        layout1.addWidget(enter_name)
        layout1.addWidget(submit_btn)
        layout.addLayout(layout1)
        layout.addWidget(debate_type)

        self.add_case.setLayout(layout)

        def setup_remove_case(self):
            layout = QVBoxLayout()
            layout1 = QHBoxLayout()

            enter_name = QLineEdit()


# Get rid of this code later, just for testing the UI, will move to main.py once app is complete
app = QApplication()
window = DebateApp()
window.show()
sys.exit(app.exec())
