
# replace <...> with your py file generate from pyuic5 command - without .py-

# It's preferaple to work on MainWindow in qt designer to support layouts
# use Dialog for relatively small windows or windows that don't have too much elements  

import sys


from imageModel import ImageModel
from PyQt5 import QtWidgets , QtGui
from image import Ui_MainWindow
import sys
from  PyQt5.QtWidgets  import QFileDialog ,QVBoxLayout, QPushButton, QLabel,QSlider, QTextEdit
import numpy as np
from PyQt5.QtGui import QPixmap
import cv2 as cv




class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Slider1.setMinimum(0)
        self.ui.Slider1.setMaximum(100)
        self.ui.Slider_2.setMinimum(0)
        self.ui.Slider_2.setMaximum(100)
        self.ui.Slider1.setTickInterval(10)
        self.ui.Slider1.setTickPosition(QSlider.TicksBelow)
        self.ui.Slider_2.setTickInterval(10)
        self.ui.Slider_2.setTickPosition(QSlider.TicksBelow)
        self.ui.load1.clicked.connect(self.getImage)
        self.ui.load2.clicked.connect(self.getImage2)
 
    def getImage(self):
        global fname
        fname = QFileDialog.getOpenFileName(self, 'Open file', '' , "*.jpg *.gif *.png" )[0]
        global img 
        img = cv.imread(fname,0)
    
        pixmap = QPixmap(fname)
        
        self.ui.img1.setPixmap(QPixmap(pixmap))
        
        
    def combox(self):
         comboxes =[self.ui.comboReal1,self.ui.comboReal2,
               self.ui.comboReal3,self.ui.chooseReal4]
         for i in comboxes:
             if self.comboxes[i].currentText() == "Magnitude":
                 self.getMagnitude()
             elif self.comboxes[i].currentText() == "Phase":
                 self.getPhase()
             elif self.comboxes[i].currentText() == "Real" :
                 self.getReal()
             else: 
                self.getImaginary()
    def getImage2(self):
        global fname
        fname = QFileDialog.getOpenFileName(self, 'Open file', '' , "*.jpg *.gif *.png" )[0]
        global img2 
        img2 = cv.imread(fname,0)
        
        pixmap = QPixmap(fname)
        self.ui.img2.setPixmap(QPixmap(pixmap)) 
           
    def getMagnitude(self,string):
        global fshift
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20*np.log(np.abs(fshift))
        
        base_image = QtGui.QImage(magnitude_spectrum.shape[0], magnitude_spectrum.shape[1], QtGui.QImage.Format_ARGB32)
        pixmap = QPixmap(base_image)
        if string == self.ui.comboReal1:
            self.ui.changed_img1.setPixmap(QPixmap(pixmap))
        elif string == self.ui.comboReal2:
            self.ui.changed_img2.setPixmap(QPixmap(pixmap))
        
        
    def getPhase(self,string):
        phase_spectrum = np.angle(fshift)
        pixmap = QPixmap(phase_spectrum)
        self.ui.changed_img1.setPixmap(QPixmap(pixmap))
        base_image = QtGui.QImage(phase_spectrum.shape[0], phase_spectrum.shape[1], QtGui.QImage.Format_ARGB32)
        pixmap = QPixmap(base_image)
        if string == self.ui.comboReal1:
            self.ui.changed_img1.setPixmap(QPixmap(pixmap))
        elif string == self.ui.comboReal2:
            self.ui.changed_img2.setPixmap(QPixmap(pixmap))
          
     
    def getReal(self,string):
        
        real = np.real(fshift)
        pixmap = QPixmap(real)
        if string == self.ui.comboReal1:
            self.ui.changed_img1.setPixmap(QPixmap(pixmap))
        elif string == self.ui.comboReal2:
            self.ui.changed_img2.setPixmap(QPixmap(pixmap))
        
        
    def getImaginary(self,string):
        imag = np.imag(fshift)
        pixmap = QPixmap(imag)
        if string == self.ui.comboReal1:
            self.ui.changed_img1.setPixmap(QPixmap(pixmap))
        elif string == self.ui.comboReal2:
            self.ui.changed_img2.setPixmap(QPixmap(pixmap))
        

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()