# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'directory_porter.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 160)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(480, 160))
        MainWindow.setMaximumSize(QtCore.QSize(480, 160))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_selectSource = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_selectSource.setObjectName("pushButton_selectSource")
        self.gridLayout.addWidget(self.pushButton_selectSource, 0, 2, 1, 1)
        self.pushButton_selectTarget = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_selectTarget.setObjectName("pushButton_selectTarget")
        self.gridLayout.addWidget(self.pushButton_selectTarget, 1, 2, 1, 1)
        self.label_target = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_target.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_target.setObjectName("label_target")
        self.gridLayout.addWidget(self.label_target, 1, 0, 1, 1)
        self.lineEdit_source = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_source.setObjectName("lineEdit_source")
        self.gridLayout.addWidget(self.lineEdit_source, 0, 1, 1, 1)
        self.lineEdit_target = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_target.setObjectName("lineEdit_target")
        self.gridLayout.addWidget(self.lineEdit_target, 1, 1, 1, 1)
        self.label_source = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_source.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_source.setObjectName("label_source")
        self.gridLayout.addWidget(self.label_source, 0, 0, 1, 1)
        self.pushButton_execute = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_execute.sizePolicy().hasHeightForWidth())
        self.pushButton_execute.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_execute.setFont(font)
        self.pushButton_execute.setAutoDefault(False)
        self.pushButton_execute.setObjectName("pushButton_execute")
        self.gridLayout.addWidget(self.pushButton_execute, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文件夹迁移"))
        self.pushButton_selectSource.setText(_translate("MainWindow", "选择文件夹"))
        self.pushButton_selectTarget.setText(_translate("MainWindow", "选择文件夹"))
        self.label_target.setText(_translate("MainWindow", "目标文件夹: "))
        self.label_source.setText(_translate("MainWindow", "源文件夹: "))
        self.pushButton_execute.setText(_translate("MainWindow", "执行文件夹迁移"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
