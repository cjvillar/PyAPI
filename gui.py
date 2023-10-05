import sys
import requests
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QSizePolicy,
)


class URLStatusCodeChecker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("URL Status Code Checker")
        self.setGeometry(500, 500, 800, 800)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter URL")

        # set the size policy for the input widget
        self.url_input.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )

        # set the minimum and maximum sizes for the input widget
        self.url_input.setMinimumSize(300, 30)
        self.url_input.setMaximumSize(600, 40)

        layout.addWidget(self.url_input)

        check_button = QPushButton("Check Status Code", self)

        # set the size policy for the check button
        check_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # set the minimum and maximum sizes for the check button
        check_button.setMinimumSize(150, 40)
        check_button.setMaximumSize(200, 50)

        layout.addWidget(check_button)

        self.status_label = QLabel(self)
        layout.addWidget(self.status_label)

        # payload
        self.payload_input = QLineEdit(self)
        self.payload_input.setPlaceholderText("Enter Payload")
        # set the size policy for the input widget
        self.payload_input.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )

        self.payload_input.setMinimumSize(300, 300)
        self.payload_input.setMaximumSize(600, 600)

        layout.addWidget(self.payload_input)


        clear_button = QPushButton("Clear Payload", self)

        # set the size policy for the clear button
        clear_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # set the minimum and maximum sizes for the clear button
        clear_button.setMinimumSize(150, 40)
        clear_button.setMaximumSize(200, 50)

        layout.addWidget(clear_button)

        central_widget.setLayout(layout)

        check_button.clicked.connect(self.check_status_code)
        clear_button.clicked.connect(self.clear_status)

    def check_status_code(self):
        url = self.url_input.text()

        try:
            response = requests.get(url)
            self.status_label.setText(f"Status Code: {response.status_code}")

            if response.status_code <= 200:
                self.status_label.setStyleSheet("color: green;")
            elif response.status_code > 202:
                self.status_label.setStyleSheet("color: red;")
            else:
                self.status_label.setStyleSheet("")

        except Exception as e:
            self.status_label.setText(f"Error: {str(e)}")
            self.status_label.setStyleSheet("color: red;")

    # define a method to clear the status label
    def clear_status(self):
        self.status_label.clear()
        self.payload_input.clear()


def main():
    app = QApplication(sys.argv)
    window = URLStatusCodeChecker()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
