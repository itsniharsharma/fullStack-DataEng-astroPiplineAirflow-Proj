from PyQt5.QtWidgets import QApplication
from ui.dashboard import DashboardWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardWindow()
    window.show()
    sys.exit(app.exec_())
