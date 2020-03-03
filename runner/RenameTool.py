# coding:utf-8

"""
    版本：0.0.1
    功能：快速批量对文件重命名。
    作者：hrp
"""

import os
import sys

filepath = os.path.dirname(os.path.realpath(__file__))
sys.path = [os.path.dirname(filepath)] + sys.path

import pickle
from Renamer import Task
from PyQt5.QtWidgets import QFileDialog as QFD
from PyQt5.QtWidgets import QMainWindow as QMW
from PyQt5.QtWidgets import QApplication as QAPP
from ui.RenameToolUI import Ui_RenameToolUI as RTUI


class RenameTool(QMW, RTUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(901, 594)

        # 设置文件的路径和规则列表的保存路径以及目标文件夹默认路径。
        self._sfpath = os.path.join(sys.path[0], "settings", "settings.bin")
        self._rulespath = os.path.join(sys.path[0], "settings", "rules.bin")
        self.defaultdir = "."

        self.tasklist, self.packetlist = [], []
        self._connect()
        self._loadsettings()
        self._loadruleslist()
        # self.settip("将鼠标停留在相应位置可查看说明。")

    def _connect(self):
        """
        统一绑定。
        checkBox_Word：       单词模式
        checkBox_IncludeLB：  包含左边界
        checkBox_IncludeRB：  包含右边界
        comboBox_OOEExt：     限定或排除指定扩展名
        comboBox_SpInf：      作用范围是否包含扩展名
        btn_SaveToList：      保存到列表
        btn_RL_DelSelected：  规则列表的删除选中项按钮
        btn_RL_EditSelected： 规则列表中的编辑选中项按钮
        btn_RL_AddToTaskList：“加入待执行”按钮
        comboBox_InsertWith： “插入”下拉单选框
        comboBox_InsertPos：  “插入位置”下拉单选框
        btn_RL_ClearRules：   规则列表的清空按钮
        btn_SetDefaultDir：   “设置默认目标文件”夹按钮
        btn_CTGPath：         规则列表中的“...”按钮
        btn_AT_MoveUp：       任务列表的“上移”按钮
        btn_AT_MoveDown：     任务列表的“下移”按钮
        btn_AT_Clear：        任务列表的“清空”按钮
        btn_AT_DelSelected：  任务列表的“移除”按钮
        btn_AT_PrevNRun：     任务列表的“预览/执行”按钮
        """
        self.checkBox_Word.clicked.connect(self._savesettings)
        self.checkBox_IncludeLB.clicked.connect(self._savesettings)
        self.checkBox_IncludeRB.clicked.connect(self._savesettings)
        self.comboBox_InExcExt.currentIndexChanged.connect(self._savesettings)
        self.comboBox_SpInf.currentIndexChanged.connect(self._savesettings)
        self.btn_SaveToList.clicked.connect(self._addtoruleslist)
        self.btn_RL_DelSelected.clicked.connect(self._rl_delselected)
        self.btn_RL_EditSelected.clicked.connect(self._rl_editselected)
        self.btn_setrule_clear.clicked.connect(self.clearstate)
        self.btn_RL_AddToTaskList.clicked.connect(self._addtotasklist)
        self.comboBox_InsertWith.currentIndexChanged.connect(self._setform)
        self.btn_RL_ClearAll.clicked.connect(self.rl_clear)
        self.btn_SetDefaultDir.clicked.connect(self.setdefaultdir)
        self.btn_CTGPath.clicked.connect(self._chtarget)
        self.btn_AT_MoveUp.clicked.connect(self._taskmoveup)
        self.btn_AT_MoveDown.clicked.connect(self._taskmovedown)
        self.btn_AT_Clear.clicked.connect(self._taskclear)
        self.btn_AT_DelSelected.clicked.connect(self._taskdelselected)
        self.btn_AT_PrevNRun.clicked.connect(self._taskprevnrun)

    def _getsettingstate(self):
        """
        获取需要作为设置来保存状态的控件状态。
        获取的控件状态依次为：
            1.限定扩展名或排除扩展名选择框；
            2.单词模式；
            3.作用范围是否包含扩展名；
            4.范围替换中的是否包含左边界；
            3.范围替换中的是否包含右边界。
        返回值state：字典。
        """
        state = dict()
        state["comboBox_inexcext"] = self.comboBox_InExcExt.currentText()
        state["checkBox_word"] = self.checkBox_Word.isChecked()
        state["comboBox_spinf"] = self.comboBox_SpInf.currentText()
        state["checkBox_inclb"] = self.checkBox_IncludeLB.isChecked()
        state["checkBox_incrb"] = self.checkBox_IncludeRB.isChecked()
        return state

    def _setsettingstate(self, state):
        """
        把从设置中读取的控件状态恢复到相应控件上。
        参数state：字典，各控件状态值。
        依次为：
            1.限定扩展名或排除扩展名选择框；
            2.单词模式；
            3.作用范围是否包含扩展名；
            4.范围替换中的是否包含左边界；
            3.范围替换中的是否包含右边界。
        """
        self.comboBox_InExcExt.setCurrentText(state["comboBox_inexcext"])
        self.checkBox_Word.setChecked(state["checkBox_word"])
        self.comboBox_SpInf.setCurrentText(state["comboBox_spinf"])
        self.checkBox_IncludeLB.setChecked(state["checkBox_inclb"])
        self.checkBox_IncludeRB.setChecked(state["checkBox_incrb"])

    def settip(self, msg=None):
        """
        状态栏提示信息。
        参数msg：要显示的字符串。
        """
        if msg:
            self.statusBar.showMessage(msg)
        else:
            self.statusBar.showMessage(" ")

    def _setform(self):
        """
        设置“插入”标签页的文本框预设内容。
        """
        if self.comboBox_InsertWith.currentIndex() == 0:
            self.lineEdit_InsertForm.setText("[%Y %m %d %H:%M]")
        else:
            self.lineEdit_InsertForm.clear()

    def _loadsettings(self):
        """
        程序运行时从文件加载上次储存的控件状态并恢复。
        """
        try:
            with open(self._sfpath, "rb") as sf:
                settings = pickle.load(sf)
            # 临时添加读取默认目标文件夹设置。
            self.defaultdir = settings["defaultdir"]
            # 恢复各控件状态。
            self._setsettingstate(settings)
        except Exception as err:
            self.settip("设置加载出错:" + str(err))

    def _savesettings(self):
        """
        设置改变时保存控件状态到文件。
        """
        # state：字典，各控件状态。
        state = self._getsettingstate()
        # 临时添加保存默认目标文件夹路径。
        state["defaultdir"] = self.defaultdir
        try:
            with open(self._sfpath, "wb") as sf:
                pickle.dump(state, sf)
        except Exception as err:
            self.settip("设置保存出错:" + str(err))

    def _pktitle(self, pk, num="", wid=0):
        """
        生成数据包(规则)的标题,用于显示在list_RulesList即规则列表中。
        """
        if pk["head"] == "rep":
            repsrc = pk["repsrc"]
            if not (repwith := pk["repwith"]):
                repwith = "无"
            title = f"{num:0>{wid}}替换>>将【{repsrc}】替换成【{repwith}】，"

        elif pk["head"] == "rrep":
            if not (rreplb := pk["rreplb"]):
                rreplb = "无"
            if not (rreprb := pk["rreprb"]):
                rreprb = "无"
            inclb = "包含" if pk["inclb"] else "不含"
            incrb = "包含" if pk["incrb"] else "不含"
            if not (rrepwith := pk["rrepwith"]):
                rrepwith = "无"

            title = (
                    f"{num:0>{wid}}范围>>范围内字符替换成【{rrepwith}】，"
                    + f"左边界【{rreplb}】，右边界【{rreprb}】，【{inclb}】左边界，【{incrb}】右边界，"
            )

        else:
            insertwith = pk["insertwith"]
            form = pk["form"]
            insertpos = (
                str(pk["insertpos"])
                if isinstance(pk["insertpos"], int)
                else (str(pk["insertpos"] * 100) + "%")
            )

            title = (
                f"{num:0>{wid}}插入>>插入【{insertwith}】，字符或格式:【{form}】，位置:【{insertpos}】，"
            )

        if not (excfd := pk["excfd"]):
            excfd = "无"
        else:
            excfd = ",".join(excfd)
        inexcext = pk["inexcext"]
        if not (exts := pk["exts"]):
            exts = "无"
        else:
            exts = " ".join(exts)
        word = "是" if pk["word"] else "否"
        spinf = pk["spinf"]
        if spinf == 0:
            spinf = "不含扩展名"
        elif spinf == 1:
            spinf = "仅限扩展名"
        else:
            spinf = "整个文件名"

        title += f"排除文件夹:【{excfd}】，{inexcext}【{exts}】，单词模式:【{word}】，作用范围:【{spinf}】。"

        return title

    def _getcommon(self):
        """
        获取“设定规则”分组内除了 tabview 以外的其他控件的数据(替换、范围替换、插入三个规则类型都共用的控件)。
        """
        state = dict()
        # 排除的文件夹，简单处理用户输入的文本，提取有效路径。
        excfd = [
            i.strip()
            for i in self.plainText_ExcludeFolder.toPlainText().split("\n")
            if i and (i != "\n")
        ]
        state["excfd"] = [i for i in excfd if os.path.isdir(i)]

        state["inexcext"] = self.comboBox_InExcExt.currentText()

        # 限定或排除的扩展名，简单处理用户输入的文本，提取扩展名。
        exts = [
            i.strip() for i in self.lineEdit_Exts.text().split(" ") if i and (i != " ")
        ]
        state["exts"] = [i if i[0] == "." else "." + i for i in exts]

        state["word"] = self.checkBox_Word.isChecked()
        state["spinf"] = self.comboBox_SpInf.currentText()

        return state

    def _setcommon(self, state):
        """
        设置“设定规则”分组内除了 tabview 以外的其他控件的数据(替换、范围替换、插入三个规则类型都共用的控件)。
        """
        # 首先是排除的文件夹列表文本框，excfd是list。
        if state["excfd"]:
            self.plainText_ExcludeFolder.setPlainText("\n".join(state["excfd"]))
        else:
            self.plainText_ExcludeFolder.clear()
        # 其次是指定或排除扩展名的下拉单选框。
        self.comboBox_InExcExt.setCurrentText(state["inexcext"])
        # 跟在后面的填扩展名的文本框，exts也是list。
        if state["exts"]:
            self.lineEdit_Exts.setText(" ".join(state["exts"]))
        else:
            self.lineEdit_Exts.clear()
        # 单词模式勾选框。
        self.checkBox_Word.setChecked(state["word"])
        # 作用范围下拉单选框。
        self.comboBox_SpInf.setCurrentText(state["spinf"])

    def get_rep(self):
        """
        获取“替换”标签页下的用户输入数据。
        """
        self.settip()
        state = self._getcommon()
        state["head"] = "rep"
        state["repsrc"] = self.lineEdit_RepSrc.text()
        if not state["repsrc"]:
            self.settip("替换源字符不能为空！")
            self.lineEdit_RepSrc.setFocus()
            return False
        state["repwith"] = self.lineEdit_RepWith.text()
        print(state)
        self.packetlist.append(state)
        return True

    def _set_rep(self, state):
        """
        设置“替换”中各控件的状态。
        """
        self.tabwid.setCurrentIndex(0)
        self._setcommon(state)
        if state["repsrc"]:
            self.lineEdit_RepSrc.setText(state["repsrc"])
        else:
            self.lineEdit_RepSrc.clear()
        if state["repwith"]:
            self.lineEdit_RepWith.setText(state["repwith"])
        else:
            self.lineEdit_RepWith.clear()

    def get_rrep(self):
        """
        获取“范围替换”标签页下的用户输入数据。
        """
        self.settip()
        state = self._getcommon()
        state["head"] = "rrep"
        rreplb = self.lineEdit_RRepLB.text()
        rreprb = self.lineEdit_RRepRB.text()
        state["inclb"] = self.checkBox_IncludeLB.isChecked()
        state["incrb"] = self.checkBox_IncludeRB.isChecked()
        rrepwith = self.lineEdit_RRepWith.text()
        if not any((rreplb, rreprb, rrepwith)):
            self.settip("左边界、右边界、替换字符不能同时为空！")
            return False
        state["rreplb"] = rreplb
        state["rreprb"] = rreprb
        state["rrepwith"] = rrepwith
        self.packetlist.append(state)
        return True

    def _set_rrep(self, state):
        """
        设置“范围替换”中各控件状态。
        """
        self.tabwid.setCurrentIndex(1)
        self._setcommon(state)
        if state["rreplb"]:
            self.lineEdit_RRepLB.setText(state["rreplb"])
        else:
            self.lineEdit_RRepLB.clear()
        if state["rreprb"]:
            self.lineEdit_RRepRB.setText(state["rreprb"])
        else:
            self.lineEdit_RRepRB.clear()
        self.checkBox_IncludeLB.setChecked(state["inclb"])
        self.checkBox_IncludeRB.setChecked(state["incrb"])
        if state["rrepwith"]:
            self.lineEdit_RRepWith.setText(state["rrepwith"])
        else:
            self.lineEdit_RRepWith.clear()

    def get_insert(self):
        """
        获取“插入”标签页下的用户输入数据。
        """
        self.settip()
        state = self._getcommon()
        state["head"] = "insert"
        state["insertwith"] = self.comboBox_InsertWith.currentText()
        form = self.lineEdit_InsertForm.text()
        if not form:
            self.settip("请输入要插入的格式!")
            return False
        state["form"] = form
        if not (insertpos := self.lineEdit_InsertPos.text()):
            self.settip("请输入插入位置(百分比或绝对数值)！")
            return False
        if ("%" in insertpos) and (insertpos[-1] == "%"):
            try:
                state["insertpos"] = float(insertpos[:-1]) / 100
            except:
                self.settip("文本插入位置百分比输入有误，请重新输入！")
                return False
        else:
            try:
                state["insertpos"] = int(float(insertpos))
            except:
                self.settip("文本插入绝对位置输入有误，请重新输入！")
                return False
        self.packetlist.append(state)
        return True

    def _set_insert(self, state):
        """
        设置“插入”中各控件状态。
        """
        self.tabwid.setCurrentIndex(2)
        self._setcommon(state)
        self.comboBox_InsertWith.setCurrentText(state["insertwith"])
        if state["form"]:
            self.lineEdit_InsertForm.setText(state["form"])
        else:
            self.lineEdit_InsertForm.clear()
        inspos = state["insertpos"]
        if isinstance(inspos, float):
            self.lineEdit_InsertPos.setText(str(inspos * 100) + "%")
        else:
            self.lineEdit_InsertPos.setText(str(inspos))

    def _addtoruleslist(self):
        """
        根据tabview的标签页位置获取相应页下的用户输入数据并添加到规则列表、保存到文件。
        """
        funlist = [self.get_rep, self.get_rrep, self.get_insert]
        if funlist[self.tabwid.currentIndex()]():
            self.ruleslistupdate()

    def _setstate(self, state):
        """
        参数state: 字典，列表packetlist中之一(保存的各控件状态的字典)。
        根据字典中head设置控件状态。
        """
        if (tmp := state["head"]) == "rep":
            self._set_rep(state)
        elif tmp == "rrep":
            self._set_rrep(state)
        else:
            self._set_insert(state)

    def clearstate(self):
        """
        清空“设定规则”分组的所有文本输入控件的状态。
        """
        self.settip()
        self.lineEdit_RepSrc.clear()
        self.lineEdit_RepWith.clear()
        self.lineEdit_RRepLB.clear()
        self.lineEdit_RRepRB.clear()
        self.lineEdit_RRepWith.clear()
        self.comboBox_InsertWith.setCurrentIndex(0)
        self.lineEdit_InsertForm.setText("[%Y %m %d %H:%M]")
        self.lineEdit_InsertPos.setText("0.0%")
        self.plainText_ExcludeFolder.clear()
        self.comboBox_InExcExt.setCurrentIndex(0)
        self.lineEdit_Exts.clear()
        self.comboBox_SpInf.setCurrentIndex(0)

    def _saveruleslist(self):
        """
        保存规则列表到文件。
        """
        try:
            with open(self._rulespath, "wb") as rsl:
                pickle.dump(self.packetlist, rsl)
        except Exception as err:
            self.settip("规则列表保存出错:" + str(err))

    def _loadruleslist(self):
        """
        读取保存在文件中的规则列表。
        """
        if os.path.exists(self._rulespath):
            try:
                with open(self._rulespath, "rb") as rsl:
                    self.packetlist = pickle.load(rsl)
            except Exception as err:
                self.settip("规则列表载入错误:" + str(err))
                return False
            self.ruleslistupdate()

    def ruleslistupdate(self, ind=None):
        """
        更新规则列表，每次更新都会把规则列表写入文件并保存。
        """
        self.list_RulesList.clear()
        lth = len(self.packetlist)
        wid = len(str(lth)) + 1
        for i in range(lth):
            self.list_RulesList.addItem(
                self._pktitle(self.packetlist[i], str(i + 1) + ".", wid)
            )
        if ind == None:
            if (lth - 1) >= 0:
                self.list_RulesList.setCurrentRow(lth - 1)
        else:
            self.list_RulesList.setCurrentRow(ind)
        self._saveruleslist()

    def tasklistupdate(self):
        """
        更新任务列表。
        """
        self.list_AlcTasks.clear()
        for i in self.tasklist:
            self.list_AlcTasks.addItem(i.title)

    def setdefaultdir(self):
        """
        设置默认目标文件夹。
        """
        dfdir = self._seldir()
        if not dfdir:
            self.settip("未设置默认起始路径。")
            return False
        self.defaultdir = dfdir
        self._savesettings()
        self.settip("默认起始路径设置成功。")

    def _seldir(self):
        """
        选择文件夹。
        """
        dirpath = QFD.getExistingDirectory(self, "选择目标文件夹", self.defaultdir)
        return os.path.realpath(dirpath)

    def _rl_delselected(self):
        """
        获取规则当前选中的项，根据索引删除packetlist相应项并更新列表显示,返回删除的项。
        """
        self.settip()
        ind = self.list_RulesList.currentRow()
        lth = len(self.packetlist)
        if ind == -1:
            if not lth:
                self.settip("规则列表为空！")
            else:
                self.settip("还未选中任何规则！")
            return False
        curit = self.packetlist.pop(ind)
        ind = (ind - 1) if (ind > 0) else (0 if lth > 0 else None)
        self.ruleslistupdate(ind)
        return curit

    def _rl_editselected(self):
        """
        编辑规则列表中选中的项：删除相应项并把该项包含的状态设置到相应控件上。
        """
        if not (curit := self._rl_delselected()):
            return False
        self._setstate(curit)
        return True

    def rl_clear(self):
        """
        清空规则列表
        """
        self.packetlist.clear()
        self.ruleslistupdate()

    def _addtotasklist(self):
        ind = self.list_RulesList.currentRow()
        if ind == -1:
            if not len(self.packetlist):
                self.settip("规则列表为空！")
            else:
                self.settip("还未选中任何规则！")
            return False
        dirpath = self.lineEdit_TGPath.text()
        if (not dirpath) or (not os.path.exists(dirpath)):
            dirpath = self._seldir()
        if not dirpath:
            self.settip("未选择目标文件夹。")
            return False
        self.settip()
        pkdic = dict(self.packetlist[ind])
        self.tasklist.append(
            Task(self._pktitle(pkdic), os.path.realpath(dirpath), pkdic)
        )
        self.tasklistupdate()
        return True

    def _chtarget(self):
        """
        “...”按钮选择路径并显示到“目标文件夹”后的文本框。
        """
        tg = self._seldir()
        if not tg:
            self.settip("没有选择文件夹。")
            return False
        self.lineEdit_TGPath.setText(tg)
        return True

    def _taskmoveup(self):
        """
        把选中任务往上移。
        """
        ind = self.list_AlcTasks.currentRow()
        if ind < 1:
            return False
        self.tasklist[ind - 1], self.tasklist[ind] = self.tasklist[ind], self.tasklist[ind - 1]
        self.tasklistupdate()
        self.list_AlcTasks.setCurrentRow(ind - 1)
        return True

    def _taskmovedown(self):
        """
        把选中任务往下移。
        """
        ind = self.list_AlcTasks.currentRow()
        if (ind == -1) or (ind >= len(self.tasklist) - 1):
            return False
        self.tasklist[ind], self.tasklist[ind + 1] = self.tasklist[ind + 1], self.tasklist[ind]
        self.tasklistupdate()
        self.list_AlcTasks.setCurrentRow(ind + 1)
        return True

    def _taskclear(self):
        """
        清空任务列表。
        """
        self.tasklist.clear()
        self.tasklistupdate()

    def _taskdelselected(self):
        """
        删除选中任务。
        """
        ind = self.list_AlcTasks.currentRow()
        if ind == -1:
            return False
        self.tasklist.pop(ind)
        self.tasklistupdate()
        return True

    def _taskprevnrun(self):
        """
        预览任务执行结果并让用户决定是否执行。
        """
        pass


if __name__ == "__main__":
    app = QAPP(sys.argv)
    ui = RenameTool()
    ui.show()
    sys.exit(app.exec_())
