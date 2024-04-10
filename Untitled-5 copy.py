import sys
import qrcode
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QColorDialog, QFileDialog, QInputDialog, QHBoxLayout, QLineEdit, QStackedWidget
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
        self.originalGreeting = 'Welcome to the QR Code Application'
        self.initUI()
        
        self.qr_generator = QRCodeGenerator()
        self.qr_scanner = QRCodeScanner()
        self.qr_analyzer = QRCodeAnalyzer()

    def initUI(self):
        self.setWindowTitle('QR Code Application')
        self.setGeometry(200, 200, 700, 400)
        self.setFixedSize(self.size())
        
        # Create a stacked widget to switch between the main layout and QR code generation options
        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)
        
        # Setup the main layout
        self.mainWidget = QWidget()
        self.mainLayout = QHBoxLayout(self.mainWidget)
        
        # Setup the QR code generation layout
        self.qrGenWidget = QWidget()
        self.qrGenLayout = QVBoxLayout(self.qrGenWidget)
        
        self.setupMainLayout()
        self.setupQRGenLayout()
        
        self.stackedWidget.addWidget(self.mainWidget)
        self.stackedWidget.addWidget(self.qrGenWidget)

    def setupMainLayout(self):
        self.greeting = QLabel(self.originalGreeting)
        self.greeting.setAlignment(Qt.AlignCenter)
        self.greeting.setWordWrap(True)
        self.greeting.setFixedWidth(250)
        self.mainLayout.addWidget(self.greeting, 1)
        
        # Setup buttons
        buttonsLayout = QVBoxLayout()
        self.generateButton = QPushButton('Generate QR Code')
        self.generateButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        buttonsLayout.addWidget(self.generateButton)
        
        self.scanButton = QPushButton('Scan QR Code')
        self.scanButton.clicked.connect(self.scanQR)
        buttonsLayout.addWidget(self.scanButton)
        
        self.analyzeButton = QPushButton('Analyze QR Code')
        self.analyzeButton.clicked.connect(self.analyzeQR)
        buttonsLayout.addWidget(self.analyzeButton)
        
        self.exitButton = QPushButton('Exit')
        self.exitButton.clicked.connect(self.close)
        buttonsLayout.addWidget(self.exitButton)

        self.generateButton.setFixedSize(300, 65)  # Set fixed size
        self.scanButton.setFixedSize(300, 65)
        self.analyzeButton.setFixedSize(300, 65)
        self.exitButton.setFixedSize(300, 65)
        
        self.mainLayout.addLayout(buttonsLayout)

    def setupQRGenLayout(self):

        qrGenLayout = QHBoxLayout()
        
        qrGenGreeting = QLabel("Enter details to generate QR Code:")
        qrGenGreeting.setAlignment(Qt.AlignCenter)
        qrGenGreeting.setWordWrap(True)
        qrGenGreeting.setFixedWidth(250)
        qrGenLayout.addWidget(qrGenGreeting, 1)
        #self.qrGenWidget.setStyleSheet("background-color: red;")
        
        optionsLayout = QVBoxLayout()
        
        self.urlInput = QLineEdit('Enter URL here')
        optionsLayout.addWidget(self.urlInput)
        
        self.colorButton = QPushButton('Choose Color')
        self.colorButton.clicked.connect(self.chooseColor)
        optionsLayout.addWidget(self.colorButton)
        
        generateButton = QPushButton('Generate')
        generateButton.clicked.connect(self.generateQR)
        optionsLayout.addWidget(generateButton)
        
        cancelButton = QPushButton('Cancel')
        cancelButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        optionsLayout.addWidget(cancelButton)
        
        qrGenLayout.addLayout(optionsLayout, 1)
        #self.qrGenWidget.setStyleSheet("background-color: blue;")

    def chooseColor(self):
        self.color = QColorDialog.getColor(Qt.black, self)

    def generateQR(self):
        url = self.urlInput.text()
        color = self.color.name() if self.color and self.color.isValid() else "black"
        # Assume fileName is determined or asked here
        result = self.qr_generator.generate_qr_code(url, color=color)
        self.displayMessage(result)
        self.stackedWidget.setCurrentIndex(0)
    
    def resetGreeting(self):
        self.greeting.setText(self.originalGreeting)

    def displayMessage(self, message):
        self.greeting.setText(message)
        QTimer.singleShot(3000, self.resetGreeting)

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
