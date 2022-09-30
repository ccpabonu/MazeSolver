import sys

from PyQt5.QtWidgets import QApplication
from UI.MainWindows import MainWindows

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec())