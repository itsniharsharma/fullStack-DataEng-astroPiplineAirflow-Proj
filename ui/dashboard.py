from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QTextEdit, QTabWidget, QMessageBox
)
from PyQt5.QtSvg import QSvgWidget
from services.storage import load_rashiphal, save_rashiphal
from services.api_service import fetch_transit_chart

import os

SIGNS = [
    'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo',
    'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
]

class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Astrologer Panel – AstroNihar")
        self.setGeometry(100, 100, 1000, 700)
        self.layout = QVBoxLayout()

        self.svg_widget = QSvgWidget("data/transit_chart.svg")
        self.svg_widget.setFixedHeight(300)

        self.tabs = QTabWidget()
        self.text_boxes = {}

        rashiphal = load_rashiphal()

        for sign in SIGNS:
            editor = QTextEdit()
            editor.setText(rashiphal.get(sign, ""))
            self.text_boxes[sign] = editor
            self.tabs.addTab(editor, sign.capitalize())

        self.save_btn = QPushButton("💾 Save Rashiphala")
        self.save_btn.clicked.connect(self.save_data)

        self.refresh_btn = QPushButton("🔄 Refresh Transit Chart")
        self.refresh_btn.clicked.connect(self.refresh_chart)

        self.layout.addWidget(QLabel("🌌 Current Transit Chart"))
        self.layout.addWidget(self.svg_widget)
        self.layout.addWidget(self.refresh_btn)
        self.layout.addWidget(QLabel("📝 Write Rashiphala for Each Sign"))
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.save_btn)

        self.setLayout(self.layout)

    def save_data(self):
        data = {sign: self.text_boxes[sign].toPlainText() for sign in SIGNS}
        save_rashiphal(data)
        QMessageBox.information(self, "Saved", "✅ Rashiphala saved successfully!")

    def refresh_chart(self):
        try:
            fetch_transit_chart()
            self.svg_widget.load("data/transit_chart.svg")
            QMessageBox.information(self, "Updated", "✅ Transit chart updated!")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to update chart:\n{e}")
