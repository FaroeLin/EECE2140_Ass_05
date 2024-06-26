import sys
import qrcode
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QColorDialog, QFileDialog, QInputDialog, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

class QRCodeGenerator:
    def __init__(self):
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
    def generate_qr_code(self, url, name=None, color="black"):
        self.qr.clear()
        self.qr.add_data(url)
        self.qr.make(fit=True)

        img = self.qr.make_image(fill_color=color, back_color="white")
        img_name = f"{name}.png" if name else "qr_code.png"
        img.save(img_name)
        return f"QR code generated successfully as {img_name}"

class QRCodeAnalyzer:
    def __init__(self):
        self.detector = cv2.QRCodeDetector()

    def image_decode(self, image):
        img = cv2.imread(image)
        data, bbox, _ = self.detector.detectAndDecode(img)
        if bbox is not None and data:
            return "Info stored in QR code: \n" + data
        else:
            return "No QR code detected"

class QRCodeScanner(QRCodeAnalyzer):
    def __init__(self):
        super().__init__()
        self.cap = None

    def camera_decode(self):
        if not self.cap:
            self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            return "Camera device not found or cannot be invoked."

        _, img = self.cap.read()
        data, bbox, _ = self.detector.detectAndDecode(img)
        if bbox is not None and data:
            result = "[+] QR code detected: data: " + data
        else:
            result = "No QR code detected"
        
        self.cap.release()
        self.cap = None
        cv2.destroyAllWindows()
        return result

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        # Initialize other components...
        self.originalGreeting = 'Welcome to the QR Code Application'
        self.greeting.setText(self.originalGreeting)
        
        self.qr_generator = QRCodeGenerator()
        self.qr_scanner = QRCodeScanner()
        self.qr_analyzer = QRCodeAnalyzer()

    def resetGreeting(self):
        self.greeting.setText(self.originalGreeting)

    def displayMessage(self, message):
        self.greeting.setText(message)
        QTimer.singleShot(3000, self.resetGreeting)

    def initUI(self):
        self.setWindowTitle('QR Code Application')
        self.setGeometry(100, 100, 600, 400)
        
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        mainLayout = QHBoxLayout()

        self.setWindowTitle('QR Code Application')
        self.setGeometry(200, 200, 700, 400)  # Set initial size and position
        
        self.setFixedSize(self.size())
        
        # Text on the left
        self.greeting = QLabel('Welcome to the QR Code Application!', self)
        self.greeting.setAlignment(Qt.AlignCenter)
        mainLayout.addWidget(self.greeting, 1)  # The second argument is the stretch factor
        self.greeting.setWordWrap(True)  # Enable word-wrap for the greeting text
        self.greeting.setFixedWidth(250)
        
        # Buttons on the right
        buttonsLayout = QVBoxLayout()
        self.generateButton = QPushButton('Generate QR Code', self)
        self.generateButton.clicked.connect(self.generateQR)
        buttonsLayout.addWidget(self.generateButton)
        
        self.scanButton = QPushButton('Scan QR Code', self)
        self.scanButton.clicked.connect(self.scanQR)
        buttonsLayout.addWidget(self.scanButton)
        
        self.analyzeButton = QPushButton('Analyze QR Code', self)
        self.analyzeButton.clicked.connect(self.analyzeQR)
        buttonsLayout.addWidget(self.analyzeButton)
        
        self.exitButton = QPushButton('Exit', self)
        self.exitButton.clicked.connect(self.close)
        buttonsLayout.addWidget(self.exitButton)

        self.generateButton.setFixedSize(300, 65)  # Set fixed size
        self.scanButton.setFixedSize(300, 65)
        self.analyzeButton.setFixedSize(300, 65)
        self.exitButton.setFixedSize(300, 65)
        
        mainLayout.addLayout(buttonsLayout, 1)  # Adding the buttons layout to the main layout with a stretch factor
        
        self.centralWidget.setLayout(mainLayout)

    def generateQR(self):
        text, ok = QInputDialog.getText(self, 'QR Code Content', 'Enter the content for the QR Code:')
        if ok and text:
            color = QColorDialog.getColor(Qt.black, self).name()
            fileName, _ = QFileDialog.getSaveFileName(self, "Save QR Code", "", "PNG Files (*.png);;All Files (*)")
            if fileName:
                result = self.qr_generator.generate_qr_code(text, fileName, color)
                self.displayMessage(result)  # Use displayMessage instead


    def scanQR(self):
        result = self.qr_scanner.camera_decode()
        self.displayMessage(result)


    def analyzeQR(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open QR Code", "", "Image Files (*.png *.jpg *.bmp);;All Files (*)")
        if fileName:
            result = self.qr_analyzer.image_decode(fileName)
            self.displayMessage(result)

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
