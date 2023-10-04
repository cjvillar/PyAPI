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
)


class URLStatusCodeChecker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("URL Status Code Checker")
        self.setGeometry(500, 500, 1000, 800) #(x,y ,width, height)

        # Create a central widget and a layout for it
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Create a QLineEdit for entering the URL
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter URL")
        layout.addWidget(self.url_input)

        # Create a QPushButton to check the status code
        check_button = QPushButton("Check Status Code", self)
        layout.addWidget(check_button)

        # Create a QLabel to display the status code
        self.status_label = QLabel(self)
        layout.addWidget(self.status_label)

        central_widget.setLayout(layout)

        # Connect the button click event to the function for checking the status code
        check_button.clicked.connect(self.check_status_code)

    def check_status_code(self):
        # Get the URL from the input field
        url = self.url_input.text()

        try:
            # Send a GET request to the URL
            response = requests.get(url)

            # Update the status label with the status code
            self.status_label.setText(f"Status Code: {response.status_code}")

            # Set the text color for easy status code
            if response.status_code <= 200:
                self.status_label.setStyleSheet("color: green;")

            elif response.status_code > 202:
                self.status_label.setStyleSheet("color: red;")

            else:
                self.status_label.setStyleSheet("")  # Reset the style

        except Exception as e:
            # Handle any exceptions, e.g., network errors or invalid URLs
            self.status_label.setText(f"Error: {str(e)}")
            self.status_label.setStyleSheet("color: red;")  # Set text color to red


def main():
    app = QApplication(sys.argv)
    window = URLStatusCodeChecker()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
