# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Python\RenameTool\RenameTool\ui\renametoolwd.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rentwd(object):
    def setupUi(self, rentwd):
        rentwd.setObjectName("rentwd")
        rentwd.resize(1000, 616)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        rentwd.setFont(font)
        rentwd.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget = QtWidgets.QWidget(rentwd)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.groupBox_SetRule = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_SetRule.setObjectName("groupBox_SetRule")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_SetRule)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabwid = QtWidgets.QTabWidget(self.groupBox_SetRule)
        self.tabwid.setObjectName("tabwid")
        self.tab_Repl = QtWidgets.QWidget()
        self.tab_Repl.setObjectName("tab_Repl")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.tab_Repl)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(self.tab_Repl)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.lineEdit_ReplSrc = QtWidgets.QLineEdit(self.tab_Repl)
        self.lineEdit_ReplSrc.setMaxLength(255)
        self.lineEdit_ReplSrc.setObjectName("lineEdit_ReplSrc")
        self.horizontalLayout_10.addWidget(self.lineEdit_ReplSrc)
        self.label_2 = QtWidgets.QLabel(self.tab_Repl)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.lineEdit_ReplWith = QtWidgets.QLineEdit(self.tab_Repl)
        self.lineEdit_ReplWith.setMaxLength(255)
        self.lineEdit_ReplWith.setObjectName("lineEdit_ReplWith")
        self.horizontalLayout_10.addWidget(self.lineEdit_ReplWith)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_10)
        self.tabwid.addTab(self.tab_Repl, "")
        self.tab_Insert = QtWidgets.QWidget()
        self.tab_Insert.setObjectName("tab_Insert")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.tab_Insert)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.tab_Insert)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.comboBox_InsertWith = QtWidgets.QComboBox(self.tab_Insert)
        self.comboBox_InsertWith.setObjectName("comboBox_InsertWith")
        self.comboBox_InsertWith.addItem("")
        self.comboBox_InsertWith.addItem("")
        self.comboBox_InsertWith.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_InsertWith)
        self.lineEdit_InsertForm = QtWidgets.QLineEdit(self.tab_Insert)
        self.lineEdit_InsertForm.setToolTipDuration(30000)
        self.lineEdit_InsertForm.setMaxLength(255)
        self.lineEdit_InsertForm.setObjectName("lineEdit_InsertForm")
        self.horizontalLayout_11.addWidget(self.lineEdit_InsertForm)
        self.label_4 = QtWidgets.QLabel(self.tab_Insert)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_11.addWidget(self.label_4)
        self.lineEdit_InsertPos = QtWidgets.QLineEdit(self.tab_Insert)
        self.lineEdit_InsertPos.setMaxLength(255)
        self.lineEdit_InsertPos.setObjectName("lineEdit_InsertPos")
        self.horizontalLayout_11.addWidget(self.lineEdit_InsertPos)
        self.horizontalLayout_11.setStretch(0, 5)
        self.horizontalLayout_11.setStretch(1, 15)
        self.horizontalLayout_11.setStretch(2, 45)
        self.horizontalLayout_11.setStretch(3, 5)
        self.horizontalLayout_11.setStretch(4, 17)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_11)
        self.tabwid.addTab(self.tab_Insert, "")
        self.tab_RRepl = QtWidgets.QWidget()
        self.tab_RRepl.setObjectName("tab_RRepl")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.tab_RRepl)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_5 = QtWidgets.QLabel(self.tab_RRepl)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_13.addWidget(self.label_5)
        self.lineEdit_RReplLB = QtWidgets.QLineEdit(self.tab_RRepl)
        self.lineEdit_RReplLB.setMaxLength(255)
        self.lineEdit_RReplLB.setObjectName("lineEdit_RReplLB")
        self.horizontalLayout_13.addWidget(self.lineEdit_RReplLB)
        self.checkBox_IncludeLB = QtWidgets.QCheckBox(self.tab_RRepl)
        self.checkBox_IncludeLB.setObjectName("checkBox_IncludeLB")
        self.horizontalLayout_13.addWidget(self.checkBox_IncludeLB)
        self.line = QtWidgets.QFrame(self.tab_RRepl)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_13.addWidget(self.line)
        self.label_6 = QtWidgets.QLabel(self.tab_RRepl)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_13.addWidget(self.label_6)
        self.lineEdit_RReplRB = QtWidgets.QLineEdit(self.tab_RRepl)
        self.lineEdit_RReplRB.setMaxLength(255)
        self.lineEdit_RReplRB.setObjectName("lineEdit_RReplRB")
        self.horizontalLayout_13.addWidget(self.lineEdit_RReplRB)
        self.checkBox_IncludeRB = QtWidgets.QCheckBox(self.tab_RRepl)
        self.checkBox_IncludeRB.setObjectName("checkBox_IncludeRB")
        self.horizontalLayout_13.addWidget(self.checkBox_IncludeRB)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_7 = QtWidgets.QLabel(self.tab_RRepl)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_12.addWidget(self.label_7)
        self.lineEdit_RReplWith = QtWidgets.QLineEdit(self.tab_RRepl)
        self.lineEdit_RReplWith.setMaxLength(255)
        self.lineEdit_RReplWith.setObjectName("lineEdit_RReplWith")
        self.horizontalLayout_12.addWidget(self.lineEdit_RReplWith)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_16.addLayout(self.verticalLayout_5)
        self.tabwid.addTab(self.tab_RRepl, "")
        self.tab_Regex = QtWidgets.QWidget()
        self.tab_Regex.setObjectName("tab_Regex")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.tab_Regex)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_8 = QtWidgets.QLabel(self.tab_Regex)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_20.addWidget(self.label_8)
        self.lineEdit_RegexPattern = QtWidgets.QLineEdit(self.tab_Regex)
        self.lineEdit_RegexPattern.setObjectName("lineEdit_RegexPattern")
        self.horizontalLayout_20.addWidget(self.lineEdit_RegexPattern)
        self.verticalLayout_14.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_9 = QtWidgets.QLabel(self.tab_Regex)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_21.addWidget(self.label_9)
        self.lineEdit_ReRepl = QtWidgets.QLineEdit(self.tab_Regex)
        self.lineEdit_ReRepl.setObjectName("lineEdit_ReRepl")
        self.horizontalLayout_21.addWidget(self.lineEdit_ReRepl)
        self.label_15 = QtWidgets.QLabel(self.tab_Regex)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_21.addWidget(self.label_15)
        self.lineEdit_ReReplCount = QtWidgets.QLineEdit(self.tab_Regex)
        self.lineEdit_ReReplCount.setObjectName("lineEdit_ReReplCount")
        self.horizontalLayout_21.addWidget(self.lineEdit_ReReplCount)
        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 30)
        self.horizontalLayout_21.setStretch(2, 1)
        self.horizontalLayout_21.setStretch(3, 5)
        self.verticalLayout_14.addLayout(self.horizontalLayout_21)
        self.verticalLayout_15.addLayout(self.verticalLayout_14)
        self.tabwid.addTab(self.tab_Regex, "")
        self.verticalLayout_6.addWidget(self.tabwid)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.comboBox_InExcExt = QtWidgets.QComboBox(self.groupBox_SetRule)
        self.comboBox_InExcExt.setObjectName("comboBox_InExcExt")
        self.comboBox_InExcExt.addItem("")
        self.comboBox_InExcExt.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_InExcExt)
        self.lineEdit_Exts = QtWidgets.QLineEdit(self.groupBox_SetRule)
        self.lineEdit_Exts.setObjectName("lineEdit_Exts")
        self.horizontalLayout_7.addWidget(self.lineEdit_Exts)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox_Word = QtWidgets.QCheckBox(self.groupBox_SetRule)
        self.checkBox_Word.setObjectName("checkBox_Word")
        self.horizontalLayout_8.addWidget(self.checkBox_Word)
        self.label_14 = QtWidgets.QLabel(self.groupBox_SetRule)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)
        self.comboBox_SpInf = QtWidgets.QComboBox(self.groupBox_SetRule)
        self.comboBox_SpInf.setObjectName("comboBox_SpInf")
        self.comboBox_SpInf.addItem("")
        self.comboBox_SpInf.addItem("")
        self.comboBox_SpInf.addItem("")
        self.comboBox_SpInf.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_SpInf)
        self.btn_setrule_clear = QtWidgets.QPushButton(self.groupBox_SetRule)
        self.btn_setrule_clear.setObjectName("btn_setrule_clear")
        self.horizontalLayout_8.addWidget(self.btn_setrule_clear)
        self.btn_SaveToList = QtWidgets.QPushButton(self.groupBox_SetRule)
        self.btn_SaveToList.setObjectName("btn_SaveToList")
        self.horizontalLayout_8.addWidget(self.btn_SaveToList)
        self.horizontalLayout_8.setStretch(0, 15)
        self.horizontalLayout_8.setStretch(1, 3)
        self.horizontalLayout_8.setStretch(2, 5)
        self.horizontalLayout_8.setStretch(3, 5)
        self.horizontalLayout_8.setStretch(4, 10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout_11.addWidget(self.groupBox_SetRule)
        self.groupBox_RuleList = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_RuleList.setObjectName("groupBox_RuleList")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_RuleList)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.list_RulesList = QtWidgets.QListWidget(self.groupBox_RuleList)
        self.list_RulesList.setObjectName("list_RulesList")
        self.horizontalLayout_3.addWidget(self.list_RulesList)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_RL_DelSelected = QtWidgets.QPushButton(self.groupBox_RuleList)
        self.btn_RL_DelSelected.setObjectName("btn_RL_DelSelected")
        self.verticalLayout.addWidget(self.btn_RL_DelSelected)
        self.btn_RL_EditSelected = QtWidgets.QPushButton(
            self.groupBox_RuleList
        )
        self.btn_RL_EditSelected.setObjectName("btn_RL_EditSelected")
        self.verticalLayout.addWidget(self.btn_RL_EditSelected)
        self.btn_RL_ClearAll = QtWidgets.QPushButton(self.groupBox_RuleList)
        self.btn_RL_ClearAll.setObjectName("btn_RL_ClearAll")
        self.verticalLayout.addWidget(self.btn_RL_ClearAll)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3.setStretch(0, 9)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_13.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.groupBox_RuleList)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_9.addWidget(self.label_12)
        self.plainText_ExcludeFolder = QtWidgets.QPlainTextEdit(
            self.groupBox_RuleList
        )
        self.plainText_ExcludeFolder.setContextMenuPolicy(
            QtCore.Qt.NoContextMenu
        )
        self.plainText_ExcludeFolder.setLineWrapMode(
            QtWidgets.QPlainTextEdit.NoWrap
        )
        self.plainText_ExcludeFolder.setObjectName("plainText_ExcludeFolder")
        self.verticalLayout_9.addWidget(self.plainText_ExcludeFolder)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.btn_chexcfile = QtWidgets.QPushButton(self.groupBox_RuleList)
        self.btn_chexcfile.setObjectName("btn_chexcfile")
        self.verticalLayout_10.addWidget(self.btn_chexcfile)
        self.btn_chexcfolder = QtWidgets.QPushButton(self.groupBox_RuleList)
        self.btn_chexcfolder.setObjectName("btn_chexcfolder")
        self.verticalLayout_10.addWidget(self.btn_chexcfolder)
        self.btn_ClearExcfd = QtWidgets.QPushButton(self.groupBox_RuleList)
        self.btn_ClearExcfd.setObjectName("btn_ClearExcfd")
        self.verticalLayout_10.addWidget(self.btn_ClearExcfd)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.horizontalLayout.setStretch(0, 9)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_13.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox_RuleList)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.lineEdit_TGPath = QtWidgets.QLineEdit(self.groupBox_RuleList)
        self.lineEdit_TGPath.setMaxLength(255)
        self.lineEdit_TGPath.setObjectName("lineEdit_TGPath")
        self.horizontalLayout_2.addWidget(self.lineEdit_TGPath)
        self.btn_CTGPath = QtWidgets.QPushButton(self.groupBox_RuleList)
        self.btn_CTGPath.setObjectName("btn_CTGPath")
        self.horizontalLayout_2.addWidget(self.btn_CTGPath)
        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 80)
        self.horizontalLayout_2.setStretch(2, 10)
        self.verticalLayout_13.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_RuleList)
        self.checkBox.setEnabled(False)
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_9.addWidget(self.checkBox)
        self.btn_RL_AddToTaskList = QtWidgets.QPushButton(
            self.groupBox_RuleList
        )
        self.btn_RL_AddToTaskList.setObjectName("btn_RL_AddToTaskList")
        self.horizontalLayout_9.addWidget(self.btn_RL_AddToTaskList)
        self.horizontalLayout_9.setStretch(1, 7)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.verticalLayout_13.setStretch(0, 6)
        self.verticalLayout_13.setStretch(1, 4)
        self.verticalLayout_13.setStretch(2, 1)
        self.verticalLayout_13.setStretch(3, 1)
        self.verticalLayout_11.addWidget(self.groupBox_RuleList)
        self.verticalLayout_11.setStretch(0, 10)
        self.verticalLayout_11.setStretch(1, 50)
        self.horizontalLayout_17.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.groupBox_Tasks = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Tasks.setObjectName("groupBox_Tasks")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_Tasks)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.groupBox_Tasks)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.list_Tasks = QtWidgets.QListWidget(self.groupBox_Tasks)
        self.list_Tasks.setObjectName("list_Tasks")
        self.horizontalLayout_5.addWidget(self.list_Tasks)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_TS_Clear = QtWidgets.QPushButton(self.groupBox_Tasks)
        self.btn_TS_Clear.setObjectName("btn_TS_Clear")
        self.verticalLayout_3.addWidget(self.btn_TS_Clear)
        self.btn_TS_DelSelected = QtWidgets.QPushButton(self.groupBox_Tasks)
        self.btn_TS_DelSelected.setObjectName("btn_TS_DelSelected")
        self.verticalLayout_3.addWidget(self.btn_TS_DelSelected)
        self.btn_TS_MoveUp = QtWidgets.QPushButton(self.groupBox_Tasks)
        self.btn_TS_MoveUp.setObjectName("btn_TS_MoveUp")
        self.verticalLayout_3.addWidget(self.btn_TS_MoveUp)
        self.btn_TS_MoveDown = QtWidgets.QPushButton(self.groupBox_Tasks)
        self.btn_TS_MoveDown.setObjectName("btn_TS_MoveDown")
        self.verticalLayout_3.addWidget(self.btn_TS_MoveDown)
        self.btn_TS_PrevSel = QtWidgets.QPushButton(self.groupBox_Tasks)
        self.btn_TS_PrevSel.setObjectName("btn_TS_PrevSel")
        self.verticalLayout_3.addWidget(self.btn_TS_PrevSel)
        self.btn_TS_PrevAll = QtWidgets.QPushButton(self.groupBox_Tasks)
        self.btn_TS_PrevAll.setEnabled(False)
        self.btn_TS_PrevAll.setObjectName("btn_TS_PrevAll")
        self.verticalLayout_3.addWidget(self.btn_TS_PrevAll)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_12.addWidget(self.groupBox_Tasks)
        self.groupBox_LogNRestore = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_LogNRestore.setObjectName("groupBox_LogNRestore")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(
            self.groupBox_LogNRestore
        )
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.groupBox_LogNRestore)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.list_Logs = QtWidgets.QListWidget(self.groupBox_LogNRestore)
        self.list_Logs.setObjectName("list_Logs")
        self.horizontalLayout_4.addWidget(self.list_Logs)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_LNR_ClearLog = QtWidgets.QPushButton(
            self.groupBox_LogNRestore
        )
        self.btn_LNR_ClearLog.setEnabled(False)
        self.btn_LNR_ClearLog.setObjectName("btn_LNR_ClearLog")
        self.verticalLayout_2.addWidget(self.btn_LNR_ClearLog)
        self.btn_LNR_ViewLog = QtWidgets.QPushButton(self.groupBox_LogNRestore)
        self.btn_LNR_ViewLog.setEnabled(False)
        self.btn_LNR_ViewLog.setObjectName("btn_LNR_ViewLog")
        self.verticalLayout_2.addWidget(self.btn_LNR_ViewLog)
        self.btn_LNR_TryTRestore = QtWidgets.QPushButton(
            self.groupBox_LogNRestore
        )
        self.btn_LNR_TryTRestore.setEnabled(False)
        self.btn_LNR_TryTRestore.setObjectName("btn_LNR_TryTRestore")
        self.verticalLayout_2.addWidget(self.btn_LNR_TryTRestore)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_18.addLayout(self.verticalLayout_7)
        self.verticalLayout_12.addWidget(self.groupBox_LogNRestore)
        self.verticalLayout_12.setStretch(0, 5)
        self.verticalLayout_12.setStretch(1, 5)
        self.horizontalLayout_17.addLayout(self.verticalLayout_12)
        self.horizontalLayout_17.setStretch(0, 50)
        self.horizontalLayout_17.setStretch(1, 45)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_17)
        rentwd.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(rentwd)
        self.statusBar.setObjectName("statusBar")
        rentwd.setStatusBar(self.statusBar)

        self.retranslateUi(rentwd)
        self.tabwid.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(rentwd)
        rentwd.setTabOrder(self.tabwid, self.lineEdit_ReplSrc)
        rentwd.setTabOrder(self.lineEdit_ReplSrc, self.lineEdit_ReplWith)
        rentwd.setTabOrder(self.lineEdit_ReplWith, self.comboBox_InsertWith)
        rentwd.setTabOrder(self.comboBox_InsertWith, self.lineEdit_InsertForm)
        rentwd.setTabOrder(self.lineEdit_InsertForm, self.lineEdit_InsertPos)
        rentwd.setTabOrder(self.lineEdit_InsertPos, self.lineEdit_RReplLB)
        rentwd.setTabOrder(self.lineEdit_RReplLB, self.checkBox_IncludeLB)
        rentwd.setTabOrder(self.checkBox_IncludeLB, self.lineEdit_RReplRB)
        rentwd.setTabOrder(self.lineEdit_RReplRB, self.checkBox_IncludeRB)
        rentwd.setTabOrder(self.checkBox_IncludeRB, self.lineEdit_RReplWith)
        rentwd.setTabOrder(self.lineEdit_RReplWith, self.comboBox_InExcExt)
        rentwd.setTabOrder(self.comboBox_InExcExt, self.lineEdit_Exts)
        rentwd.setTabOrder(self.lineEdit_Exts, self.checkBox_Word)
        rentwd.setTabOrder(self.checkBox_Word, self.comboBox_SpInf)
        rentwd.setTabOrder(self.comboBox_SpInf, self.btn_setrule_clear)
        rentwd.setTabOrder(self.btn_setrule_clear, self.btn_SaveToList)
        rentwd.setTabOrder(self.btn_SaveToList, self.list_RulesList)
        rentwd.setTabOrder(self.list_RulesList, self.btn_RL_DelSelected)
        rentwd.setTabOrder(self.btn_RL_DelSelected, self.btn_RL_EditSelected)
        rentwd.setTabOrder(self.btn_RL_EditSelected, self.btn_RL_ClearAll)
        rentwd.setTabOrder(self.btn_RL_ClearAll, self.plainText_ExcludeFolder)
        rentwd.setTabOrder(self.plainText_ExcludeFolder, self.btn_chexcfile)
        rentwd.setTabOrder(self.btn_chexcfile, self.btn_chexcfolder)
        rentwd.setTabOrder(self.btn_chexcfolder, self.btn_ClearExcfd)
        rentwd.setTabOrder(self.btn_ClearExcfd, self.lineEdit_TGPath)
        rentwd.setTabOrder(self.lineEdit_TGPath, self.btn_CTGPath)
        rentwd.setTabOrder(self.btn_CTGPath, self.btn_RL_AddToTaskList)
        rentwd.setTabOrder(self.btn_RL_AddToTaskList, self.list_Tasks)
        rentwd.setTabOrder(self.list_Tasks, self.btn_TS_MoveUp)
        rentwd.setTabOrder(self.btn_TS_MoveUp, self.btn_TS_MoveDown)
        rentwd.setTabOrder(self.btn_TS_MoveDown, self.btn_TS_PrevSel)
        rentwd.setTabOrder(self.btn_TS_PrevSel, self.btn_TS_PrevAll)
        rentwd.setTabOrder(self.btn_TS_PrevAll, self.list_Logs)
        rentwd.setTabOrder(self.list_Logs, self.btn_LNR_ClearLog)
        rentwd.setTabOrder(self.btn_LNR_ClearLog, self.btn_LNR_ViewLog)
        rentwd.setTabOrder(self.btn_LNR_ViewLog, self.btn_LNR_TryTRestore)

    def retranslateUi(self, rentwd):
        _translate = QtCore.QCoreApplication.translate
        rentwd.setWindowTitle(_translate("rentwd", "批量重命名工具"))
        self.groupBox_SetRule.setTitle(_translate("rentwd", "设定规则"))
        self.label.setText(_translate("rentwd", "替换源:"))
        self.lineEdit_ReplSrc.setStatusTip(
            _translate("rentwd", "必填项，多个替换源请用空格隔开，需要替换空格本身时，请输入 \\k 替代。")
        )
        self.label_2.setText(_translate("rentwd", "替换为:"))
        self.lineEdit_ReplWith.setStatusTip(
            _translate("rentwd", "此处留空则表示将删除前面填写的字符。")
        )
        self.tabwid.setTabText(
            self.tabwid.indexOf(self.tab_Repl), _translate("rentwd", "替换")
        )
        self.label_13.setText(_translate("rentwd", "插入："))
        self.comboBox_InsertWith.setStatusTip(
            _translate("rentwd", "选择插入日期时间、者普通字符或者数字序号。")
        )
        self.comboBox_InsertWith.setItemText(0, _translate("rentwd", "日期时间"))
        self.comboBox_InsertWith.setItemText(1, _translate("rentwd", "普通字符"))
        self.comboBox_InsertWith.setItemText(2, _translate("rentwd", "数字序号"))
        self.lineEdit_InsertForm.setToolTip(
            _translate(
                "rentwd",
                "日期时间：%Y(年)、%y(年,两位数)、%m(月)、%d(日)、%H(时)、%M(分)、%S(秒)，可与普通字符自由组合。\n"
                "数字序号：填写格式：<起始.步长.宽度>，可与普通字符组合，如 <0.1.3>~，则按 000~、001~、002~、003~…添加序号。",
            )
        )
        self.lineEdit_InsertForm.setStatusTip(
            _translate("rentwd", "具体用法请将鼠标置于本文本框上2秒以查看悬浮提示。")
        )
        self.lineEdit_InsertForm.setText(_translate("rentwd", "[%Y-%m-%d]"))
        self.label_4.setText(_translate("rentwd", "插入位置："))
        self.lineEdit_InsertPos.setStatusTip(
            _translate(
                "rentwd",
                "自定义位置支持输入百分比或绝对数值，如果输入的百分比或绝对数值大于文件名长度，则插入到文件名末尾，不支持负数。",
            )
        )
        self.lineEdit_InsertPos.setText(_translate("rentwd", "0.0%"))
        self.tabwid.setTabText(
            self.tabwid.indexOf(self.tab_Insert), _translate("rentwd", "插入")
        )
        self.label_5.setText(_translate("rentwd", "左边界："))
        self.lineEdit_RReplLB.setStatusTip(
            _translate(
                "rentwd",
                "填写想要用来确定左边界的字符串(字符串越长匹配越准确)，左边界可以留空，留空时左边界默认为文件名最前端。",
            )
        )
        self.checkBox_IncludeLB.setStatusTip(
            _translate("rentwd", "是否包括左边界字符。")
        )
        self.checkBox_IncludeLB.setText(_translate("rentwd", "包含"))
        self.label_6.setText(_translate("rentwd", "右边界："))
        self.lineEdit_RReplRB.setStatusTip(
            _translate(
                "rentwd",
                "填写想要用来确定右边界的字符串(字符串越长匹配越准确)，右边界可以留空，留空时右边界默认为文件名末尾(默认不含扩展名)。",
            )
        )
        self.checkBox_IncludeRB.setStatusTip(
            _translate("rentwd", "是否包括右边界字符。")
        )
        self.checkBox_IncludeRB.setText(_translate("rentwd", "包含"))
        self.label_7.setText(_translate("rentwd", "边界内字符替换为："))
        self.lineEdit_RReplWith.setStatusTip(
            _translate("rentwd", "此处留空则表示将删除范围内所有字符，注意此处和左右边界不能同时为空。")
        )
        self.tabwid.setTabText(
            self.tabwid.indexOf(self.tab_RRepl), _translate("rentwd", "范围替换")
        )
        self.label_8.setText(_translate("rentwd", "正则表达式："))
        self.lineEdit_RegexPattern.setStatusTip(
            _translate(
                "rentwd", "此模式需要掌握正则表达式写法。正则表达式匹配时单词模式不生效，可以自己写表达式来匹配单词。"
            )
        )
        self.label_9.setText(_translate("rentwd", "替换为："))
        self.lineEdit_ReRepl.setStatusTip(_translate("rentwd", "要替换掉匹配字符的字符。"))
        self.label_15.setText(_translate("rentwd", "替换次数："))
        self.lineEdit_ReReplCount.setStatusTip(
            _translate("rentwd", "替换次数，0 代表全部替换。")
        )
        self.lineEdit_ReReplCount.setText(_translate("rentwd", "0"))
        self.tabwid.setTabText(
            self.tabwid.indexOf(self.tab_Regex), _translate("rentwd", "正则表达式")
        )
        self.comboBox_InExcExt.setStatusTip(
            _translate("rentwd", "符合后面列出的扩展名的文件，限定只对其起作用或只对其不起作用。")
        )
        self.comboBox_InExcExt.setItemText(0, _translate("rentwd", "指定文件格式"))
        self.comboBox_InExcExt.setItemText(1, _translate("rentwd", "排除文件格式"))
        self.lineEdit_Exts.setStatusTip(
            _translate("rentwd", "此处留空则表示将对所有扩展名的文件进行操作。")
        )
        self.lineEdit_Exts.setPlaceholderText(
            _translate("rentwd", "多个扩展名请用空格隔开，例如：mp3 mp4 mkv。")
        )
        self.checkBox_Word.setStatusTip(
            _translate(
                "rentwd", "单词模式下，如果文件名以单词组成(以空格分开的词，包括中文)，则会按单词进行匹配，不会拆分单词。"
            )
        )
        self.checkBox_Word.setText(_translate("rentwd", "单词模式"))
        self.label_14.setStatusTip(
            _translate("rentwd", "重命名文件时的作用范围，当扩展名中有符合匹配项时是否对扩展名进行操作。")
        )
        self.label_14.setText(_translate("rentwd", "作用范围："))
        self.comboBox_SpInf.setStatusTip(
            _translate("rentwd", "重命名文件时的作用范围，当扩展名中有符合匹配项时是否对扩展名进行操作。")
        )
        self.comboBox_SpInf.setItemText(0, _translate("rentwd", "不含扩展名"))
        self.comboBox_SpInf.setItemText(1, _translate("rentwd", "仅限扩展名"))
        self.comboBox_SpInf.setItemText(2, _translate("rentwd", "全部：独立"))
        self.comboBox_SpInf.setItemText(3, _translate("rentwd", "全部：整体"))
        self.btn_setrule_clear.setStatusTip(
            _translate("rentwd", "重置所有标签页的输入状态。")
        )
        self.btn_setrule_clear.setText(_translate("rentwd", "清空输入"))
        self.btn_SaveToList.setStatusTip(
            _translate("rentwd", "把当前标签页的输入信息打包成一条规则并保存到列表。")
        )
        self.btn_SaveToList.setText(_translate("rentwd", "保存到规则列表"))
        self.groupBox_RuleList.setTitle(_translate("rentwd", "规则列表"))
        self.list_RulesList.setStatusTip(
            _translate(
                "rentwd",
                "用户创建的重命名规则列表，同一规则可以多次与不同文件夹组合加入任务列表，或同一文件夹可以多次组合不同规则加入任务列表。",
            )
        )
        self.btn_RL_DelSelected.setStatusTip(_translate("rentwd", "删除选中的规则。"))
        self.btn_RL_DelSelected.setText(_translate("rentwd", "删除"))
        self.btn_RL_EditSelected.setStatusTip(
            _translate("rentwd", "编辑选中的规则，注意编辑完成后不要忘记重新保存到规则列表。")
        )
        self.btn_RL_EditSelected.setText(_translate("rentwd", "编辑"))
        self.btn_RL_ClearAll.setStatusTip(_translate("rentwd", "清空规则列表。"))
        self.btn_RL_ClearAll.setText(_translate("rentwd", "清空"))
        self.label_12.setText(_translate("rentwd", "排除文件和文件夹:"))
        self.plainText_ExcludeFolder.setStatusTip(
            _translate("rentwd", "要排除的文件和文件夹请输入完整、正确路径，否则排除的文件或文件夹将不生效。")
        )
        self.plainText_ExcludeFolder.setPlaceholderText(
            _translate("rentwd", "填写多个文件或文件夹时请每行填写一个文件或文件夹路径。")
        )
        self.btn_chexcfile.setStatusTip(_translate("rentwd", "选择要排除的文件。"))
        self.btn_chexcfile.setText(_translate("rentwd", "选择文件"))
        self.btn_chexcfolder.setStatusTip(_translate("rentwd", "选择要排除的文件夹。"))
        self.btn_chexcfolder.setText(_translate("rentwd", "选择文件夹"))
        self.btn_ClearExcfd.setStatusTip(
            _translate("rentwd", "清空要排除的文件或文件夹列表。")
        )
        self.btn_ClearExcfd.setText(_translate("rentwd", "清除全部"))
        self.label_11.setStatusTip(_translate("rentwd", "要进行批量重命名操作的文件夹。"))
        self.label_11.setText(_translate("rentwd", "目标文件夹:"))
        self.lineEdit_TGPath.setStatusTip(
            _translate("rentwd", "要进行批量重命名操作的文件夹。")
        )
        self.btn_CTGPath.setStatusTip(
            _translate("rentwd", "选择要进行批量重命名操作的文件夹。")
        )
        self.btn_CTGPath.setText(_translate("rentwd", "…"))
        self.checkBox.setStatusTip(_translate("rentwd", "未完成的功能。"))
        self.checkBox.setText(_translate("rentwd", "深入子目录"))
        self.btn_RL_AddToTaskList.setStatusTip(
            _translate("rentwd", "将规则、排除的文件、文件夹、目标目录打包成一个任务加入到任务列表。")
        )
        self.btn_RL_AddToTaskList.setText(
            _translate("rentwd", "将选中规则+目标+排除组合加入任务")
        )
        self.groupBox_Tasks.setTitle(_translate("rentwd", "任务"))
        self.label_10.setText(_translate("rentwd", "待执行任务 / 执行顺序:"))
        self.list_Tasks.setStatusTip(_translate("rentwd", "等待执行的任务列表。"))
        self.btn_TS_Clear.setStatusTip(_translate("rentwd", "清空任务列表。"))
        self.btn_TS_Clear.setText(_translate("rentwd", "清空任务"))
        self.btn_TS_DelSelected.setStatusTip(_translate("rentwd", "移除选中的任务。"))
        self.btn_TS_DelSelected.setText(_translate("rentwd", "移除任务"))
        self.btn_TS_MoveUp.setStatusTip(_translate("rentwd", "将选中任务上移。"))
        self.btn_TS_MoveUp.setText(_translate("rentwd", "上移"))
        self.btn_TS_MoveDown.setStatusTip(_translate("rentwd", "将选中任务下移。"))
        self.btn_TS_MoveDown.setText(_translate("rentwd", "下移"))
        self.btn_TS_PrevSel.setStatusTip(
            _translate(
                "rentwd",
                "预览选中的任务的执行结果，在弹出的结果预览窗口中决定是否重命名。注意预览结果不代表最终结果，可能正式重命名过程中还会有重命名失败的文件。",
            )
        )
        self.btn_TS_PrevSel.setText(_translate("rentwd", "预览"))
        self.btn_TS_PrevAll.setStatusTip(
            _translate("rentwd", "考虑到可能会有大量文件进行重命名造成性能问题，该功能暂不可用。")
        )
        self.btn_TS_PrevAll.setText(_translate("rentwd", "预览全部"))
        self.groupBox_LogNRestore.setTitle(_translate("rentwd", "记录 / 还原"))
        self.label_3.setText(_translate("rentwd", "重命名记录："))
        self.list_Logs.setStatusTip(
            _translate("rentwd", "重命名后生成的历史记录，可以提供有限的恢复功能。")
        )
        self.btn_LNR_ClearLog.setStatusTip(_translate("rentwd", "删除选中的历史记录。"))
        self.btn_LNR_ClearLog.setText(_translate("rentwd", "删除记录"))
        self.btn_LNR_ViewLog.setStatusTip(_translate("rentwd", "查看选中的历史记录。"))
        self.btn_LNR_ViewLog.setText(_translate("rentwd", "查看记录"))
        self.btn_LNR_TryTRestore.setStatusTip(
            _translate("rentwd", "尝试将上一次重命名操作进行还原。")
        )
        self.btn_LNR_TryTRestore.setText(_translate("rentwd", "尝试还原"))