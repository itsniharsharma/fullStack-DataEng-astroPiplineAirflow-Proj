import os
import json
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QTextEdit, QTabWidget, QMessageBox
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from services.api_service import fetch_transit_chart
from services.storage import load_rashiphal, save_rashiphal

SIGNS = [
    'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo',
    'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
]

class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Astrologer Panel – AstroNihar")
        self.setGeometry(100, 100, 1200, 800)

        main_layout = QVBoxLayout()

        # --- Horoscope Chart Viewer ---
        self.web_view = QWebEngineView()
        html_path = os.path.abspath("templates/transit.html")
        self.web_view.load(QUrl.fromLocalFile(html_path))
        self.web_view.setMinimumHeight(400)

        self.refresh_btn = QPushButton("🔁 Refresh Transit Chart")
        self.refresh_btn.clicked.connect(self.refresh_chart)

        main_layout.addWidget(QLabel("🌌 Live Transit Horoscope"))
        main_layout.addWidget(self.web_view)
        main_layout.addWidget(self.refresh_btn)

        # --- Rashiphala Editor Section ---
        self.tabs = QTabWidget()
        self.text_boxes = {}

        rashiphal = load_rashiphal()
        for sign in SIGNS:
            editor = QTextEdit()
            editor.setPlaceholderText(f"Write Rashiphala for {sign.capitalize()}...")
            editor.setText(rashiphal.get(sign, ""))
            self.text_boxes[sign] = editor
            self.tabs.addTab(editor, sign.capitalize())

        self.save_btn = QPushButton("💾 Save Rashiphala")
        self.save_btn.clicked.connect(self.save_data)

        main_layout.addWidget(QLabel("📝 Write Rashiphala for Each Sign"))
        main_layout.addWidget(self.tabs)
        main_layout.addWidget(self.save_btn)

        self.setLayout(main_layout)

    def save_data(self):
        data = {sign: self.text_boxes[sign].toPlainText() for sign in SIGNS}

        # Save to rashiphal.json
        save_rashiphal(data)

        # Also save to dataflow.json for Airflow or other use
        try:
            with open("dataflow.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            QMessageBox.information(self, "Saved", "✅ Rashiphala saved to dataflow.json!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save to dataflow.json:\n{str(e)}")

    def refresh_chart(self):
        try:
            fetch_transit_chart()
            html_path = os.path.abspath("templates/transit.html")
            self.web_view.load(QUrl.fromLocalFile(html_path))
            QMessageBox.information(self, "Updated", "♻️ Horoscope refreshed successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error updating chart:\n{str(e)}")
