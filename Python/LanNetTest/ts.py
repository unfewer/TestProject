# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ts.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_st(object):
    def setupUi(self, st):
        st.setObjectName("st")
        st.resize(488, 294)
        self.label = QtWidgets.QLabel(st)
        self.label.setGeometry(QtCore.QRect(80, 250, 111, 31))
        self.label.setLineWidth(2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(st)
        self.pushButton.setGeometry(QtCore.QRect(250, 250, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(st)
        self.graphicsView.setGeometry(QtCore.QRect(60, 20, 361, 201))
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(st)
        QtCore.QMetaObject.connectSlotsByName(st)

    def retranslateUi(self, st):
        _translate = QtCore.QCoreApplication.translate
        st.setWindowTitle(_translate("st", "Dialog"))
        self.label.setText(_translate("st", "TextLabel"))
        self.pushButton.setText(_translate("st", "测试"))
