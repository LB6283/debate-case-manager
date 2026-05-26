#!/bin/python3
import sqlite3
import backend
import ui
import sys
from PySide6.QtWidgets import QApplication


def main():
    backend.create_database()
    app = QApplication()
    window = ui.DebateApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
