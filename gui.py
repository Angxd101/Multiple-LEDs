from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(720, 290, 250, 250)
        self.setWindowTitle("TASK 5.2C")
        self.initUI()
        
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Select the LED you want to light up.")
        self.label.adjustSize()
        
        self.red = QtWidgets.QRadioButton(self)
        self.red.setGeometry(50, 50, 95, 20)
        self.red.setText("RED")
        self.red.toggled.connect(self.redselected)
        
        self.blue = QtWidgets.QRadioButton(self)
        self.blue.setGeometry(50, 70, 95, 20)
        self.blue.setText("BLUE")
        self.blue.toggled.connect(self.blueselected)
        
        self.green = QtWidgets.QRadioButton(self)
        self.green.setGeometry(50, 90, 95, 20)
        self.green.setText("GREEN")
        self.green.toggled.connect(self.greenselected)
        
        self.off = QtWidgets.QRadioButton(self)
        self.off.setGeometry(50, 150, 95, 20)
        self.off.setText("Turn off all LEDs")
        self.off.toggled.connect(self.turn_off_all_LED)
    
    def redselected(self, selected):
        if selected:
            GPIO.output(10, True)
            GPIO.output(11, False)
            GPIO.output(12, False)
            
    def blueselected(self, selected):
        if selected:
            GPIO.output(11, True)
            GPIO.output(10, False)
            GPIO.output(12, False)
            
    def greenselected(self, selected):
        if selected:
            GPIO.output(12, True)
            GPIO.output(11, False)
            GPIO.output(10, False)
    def turn_off_all_LED(self, selected):
        if selected:
            GPIO.output(10, False)
            GPIO.output(11, False)
            GPIO.output(12, False)
            
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()