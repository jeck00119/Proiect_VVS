# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import subprocess
import sys

import requests
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QRadioButton, QSpinBox


class WebServerUI(QWidget):
    # @profile()
    def __init__(self):
        super().__init__()
        self.result = None
        self.status = None

        self.port_label = QLabel()

        self.port_label.setText("Port Select:")
        self.port_label.setFont(QFont('Arial', 13, QFont.Bold))

        self.site_label = QLabel()
        self.site_label.setOpenExternalLinks(True)
        self.site_label.setFont(QFont('Arial', 13, QFont.Bold))
        self.site_label.setAlignment(QtCore.Qt.AlignCenter)
        self.site_label.setVisible(False)

        self.maintenance = QRadioButton("Maintenance")
        self.maintenance.setFont(QFont('Arial', 13, QFont.Bold))

        self.portInput = QSpinBox(self)
        self.portInput.setRange(100, 65535)
        self.portInput.setValue(5000)
        self.portInput.setFont(QFont("Arial", 12, QFont.Bold))
        self.portInput.setStyleSheet("background-color : white")

        self.startButton = QPushButton("Start")
        self.startButton.setFont(QFont('Arial', 14, QFont.Bold))
        self.startButton.setStyleSheet("background-color : green")
        self.startButton.styleSheet()
        self.stopButton = QPushButton("Stop")
        self.stopButton.setFont(QFont('Arial', 14, QFont.Bold))
        self.stopButton.setStyleSheet("background-color : grey")

        self.setGeometry(50, 50, 300, 200)
        self.setWindowTitle("Web Server UI")
        self.setStyleSheet("background-color : #badeff")

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.startButton)
        self.layout.addWidget(self.stopButton)
        self.layout.addWidget(self.port_label)
        self.layout.addWidget(self.portInput)
        self.layout.addWidget(self.maintenance)
        self.layout.addWidget(self.site_label)
        self.setLayout(self.layout)

        self.startButton.clicked.connect(self.start_app)
        self.stopButton.clicked.connect(self.stop_app)
        self.maintenance.toggled['bool'].connect(self.maintenance_mode)

        self.show()

    def maintenance_mode(self):

        try:
            if self.portInput.text() == '':
                requests.get('http://127.0.0.1:' + '5000' + '/maintenance')
                if self.maintenance.isChecked():
                    self.portInput.setReadOnly(True)

            else:
                requests.get('http://127.0.0.1:' + self.portInput.text() + '/maintenance')

                if self.maintenance.isChecked():
                    self.portInput.setReadOnly(True)

        except:
            self.maintenance.setChecked(False)

    def start_app(self, ):
        if self.status != 1:
            self.result = subprocess.Popen(['python', 'webserver.py', self.portInput.text()], stdout=subprocess.PIPE,
                                           shell=True)
            self.portInput.setReadOnly(True)
            self.startButton.setStyleSheet("background-color : yellow")
            self.stopButton.setStyleSheet("background-color : #fc4503")
            self.site_label.setText("<a href=\"http://127.0.0.1:" + self.portInput.text() + "\">'http://127.0.0.1:" + self.portInput.text() + "'</a>")
            self.site_label.setVisible(True)
            self.status = 1

    def stop_app(self):
        try:
            subprocess.Popen(['taskkill', '/F', '/T', '/PID', str(self.result.pid)])
            self.site_label.setVisible(False)
            if not self.maintenance.isChecked():
                self.portInput.setReadOnly(False)
            else:
                self.maintenance.setChecked(False)
            self.startButton.setStyleSheet("background-color : green")
            self.stopButton.setStyleSheet("background-color : grey")
            self.status = 0

        except:
            pass

    def closeEvent(self, event):
        try:
            subprocess.Popen(['taskkill', '/F', '/T', '/PID', str(self.result.pid)])
            event.accept()
        except:
            event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WebServerUI()
    ex.show()
    sys.exit(app.exec_())
