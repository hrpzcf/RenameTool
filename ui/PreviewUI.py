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
        PreviewUI.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(PreviewUI)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_successful = QtWidgets.QTextEdit(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setUnderline(False)
        self.textEdit_successful.setFont(font)
        self.textEdit_successful.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textEdit_successful.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_successful.setReadOnly(True)
        self.textEdit_successful.setObjectName("textEdit_successful")
        self.horizontalLayout.addWidget(self.textEdit_successful)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textEdit_failed = QtWidgets.QTextEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setUnderline(False)
        self.textEdit_failed.setFont(font)
        self.textEdit_failed.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textEdit_failed.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_failed.setReadOnly(True)
        self.textEdit_failed.setObjectName("textEdit_failed")
        self.horizontalLayout_4.addWidget(self.textEdit_failed)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textEdit_unchanged = QtWidgets.QTextEdit(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setUnderline(False)
        self.textEdit_unchanged.setFont(font)
        self.textEdit_unchanged.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textEdit_unchanged.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_unchanged.setReadOnly(True)
        self.textEdit_unchanged.setObjectName("textEdit_unchanged")
        self.horizontalLayout_5.addWidget(self.textEdit_unchanged)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 2, -1)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_confirm = QtWidgets.QPushButton(self.centralwidget)
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
        self.btn_confirm.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_confirm.setFont(font)
        self.btn_confirm.setObjectName("btn_confirm")
        self.horizontalLayout_2.addWidget(self.btn_confirm)
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 94)
        self.verticalLayout.setStretch(1, 6)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        PreviewUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(PreviewUI)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PreviewUI)

    def retranslateUi(self, PreviewUI):
        _translate = QtCore.QCoreApplication.translate
        PreviewUI.setWindowTitle(_translate("PreviewUI", "结果预览"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("PreviewUI", "可以重命名"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PreviewUI", "无法重命名"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("PreviewUI", "无变化"))
        self.btn_confirm.setText(_translate("PreviewUI", "重命名( 不再确认！)"))
        self.btn_cancel.setText(_translate("PreviewUI", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PreviewUI = QtWidgets.QMainWindow()
    ui = Ui_PreviewUI()
    ui.setupUi(PreviewUI)
    PreviewUI.show()
    sys.exit(app.exec_())
