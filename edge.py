from PyQt6 import QtCore, QtGui, QtWidgets
from PIL import Image
import os
import cv2
from navigate.navigate import Edit
import image_processing
import math
class Ui_edge(object):
    
    def setupUi(self, Form,File,x):
        global val
        val=x
        global wid
        wid = Form
        global pfile
        pfile=File
        global name
        name="Temp/edge.png"
        Form.setObjectName("Form")
        Form.resize(889, 612)
        Form.setStyleSheet("*{border:none;\n"
"background-color:#fff;\n"
"color:#000;}\n"
"#ui{\n"
"background-color:rgb(97, 53, 131)\n"
"}\n"
"QPushButton{\n"
"background-color:#071e26;\n"
"color:#fff}")
        global tname
        tname="Temp/temp.png"
        global isExist
        isExist = os.path.exists(tname)
        if isExist==False:
            img = Image.open(File)
            img = img.save(tname)
        isThere = os.path.exists(name)
        if isThere==False:
            img = Image.open(tname)
            img = img.save(name)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.save = QtWidgets.QPushButton(self.frame)
        self.save.setGeometry(QtCore.QRect(738, 4, 121, 41))
        icon = QtGui.QIcon.fromTheme("document-save")
        self.save.setIcon(icon)
        self.save.setObjectName("save")
        self.save.clicked.connect(self.img_save)
        self.discarded = QtWidgets.QPushButton(self.frame)
        self.discarded.setGeometry(QtCore.QRect(598, 4, 121, 41))
        icon = QtGui.QIcon.fromTheme("edit-clear")
        self.discarded.setIcon(icon)
        self.discarded.setObjectName("discarded")
        self.discarded.clicked.connect(self.img_discard)
        self.heading = QtWidgets.QLabel(self.frame)
        self.heading.setGeometry(QtCore.QRect(6, 6, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(24)
        self.heading.setFont(font)
        self.heading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.heading.setObjectName("heading")
        self.heading.setText("Sharpness")
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_2 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(70, 20, 451, 491))
        self.label.setText("")
        self.label.setObjectName("label")
        
        pixmap = QtGui.QPixmap(tname)
        print(pixmap)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.ui = QtWidgets.QFrame(self.frame_2)
        self.ui.setGeometry(QtCore.QRect(590, 0, 281, 541))
        self.ui.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ui.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ui.setObjectName("ui")
        self.verticalSlider = QtWidgets.QSlider(self.ui)
        self.verticalSlider.setGeometry(QtCore.QRect(130, 50, 20, 231))
        self.verticalSlider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider.valueChanged.connect(self.update_image)
        self.reset = QtWidgets.QPushButton(self.ui)
        self.reset.setGeometry(QtCore.QRect(80, 310, 131, 41))
        icon = QtGui.QIcon.fromTheme("document-open")
        self.reset.setIcon(icon)
        self.reset.setObjectName("reset")
        self.reset.clicked.connect(self.img_reset)
        self.compare = QtWidgets.QPushButton(self.ui)
        self.compare.setGeometry(QtCore.QRect(78, 384, 131, 41))
        icon = QtGui.QIcon.fromTheme("system-reboot")
        self.compare.setIcon(icon)
        self.compare.setObjectName("compare")
        
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def img_reset(self):
        isThere = os.path.exists(name)
        if isThere==True:
            os.remove(name)
    
    def update_image(self, value):
        
        i = cv2.imread(tname)
        value = math.ceil(value*30/200)
        if value==0:
            out = i
        if value%2==0 and value>0:
            value = value+1
        if value!=0:
            out = image_processing.edgeYSobel(i, value)
        
        cv2.imwrite(name, out)
        pixmap = QtGui.QPixmap(name)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
    def img_save(self):
        global val
        val=val+1
        isThere = os.path.exists(name)
        if isThere==True:
            img = Image.open(name)
            img = img.save(tname)
            os.remove(name)
        Edit.img_saved(self,wid,pfile,tname,val)
    def img_discard(self):
        print(val)
        if val==0:
            os.remove(tname)
            print(pfile)
        isThere = os.path.exists(name)
        if isThere==True:
            os.remove(name)
        Edit.img_discarded(self,wid,pfile,tname,val)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.save.setText(_translate("Form", "Save"))
        self.discarded.setText(_translate("Form", "Discard"))
        self.heading.setText(_translate("Form", "Edge Detection"))
        self.reset.setText(_translate("Form", "Reset"))
        self.compare.setText(_translate("Form", "Compare"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_edge()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
