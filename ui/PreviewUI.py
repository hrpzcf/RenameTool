# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PreviewUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PreviewUI(object):
    def setupUi(self, PreviewUI):
        PreviewUI.setObjectName("PreviewUI")
        PreviewUI.setWindowModality(QtCore.Qt.ApplicationModal)
        PreviewUI.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(PreviewUI)
        self.centralwidget.setObjectName("centralwidget")
        # self.centralwidget = QtWidgets.QWidget(self.centralwidget)
        # self.centralwidget.setGeometry(QtCore.QRect(0, 0, 641, 481))
        # self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setUnderline(False)
        self.textEdit.setFont(font)
        self.textEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 94)
        self.verticalLayout.setStretch(1, 6)
        PreviewUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(PreviewUI)
        QtCore.QMetaObject.connectSlotsByName(PreviewUI)

    def retranslateUi(self, PreviewUI):
        _translate = QtCore.QCoreApplication.translate
        PreviewUI.setWindowTitle(_translate("PreviewUI", "结果预览"))
        self.pushButton.setText(_translate("PreviewUI", "执行"))
        self.pushButton_2.setText(_translate("PreviewUI", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PreviewUI = QtWidgets.QMainWindow()
    ui = Ui_PreviewUI()
    ui.setupUi(PreviewUI)
    PreviewUI.show()
    sys.exit(app.exec_())
