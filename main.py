from PyQt5.QtWidgets import QApplication
from ui.dashboard import DashboardWindow
import sys
from routes.transit_routes import transit_routes
from flask import Flask
import os

main = Flask(__name__)

main.register_blueprint(transit_routes)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardWindow()
    window.show()
    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main.run(debug=True)
