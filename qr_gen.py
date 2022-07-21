import sys, pyqrcode, png
from pyqrcode import QRCode
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QDesktopWidget, QGridLayout, QGroupBox, QApplication
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QMessageBox

class QRCodeGenerator(QDialog):
    def __init__(self):
        super().__init__()
        self.WindowGUI()

    def WindowGUI(self):
        self.setFixedSize(400, 200)
        self.setWindowTitle('QRCode Generator')
        self.setWindowIcon(QIcon('app_data/motherlandia.png'))
        self.grid = QGridLayout()
        self.grid.addWidget(self.qrcodeGroupBox())
        self.setLayout(self.grid)
        self.centerUserInterface()
        self.show()
        
    def centerUserInterface(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
     
    def qrcodeGroupBox(self):
        RightGroupBox = QGroupBox()
        
        self.qrcode_information = QLabel('QRCode URL informacije:')
        self.qrcode_information_data = QLineEdit('')
        
        self.qrcode_save = QLabel('Ime datoteke:')
        self.qrcode_save_data = QLineEdit('qr_code_file_name')
        
        buttonSaveProject = QPushButton('Snimi QRCode')
        buttonSaveProject.clicked.connect(self.generateQRCode)
        
        layout = QVBoxLayout()
        layout.addWidget(self.qrcode_information)
        layout.addWidget(self.qrcode_information_data)
        layout.addWidget(self.qrcode_save)
        layout.addWidget(self.qrcode_save_data)
        layout.addWidget(buttonSaveProject)
        layout.addStretch(1)
        RightGroupBox.setLayout(layout)
        
        return RightGroupBox
    
        
    def generateQRCode(self):
        
        if not self.qrcode_information_data.text():
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText('Informacije o URLu ne mogu biti prazne!')
            self.msg.setWindowTitle('QRCode Generator')
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.buttonClicked.connect(self.msg.close)
            self.msg.show()
        else:
            data = self.qrcode_information_data.text()
            file_data = self.qrcode_save_data.text()
            url = pyqrcode.create(data)
            url.svg('qrcodes/' + file_data + '.svg', scale=8)
            url.png('qrcodes/' + file_data + '.png', scale=8)

            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText('QRCode uspiješno snimljen!')
            self.msg.setWindowTitle('QRCode Generator')
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.buttonClicked.connect(self.message_box_success)
            self.msg.show()
            
    def message_box_success(self):
        pass

if __name__ == '__main__':
    mainApplication = QApplication(sys.argv)
    mainWindow = QRCodeGenerator()
    sys.exit(mainApplication.exec_())