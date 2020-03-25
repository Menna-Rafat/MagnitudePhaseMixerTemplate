
# replace <...> with your py file generate from pyuic5 command - without .py-

# It's preferaple to work on MainWindow in qt designer to support layouts
# use Dialog for relatively small windows or windows that don't have too much elements  

import sys


from imageModel import ImageModel
from PyQt5 import QtWidgets , QtGui
from image import Ui_MainWindow
import sys
from  PyQt5.QtWidgets  import QFileDialog ,QVBoxLayout, QPushButton, QLabel, QTextEdit
import numpy as np
from PyQt5.QtGui import QPixmap
import cv2 as cv




class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.data=[]
        self.y=[]
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
      
 
    def getImage(self):
        global fname
        fname = QFileDialog.getOpenFileName(self, 'Open file', '' , "*.jpg *.gif *.png" )[0]
        global img , base_image
        img = cv.imread(fname,0)
        dimensions = img.shape
        pixmap = QPixmap(fname)
        base_image = QtGui.QImage(dimensions[0], dimensions[1], QtGui.QImage.Format_ARGB32)
        self.ui.img1.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(), pixmap.height())
        
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
           
    def getMagnitude(self):
        global fshift
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20*np.log(np.abs(fshift))
        
        base_image = QtGui.QImage(magnitude_spectrum.shape[0], magnitude_spectrum.shape[1], QtGui.QImage.Format_ARGB32)
        pixmap = QPixmap(base_image)
        self.ui.changed_img1.setPixmap(QPixmap(pixmap))
        
    def getPhase(self):
        phase_spectrum = np.angle(fshift)
        pixmap = QPixmap(phase_spectrum)
        self.ui.changed_img1.setPixmap(QPixmap(pixmap))
        base_image = QtGui.QImage(phase_spectrum.shape[0], phase_spectrum.shape[1], QtGui.QImage.Format_ARGB32)
        pixmap = QPixmap(base_image)
        self.ui.changed_img1.setPixmap(QPixmap(pixmap))  
     
    def getReal(self):
        
        real = np.real(fshift)
        pixmap = QPixmap(real)
        self.ui.changed_img1.setPixmap(QPixmap(pixmap))
        
    def getImaginary(self):
        imag = np.imag(fshift)
        pixmap = QPixmap(imag)
        self.ui.changed_img1.setPixmap(QPixmap(pixmap))

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