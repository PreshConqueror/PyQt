# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created: Sun Apr 26 14:05:46 2020
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.Name = QtGui.QLabel(Dialog)
        self.Name.setGeometry(QtCore.QRect(40, 120, 46, 13))
        self.Name.setObjectName(_fromUtf8("Name"))
        self.clear = QtGui.QLineEdit(Dialog)
        self.clear.setGeometry(QtCore.QRect(100, 120, 113, 20))
        self.clear.setText(_fromUtf8(""))
        self.clear.setObjectName(_fromUtf8("clear"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 160, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.Name.setText(_translate("Dialog", "TextLabel", None))
        self.pushButton.setText(_translate("Dialog", "clear", None))

