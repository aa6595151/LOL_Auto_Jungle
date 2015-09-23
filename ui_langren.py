# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from LOL_jungle import Keythread,Mythread
import sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(QtGui.QWidget):
    def  __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./pic/ico.png'))
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setFixedSize(400, 300)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 190, 131, 81))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(120, 10, 241, 151))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 81, 81))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("./pic/web.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 190, 71, 71))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("./pic/web1.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(290, 190, 71, 71))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("./pic/web2.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "LOL狼人刷野外挂", None))
        self.pushButton.setText(_translate("Dialog", "开始刷野", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">英雄联盟狼人刷野外挂</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    -----By<span style=\" font-size:10pt;\"> </span><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Root lee</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.确保使用的英雄是狼人（嗜血猎手）。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.确保已经买了装备 <span style=\" font-weight:600;\">比尔吉沃特弯刀 + 反曲之弓 </span>确保你刷野时不会被野怪打死。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.按下 键盘上的 <span style=\" font-size:12pt; font-weight:600;\">M </span>键可以退出本程序。</p></body></html>", None))
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton.hide)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.subprocess)
       
    def subprocess(self):
        self.keypro = Keythread()
        self.mypro = Mythread()
        print "ssssff"
        self.keypro.start()
        print "after start"
        self.mypro.start()
        self.connect(self.keypro, QtCore.SIGNAL("clos"), QtGui.qApp,QtCore.SLOT('quit()'))
app = QtGui.QApplication(sys.argv)
qb = Ui_Dialog()
qb.show()
#qb.subprocess()
sys.exit(app.exec_())
