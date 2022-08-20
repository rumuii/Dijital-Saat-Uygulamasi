
from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 305)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(140, 40, 461, 191))
        self.lcdNumber.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0170455, y1:1, x2:1, y2:0, stop:0 rgba(255, 169, 210, 209), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(170, 85, 127);\n"
"\n"
"border-radius: 5px;\n"
"")
        self.lcdNumber.setObjectName("lcdNumber")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber(Form).Filled)
        zamanlayici = QtCore.QTimer(self.lcdNumber)
        zamanlayici.timeout.connect(self.zamanigoster)
        zamanlayici.start(1000)
        self.zamanigoster()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def zamanigoster(self):
        zaman = QtCore.QTime.currentTime()
        metin = zaman.toString('hh:mm')
        print(metin)
        if (zaman.second()%2) == 0:
            metin = metin[:2]+ " " + metin[3:]

        self.lcdNumber.display(metin)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
