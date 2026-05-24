import init_db
import ui
import sys
from PySide6.QtWidgets import QApplication


def main():
    init_db.create_database()
    app = QApplication()
    window = ui.DebateApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
