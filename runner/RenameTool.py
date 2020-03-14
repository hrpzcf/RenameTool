# coding:utf-8

# 版本：0.0.1
# 功能：快速批量对文件重命名
# 作者：hrp

import os
import sys

filepath = os.path.dirname(os.path.realpath(__file__))
sys.path = [os.path.dirname(filepath)] + sys.path

import pickle
import re
from copy import deepcopy
from PyQt5.QtWidgets import QApplication as QAPP
from PyQt5.QtWidgets import QFileDialog as QFD
from PyQt5.QtWidgets import QMainWindow as QMW
from Renamer import Task
from ui.RenameToolUI import Ui_RenameToolUI as RTUI
from ui.PreviewUI import Ui_PreviewUI as PUI


class RenameTool(QMW, RTUI):
    ''' RnameTool的主模块。
    '''

    def __init__(self):
        # 设置文件的路径和规则列表的保存路径以及目标文件夹默认路径。
        dir_logs = os.path.join(sys.path[0], 'logs')
        dir_sets = os.path.join(sys.path[0], 'settings')
        for dirs in (dir_sets, dir_logs):
            if not os.path.exists(dirs):
                try:
                    os.mkdir(dirs)
                except:
                    exit(1)
            elif not os.path.isdir(dirs):
                exit(1)
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(901, 594)
        self._rulespath = os.path.join(dir_sets, 'rules.bin')
        self._setspath = os.path.join(dir_sets, 'settings.bin')
        self.UNUSABLE = set(r"\/?:*'><|")
        self._task_current = None
        self._tasklist = list()
        self._packetlist = list()
        self._settingstate = dict()
        self._defaultdir = os.path.realpath('.')
        self._loadsettings()
        self._signal_slotfunc()

    def closeEvent(self, *args, **kwargs):
        self._savesettings()

    def _signal_slotfunc(self):
        ''' 统一绑定各种控件信号与槽函数。
             1.checkBox_Word：       单词模式
             2.checkBox_IncludeLB：  包含左边界
             3.checkBox_IncludeRB：  包含右边界
             4.comboBox_OOEExt：     限定或排除指定扩展名
             5.comboBox_SpInf：      作用范围是否包含扩展名
             6.btn_SaveToList：      保存到列表
             7.btn_RL_DelSelected：  规则列表的删除选中项按钮
             8.btn_RL_EditSelected： 规则列表中的编辑选中项按钮
             9.btn_RL_AddToTaskList：“加入待执行”按钮
            10.comboBox_InsertWith： “插入”下拉单选框
            11.comboBox_InsertPos：  “插入位置”下拉单选框
            12.btn_RL_ClearRules：   规则列表的清空按钮
            13.btn_SetDefaultDir：   “设置默认目标文件”夹按钮
            14.btn_CTGPath：         规则列表中的“...”按钮
            15.btn_TS_MoveUp：       任务列表的“上移”按钮
            16.btn_TS_MoveDown：     任务列表的“下移”按钮
            17.btn_TS_Clear：        任务列表的“清空”按钮
            18.btn_TS_DelSelected：  任务列表的“移除”按钮
            19.btn_TS_PrevSel：      任务列表的“预览选中”按钮
        '''
        self.checkBox_Word.clicked.connect(
            self._getsettingstate)
        self.checkBox_IncludeLB.clicked.connect(
            self._getsettingstate)
        self.checkBox_IncludeRB.clicked.connect(
            self._getsettingstate)
        self.comboBox_InExcExt.currentIndexChanged.connect(
            self._getsettingstate)
        self.comboBox_SpInf.currentIndexChanged.connect(
            self._getsettingstate)
        self.btn_SaveToList.clicked.connect(
            self._addtoruleslist)
        self.btn_RL_DelSelected.clicked.connect(
            self._rl_delselected)
        self.btn_RL_EditSelected.clicked.connect(
            self._rl_editselected)
        self.btn_setrule_clear.clicked.connect(
            self.clearstate)
        self.btn_RL_AddToTaskList.clicked.connect(
            self._addtotasklist)
        self.comboBox_InsertWith.currentIndexChanged.connect(
            self._setform)
        self.btn_RL_ClearAll.clicked.connect(
            self._rl_clear)
        self.btn_SetDefaultDir.clicked.connect(
            self.setdefaultdir)
        self.btn_CTGPath.clicked.connect(
            self._dptarget)
        self.btn_TS_MoveUp.clicked.connect(
            self._taskmoveup)
        self.btn_TS_MoveDown.clicked.connect(
            self._taskmovedown)
        self.btn_TS_Clear.clicked.connect(
            self._taskclear)
        self.btn_TS_DelSelected.clicked.connect(
            self._taskdelselected)
        self.btn_TS_PrevSel.clicked.connect(
            self._task_prev_sel)

    def _getsettingstate(self):
        ''' 获取需要保存状态的常用控件状态值。
            _settingstate：字典，各常用控件状态值。
            获取的控件状态依次为：
                1.选择目标文件夹时的默认起始路径。
                2.限定扩展名或排除扩展名选择框；
                3.单词模式；
                4.作用范围是否包含扩展名；
                5.范围替换中的是否包含左边界；
                6.范围替换中的是否包含右边界；
                7.目标文件夹。
        '''
        self._settingstate['defaultdir'] \
            = self._defaultdir
        self._settingstate['comboBox_inexcext'] \
            = self.comboBox_InExcExt.currentText()
        self._settingstate['checkBox_word'] \
            = self.checkBox_Word.isChecked()
        self._settingstate['comboBox_spinf'] \
            = self.comboBox_SpInf.currentText()
        self._settingstate['checkBox_inclb'] \
            = self.checkBox_IncludeLB.isChecked()
        self._settingstate['checkBox_incrb'] \
            = self.checkBox_IncludeRB.isChecked()

    def _setsettingstate(self):
        ''' 把从设置中读取的控件状态恢复到相应控件上。
            _settingstate：字典，各常用控件状态值。
            依次为：
                1.选择目标文件夹时的默认起始路径。
                2.限定扩展名或排除扩展名选择框；
                3.单词模式；
                4.作用范围是否包含扩展名；
                5.范围替换中的是否包含左边界；
                6.范围替换中的是否包含右边界；
                7.目标文件夹。
        '''
        try:
            self._defaultdir = \
                self._settingstate['defaultdir']
            self.comboBox_InExcExt.setCurrentText(
                self._settingstate['comboBox_inexcext'])
            self.checkBox_Word.setChecked(
                self._settingstate['checkBox_word'])
            self.comboBox_SpInf.setCurrentText(
                self._settingstate['comboBox_spinf'])
            self.checkBox_IncludeLB.setChecked(
                self._settingstate['checkBox_inclb'])
            self.checkBox_IncludeRB.setChecked(
                self._settingstate['checkBox_incrb'])
            self.lineEdit_TGPath.setText(
                self._settingstate['defaultdir'])
        except:
            pass

    def _loadsettings(self):
        ''' 程序运行时从文件加载上次储存的控件状态和规则列表并恢复、刷新。'''
        if os.path.exists(self._setspath):
            try:
                with open(self._setspath, 'rb') as sf:
                    self._settingstate = pickle.load(sf)
                self._setsettingstate()
            except Exception as err:
                self.settip('设置加载出错:' + str(err))
        # 读取规则列表并刷新。
        if os.path.exists(self._rulespath):
            try:
                with open(self._rulespath, 'rb') as rsl:
                    self._packetlist = pickle.load(rsl)
                    self.ruleslistupdate()
            except Exception as err:
                self.settip('规则列表载入错误:' + str(err))

    def _savesettings(self):
        ''' 设置改变时保存控件状态到文件。'''
        # _settingstate：字典，各常用控件状态值，详见 getsettingstate 函数。
        try:
            with open(self._setspath, 'wb') as sf:
                pickle.dump(self._settingstate, sf)
        except Exception as err:
            self.settip('设置保存出错:' + str(err))
        # 保存规则列表到文件。_packetlist：规则列表。
        try:
            with open(self._rulespath, 'wb') as rsl:
                pickle.dump(self._packetlist, rsl)
        except Exception as err:
            self.settip('规则列表保存出错:' + str(err))

    def settip(self, msg=None):
        ''' 状态栏提示信息。
            参数msg：要显示的字符串。
        '''
        if msg:
            self.statusBar.showMessage(msg)
        else:
            self.statusBar.showMessage(' ')

    def _setform(self):
        ''' 设置“插入”标签页的文本框预设内容。'''
        if self.comboBox_InsertWith.currentIndex() == 0:
            self.lineEdit_InsertForm.setText('[%Y-%m-%d]')
        else:
            self.lineEdit_InsertForm.clear()

    def _pktitle(self, pk, num='', wid=0):
        ''' 生成数据包(规则)的标题,用于显示在list_RulesList即规则列表中。'''
        if pk['head'] == 'repl':
            replsrcs = '、'.join(pk['replsrcs'])
            if not (replwith := pk['replwith']):
                replwith = '无'
            title = (f'{num:0>{wid}}替换：将 < {replsrcs} > '
                     f'替换成 < {replwith} >，')
        elif pk['head'] == 'rrepl':
            if not (rrepllb := pk['rrepllb']):
                rrepllb = '无'
            if not (rreplrb := pk['rreplrb']):
                rreplrb = '无'
            inclb = '包含' if pk['inclb'] else '不含'
            incrb = '包含' if pk['incrb'] else '不含'
            if not (rreplwith := pk['rreplwith']):
                rreplwith = '无'
            title = (f'{num:0>{wid}}范围：范围内替换成 < {rreplwith} >，'
                     f'左边界 < {rrepllb} >，右边界 < {rreplrb} >，'
                     f'< {inclb} > 左边界，< {incrb} > 右边界，')
        elif pk['head'] == 'insert':
            insertwith = pk['insertwith']
            form = pk['form']
            insertpos = (
                str(pk['insertpos'])
                if isinstance(pk['insertpos'], int)
                else (str(pk['insertpos'] * 100) + '%'))
            title = (f'{num:0>{wid}}插入：插入 < {insertwith} >，'
                     f'字符或格式: < {form} >，位置: < {insertpos} >，')
        if not (excfd := pk['excfd']):
            excfd = '无'
        else:
            excfd = '，'.join(excfd)
        inexcext = pk['inexcext']
        if not (exts := pk['exts']):
            exts = '无'
        else:
            exts = ' '.join(exts)
        word = '是' if pk['word'] else '否'
        spinf = pk['spinf']
        title += (f'排除文件夹: < {excfd} >，{inexcext} < {exts} >，'
                  f'单词模式: < {word} >，作用范围: < {spinf} >')
        return title

    def _getcommon(self):
        ''' 获取“设定规则”分组内除了 tabview 以外的其他控件的数据
        (替换、范围替换、插入三个规则类型都共用的控件)。
        '''
        state = dict()
        # 排除的文件夹，简单处理用户输入的文本，提取有效路径
        excfd = [
            i.strip()
            for i in self.plainText_ExcludeFolder.toPlainText().split('\n')
            if i and (i != '\n')]
        state['excfd'] = [i for i in excfd if os.path.isdir(i)]
        state['inexcext'] = self.comboBox_InExcExt.currentText()
        # 限定或排除的扩展名，简单处理用户输入的文本，提取扩展名
        exts = [
            i.strip() for i in self.lineEdit_Exts.text().split(' ')
            if i and (i != ' ')]
        state['exts'] = [i if i[0] == '.' else '.' + i for i in exts]
        state['word'] = self.checkBox_Word.isChecked()
        state['spinf'] = self.comboBox_SpInf.currentText()
        return state

    def _setcommon(self, state):
        ''' 设置“设定规则”分组内除了 tabview 以外的其他控件的数据
        (替换、范围替换、插入三个规则类型都共用的控件)。
        '''
        try:
            # 指定或排除扩展名的下拉单选框
            self.comboBox_InExcExt.setCurrentText(state['inexcext'])
            # 后面的填写扩展名的文本框，exts也是list
            if state['exts']:
                self.lineEdit_Exts.setText(' '.join(state['exts']))
            else:
                self.lineEdit_Exts.clear()
            # 单词模式勾选框
            self.checkBox_Word.setChecked(state['word'])
            # 作用范围下拉单选框
            self.comboBox_SpInf.setCurrentText(state['spinf'])
            # 排除的文件夹列表文本框，excfd是list
            if state['excfd']:
                self.plainText_ExcludeFolder.setPlainText(
                    '\n'.join(state['excfd']))
            else:
                self.plainText_ExcludeFolder.clear()
        except Exception as err:
            self.settip('设置控件时出错：' + str(err))

    def get_repl(self):
        ''' 获取“替换”标签页下的用户输入数据。'''
        self.settip()
        state = self._getcommon()
        state['head'] = 'repl'
        replsrcs = [i for i in self.lineEdit_RepSrc.text().split(' ') if i]
        if not replsrcs:
            self.settip('替换源字符不能为空！')
            self.lineEdit_RepSrc.setFocus()
            return False
        state['replsrcs'] = replsrcs
        replwith = self.lineEdit_RepWith.text()
        if not set(replwith).isdisjoint(self.UNUSABLE):
            self.settip(
                r"输入字符中包含不可用字符( \ / ? : * ' > < | )，请输入其他字符。")
            return False
        state['replwith'] = replwith
        self._packetlist.append(state)
        return True

    def _set_repl(self, state):
        ''' 设置“替换”中各控件的状态。'''
        self._setcommon(state)
        if state['replsrcs']:
            srcs = [i if i != ' ' else '%k' for i in state['replsrcs']]
            self.lineEdit_RepSrc.setText(' '.join(srcs))
        else:
            self.lineEdit_RepSrc.clear()
        if state['replwith']:
            self.lineEdit_RepWith.setText(state['replwith'])
        else:
            self.lineEdit_RepWith.clear()

    def get_rrepl(self):
        ''' 获取“范围替换”标签页下的用户输入数据。'''
        self.settip()
        state = self._getcommon()
        state['head'] = 'rrepl'
        rrepllb = self.lineEdit_RRepLB.text()
        rreplrb = self.lineEdit_RRepRB.text()
        state['inclb'] = self.checkBox_IncludeLB.isChecked()
        state['incrb'] = self.checkBox_IncludeRB.isChecked()
        rreplwith = self.lineEdit_RRepWith.text()
        if not any((rrepllb, rreplrb, rreplwith)):
            self.settip('左边界、右边界、替换字符不能同时为空！')
            return False
        if not set(rreplwith).isdisjoint(self.UNUSABLE):
            self.settip(
                r"输入字符中包含不可用字符( \ / ? : * ' > < | )，请输入其他字符。")
            return False
        state['rrepllb'] = rrepllb
        state['rreplrb'] = rreplrb
        state['rreplwith'] = rreplwith
        self._packetlist.append(state)
        return True

    def _set_rrepl(self, state):
        ''' 设置“范围替换”中各控件状态。'''
        self._setcommon(state)
        if state['rrepllb']:
            self.lineEdit_RRepLB.setText(state['rrepllb'])
        else:
            self.lineEdit_RRepLB.clear()
        if state['rreplrb']:
            self.lineEdit_RRepRB.setText(state['rreplrb'])
        else:
            self.lineEdit_RRepRB.clear()
        self.checkBox_IncludeLB.setChecked(state['inclb'])
        self.checkBox_IncludeRB.setChecked(state['incrb'])
        if state['rreplwith']:
            self.lineEdit_RRepWith.setText(state['rreplwith'])
        else:
            self.lineEdit_RRepWith.clear()

    def get_insert(self):
        ''' 获取“插入”标签页下的用户输入数据。'''
        self.settip()
        state = self._getcommon()
        state['head'] = 'insert'
        state['insertwith'] = self.comboBox_InsertWith.currentText()
        form = self.lineEdit_InsertForm.text()
        if not form:
            self.settip('请输入要插入的格式!')
            return False
        if not set(form).isdisjoint(self.UNUSABLE):
            self.settip(
                r"输入字符中包含不可用字符( \ / ? : * ' > < | )，请输入其他字符。")
            return False
        if self.comboBox_InsertWith.currentText() == '数字序号':
            if not re.search(r'%([\+\-0-9]{1,11}\.[\+\-0-9]{1,11})%', form):
                self.settip('请输入正确格式！')
                return False
        state['form'] = form
        if not (insertpos := self.lineEdit_InsertPos.text()):
            self.settip('请输入插入位置(百分比或绝对数值)！')
            return False
        if ('%' in insertpos) and (insertpos[-1] == '%'):
            try:
                state['insertpos'] = abs(float(insertpos[:-1])) / 100
            except:
                self.settip('文本插入位置百分比输入有误，请重新输入！')
                return False
        else:
            try:
                state['insertpos'] = abs(int(float(insertpos)))
            except:
                self.settip('文本插入绝对位置输入有误，请重新输入！')
                return False
        self._packetlist.append(state)
        return True

    def _set_insert(self, state):
        ''' 设置“插入”中各控件状态。'''
        self._setcommon(state)
        self.comboBox_InsertWith.setCurrentText(state['insertwith'])
        if state['form']:
            self.lineEdit_InsertForm.setText(state['form'])
        else:
            self.lineEdit_InsertForm.clear()
        inspos = state['insertpos']
        if isinstance(inspos, float):
            self.lineEdit_InsertPos.setText(str(inspos * 100) + '%')
        else:
            self.lineEdit_InsertPos.setText(str(inspos))

    def _addtoruleslist(self):
        ''' 根据tabview的标签页位置获取相应页下的用户输入数据并添加到规则列表、
        保存到文件。
        '''
        funlist = [self.get_repl, self.get_insert, self.get_rrepl]
        if funlist[self.tabwid.currentIndex()]():
            self.ruleslistupdate()

    def _setstate(self, state):
        ''' 参数state: 字典，列表packetlist中之一(保存的各控件状态的字典)。
            根据字典中head设置控件状态。
        '''
        if (tmp := state['head']) == 'repl':
            self.tabwid.setCurrentWidget(self.tab_Rep)
            self._set_repl(state)
        elif tmp == 'rrepl':
            self.tabwid.setCurrentWidget(self.tab_RRep)
            self._set_rrepl(state)
        elif tmp == 'insert':
            self.tabwid.setCurrentWidget(self.tab_Insert)
            self._set_insert(state)

    def clearstate(self):
        ''' 清空(恢复默认)“设定规则”分组的所有文本输入控件的状态。'''
        self.settip()
        self.lineEdit_RepSrc.clear()
        self.lineEdit_RepWith.clear()
        self.lineEdit_RRepLB.clear()
        self.lineEdit_RRepRB.clear()
        self.lineEdit_RRepWith.clear()
        self.comboBox_InsertWith.setCurrentIndex(0)
        self.lineEdit_InsertForm.setText('[%Y-%m-%d]')
        self.lineEdit_InsertPos.setText('0.0%')
        self.plainText_ExcludeFolder.clear()
        self.comboBox_InExcExt.setCurrentIndex(0)
        self.lineEdit_Exts.clear()
        self.comboBox_SpInf.setCurrentIndex(0)

    def ruleslistupdate(self, ind=None):
        ''' 更新规则列表。'''
        self.list_RulesList.clear()
        lth = len(self._packetlist)
        wid = len(str(lth)) + 1
        for i in range(lth):
            self.list_RulesList.addItem(
                self._pktitle(self._packetlist[i], str(i + 1) + '.', wid))
        if ind == None:
            if (lth - 1) >= 0:
                self.list_RulesList.setCurrentRow(lth - 1)
        else:
            self.list_RulesList.setCurrentRow(ind)

    def tasklistupdate(self):
        ''' 更新任务列表。'''
        self.list_Tasks.clear()
        for i in self._tasklist:
            self.list_Tasks.addItem(i.title)

    def setdefaultdir(self):
        ''' 设置默认起始文件夹。'''
        dfdir = self._selectdir()
        if not dfdir:
            self.settip('未设置默认起始路径。')
            return False
        self._defaultdir = dfdir
        self._settingstate['defaultdir'] = dfdir
        self.settip('默认起始路径设置成功。')

    def _selectdir(self):
        ''' 弹出选择文件夹对话框并返回选择值。'''
        folderpath = QFD.getExistingDirectory(
            self, '选择目标文件夹', self._defaultdir)
        if folderpath:
            return os.path.realpath(folderpath)
        self._defaultdir = folderpath
        return folderpath

    def _rl_delselected(self):
        ''' 获取规则当前选中的项，根据索引删除packetlist相应项并更新列表显示,
        返回删除的项。
        '''
        self.settip()
        ind = self.list_RulesList.currentRow()
        lth = len(self._packetlist)
        if ind == -1:
            if not lth:
                self.settip('规则列表为空！')
            else:
                self.settip('还未选中任何规则！')
            return False
        curit = self._packetlist.pop(ind)
        # 以下左ind是删除其中一项后要选中的项，如果右ind大于0就选中前面一项，
        # 小于等于0时：lth不为空就选中第0项，为空就不选中
        ind = (ind - 1) if (ind > 0) else (0 if lth > 0 else None)
        self.ruleslistupdate(ind)
        return curit

    def _rl_editselected(self):
        ''' 编辑规则列表中选中的项：删除相应项并把该项包含的状态设置到相应控件上。'''
        if not (curit := self._rl_delselected()):
            return False
        self._setstate(curit)
        return True

    def _rl_clear(self):
        ''' 清空规则列表。'''
        self._packetlist.clear()
        self.ruleslistupdate()

    def _addtotasklist(self):
        ind = self.list_RulesList.currentRow()
        if ind == -1:
            if not len(self._packetlist):
                self.settip('规则列表为空！')
            else:
                self.settip('还未选中任何规则！')
            return False
        dirpath = self.lineEdit_TGPath.text()
        if (not dirpath) or (not os.path.exists(dirpath)):
            dirpath = self._selectdir()
        if not dirpath:
            self.settip('未选择目标文件夹。')
            return False
        self.settip()
        pkdic = deepcopy(self._packetlist[ind])
        self._tasklist.append(
            Task(self._pktitle(pkdic), os.path.realpath(dirpath), pkdic)
        )
        self.tasklistupdate()
        return True

    def _dptarget(self):
        ''' “...”按钮选择路径并显示到“目标文件夹”后的文本框。'''
        tg = self._selectdir()
        if not tg:
            self.settip('没有选择文件夹。')
            return False
        self.lineEdit_TGPath.setText(tg)
        return True

    def _taskmoveup(self):
        ''' 把选中任务往上移。'''
        ind = self.list_Tasks.currentRow()
        if ind < 1:
            return False
        self._tasklist[ind - 1], self._tasklist[ind] = \
            self._tasklist[ind], self._tasklist[ind - 1]
        self.tasklistupdate()
        self.list_Tasks.setCurrentRow(ind - 1)
        return True

    def _taskmovedown(self):
        ''' 把选中任务往下移。'''
        ind = self.list_Tasks.currentRow()
        if (ind == -1) or (ind >= len(self._tasklist) - 1):
            return False
        self._tasklist[ind], self._tasklist[ind + 1] = \
            self._tasklist[ind + 1], self._tasklist[ind]
        self.tasklistupdate()
        self.list_Tasks.setCurrentRow(ind + 1)
        return True

    def _taskclear(self):
        ''' 清空任务列表。'''
        self._tasklist.clear()
        self.settip('任务已清空。')
        self.tasklistupdate()

    def _taskdelselected(self):
        ''' 删除选中任务。'''
        ind = self.list_Tasks.currentRow()
        if ind == -1:
            self.settip('未选中任何任务。')
            return False
        self._tasklist.pop(ind)
        self.tasklistupdate()
        return True

    def _mk_res_txt(self, successful, failed, unchanged):
        unchanged = '\n'.join(
            [f'文件名：{os.path.basename(i)}\n'
             f'所在目录：{os.path.dirname(i)}\n'
             f'{"-" * 150}'
             for i in unchanged])
        failed = '\n'.join(
            [f'重命名后：{os.path.basename(val)}\n'
             f'原文件名：{os.path.basename(key)}\n'
             f'所在目录：{os.path.dirname(key)}\\\n{"-" * 150}'
             for key, val in failed.items()])
        successful = '\n'.join(
            [f'重命名后：{os.path.basename(val)}\n'
             f'原文件名：{os.path.basename(key)}\n'
             f'所在目录：{os.path.dirname(key)}\\\n{"-" * 150}'
             for key, val in successful.items()])
        return successful, failed, unchanged

    def _task_prev_all(self):
        ''' 运行所有任务。'''
        pass

    def _task_prev_sel(self):
        ''' 预览选中任务的执行结果并让用户决定是否执行。'''
        self.settip()
        if (ind := self.list_Tasks.currentRow()) != -1:
            self._task_current = self._tasklist[ind]
            if not self._task_current.RENAMED:
                PrevWindow.btn_confirm.setEnabled(True)
            successful, failed, unchanged = self._task_current.preview()
            successful, failed, unchanged = self._mk_res_txt(
                successful, failed, unchanged)
            PrevWindow.textEdit.setText(successful)
            PrevWindow.show()
            # TODO: 增加PreviewWindow的标签页功能，以查看重命名成功、失败、无变化的文件信息。
        else:
            self.settip('没有选中任何任务！')

    def _dorename(self, mode):
        if mode == 'sel':
            if self._task_current != None:
                self._task_current.start()
        elif mode == 'all':
            pass


class Preview(QMW, PUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_cancel.clicked.connect(self._cancel)
        self.btn_confirm.clicked.connect(self._confirm)

    def _cancel(self):
        self.close()

    def _confirm(self):
        self.btn_confirm.setEnabled(False)
        MainWindow._dorename('sel')


if __name__ == '__main__':
    app = QAPP(sys.argv)
    MainWindow = RenameTool()
    PrevWindow = Preview()
    MainWindow.show()
    sys.exit(app.exec_())
