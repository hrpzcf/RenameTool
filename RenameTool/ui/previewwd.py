# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Python\RenameTool\RenameTool\ui\previewwd.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_prevwd(object):
    def setupUi(self, prevwd):
        prevwd.setObjectName("prevwd")
        prevwd.setWindowModality(QtCore.Qt.ApplicationModal)
        prevwd.resize(800, 500)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        prevwd.setFont(font)
        self.centralwidget = QtWidgets.QWidget(prevwd)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_successful = QtWidgets.QTextEdit(self.tab_1)
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
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush
        )
        self.btn_confirm.setPalette(palette)
        self.btn_confirm.setObjectName("btn_confirm")
        self.horizontalLayout_2.addWidget(self.btn_confirm)
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 94)
        self.verticalLayout.setStretch(1, 6)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        prevwd.setCentralWidget(self.centralwidget)

        self.retranslateUi(prevwd)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(prevwd)

    def retranslateUi(self, prevwd):
        _translate = QtCore.QCoreApplication.translate
        prevwd.setWindowTitle(_translate("prevwd", "重命名结果预览"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_1), _translate("prevwd", "可以重命名")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2), _translate("prevwd", "无法重命名")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3), _translate("prevwd", "无变化")
        )
        self.btn_confirm.setText(_translate("prevwd", "重命名( 不再确认 )"))
        self.btn_cancel.setText(_translate("prevwd", "取消"))
