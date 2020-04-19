# -*- encoding: utf-8 -*-
'''
--------------------------------------
@Version   : 2020.0413.00
@Author    : hrp
@Desciption: 主程序，快速批量对文件重命名。
--------------------------------------
'''

# TODO: 计划变更功能:目标支持多文件和文件夹，支持文件、文件夹这样的混合目标。

import os
import sys

filepath = os.path.dirname(os.path.realpath(__file__))
sys.path = [os.path.dirname(filepath)] + sys.path

import pickle
import re
from copy import deepcopy
from PyQt5.QtWidgets import QApplication as app
from PyQt5.QtWidgets import QFileDialog as qfd
from PyQt5.QtWidgets import QMainWindow as qmw
from Renamer import Task
from ui import *

sep = os.sep

class RenameTool(qmw, rentwd):
    '''
    RnameTool的主模块。
    属性 __UNUSABLE: set，win平台不可用于文件名的字符的集合。
    属性 _task_current: Task实例，当前操作的Task实例。
    属性 _tasklist: list，Task实例列表。
    属性 _packetlist: list，规则列表。
    属性 _settingstate: dict，暂存设置状态的字典。
    属性 _setspath: 保存设置的文件的完整路径。
    属性 _rulespath: 保存规则列表的文件的完整路径。
    '''
    __UNUSABLE = set(r"\/?:*'><|")

    def __init__(self):
        super(RenameTool, self).__init__()
        self.setupUi(self)
        if not self._checksetsdir():
            exit('保存设置的文件夹不存在并创建失败。')
        self._task_current = None
        self._tasklist = list()
        self._packetlist = list()
        self._settingstate = dict()
        self._getsettingstate()
        self._settingstate['defaultdir'] = os.path.realpath('.')
        self._loadsettings()
        self._signal_slot_func()

    def _checksetsdir(self):
        '''
        检查路径下存放设置文件的目录状态是否正常。
        '''
        dir_logs = os.path.join(sys.path[0], 'logs')
        dir_sets = os.path.join(sys.path[0], 'settings')
        for i in (dir_sets, dir_logs):
            if not os.path.exists(i):
                try:
                    os.mkdir(i)
                except:
                    return False
            elif not os.path.isdir(i):
                return False
        self._setspath = os.path.join(dir_sets, 'settings.bin')
        self._rulespath = os.path.join(dir_sets, 'rules.bin')
        return True

    def closeEvent(self, *args, **kwargs):
        self._savesettings()

    def _signal_slot_func(self):
        '''
        统一绑定各种控件信号与函数。
        '''
        # checkBox_Word：          单词模式选择框
        self.checkBox_Word.clicked.connect(self._getsettingstate)
        # checkBox_IncludeLB：     包含左边界选择框
        self.checkBox_IncludeLB.clicked.connect(self._getsettingstate)
        # checkBox_IncludeRB：     包含右边界选择框
        self.checkBox_IncludeRB.clicked.connect(self._getsettingstate)
        # comboBox_InExcExt：      指定或排除文件格式下拉单选框
        self.comboBox_InExcExt.currentIndexChanged.connect(self._getsettingstate)
        # comboBox_SpInf：         作用范围是否包含扩展名下拉单选框
        self.comboBox_SpInf.currentIndexChanged.connect(self._getsettingstate)
        # btn_SaveToList：         保存到列表按钮
        self.btn_SaveToList.clicked.connect(self._addtoruleslist)
        # btn_RL_DelSelected：     规则列表的删除选中项按钮
        self.btn_RL_DelSelected.clicked.connect(self._rl_delselected)
        # btn_RL_EditSelected：    规则列表中的编辑选中项按钮
        self.btn_RL_EditSelected.clicked.connect(self._rl_editselected)
        # btn_RL_AddToTaskList：   “加入待执行”按钮
        self.btn_setrule_clear.clicked.connect(self.clearstate)
        # comboBox_InsertWith：   “插入”下拉单选框
        self.btn_RL_AddToTaskList.clicked.connect(self._addtotasklist)
        # comboBox_InsertPos：    “插入位置”下拉单选框
        self.comboBox_InsertWith.currentIndexChanged.connect(self._setform)
        # btn_RL_ClearRules：     规则列表的清空按钮
        self.btn_RL_ClearAll.clicked.connect(self._rl_clear)
        # btn_CTGPath：           规则列表中的“...”按钮
        self.btn_CTGPath.clicked.connect(self._dptarget)
        # btn_TS_MoveUp：         任务列表的“上移”按钮
        self.btn_TS_MoveUp.clicked.connect(self._taskmoveup)
        # btn_TS_MoveDown：       任务列表的“下移”按钮
        self.btn_TS_MoveDown.clicked.connect(self._taskmovedown)
        # btn_TS_Clear：          任务列表的“清空”按钮
        self.btn_TS_Clear.clicked.connect(self._taskclear)
        # btn_TS_DelSelected：    任务列表的“移除”按钮
        self.btn_TS_DelSelected.clicked.connect(self._taskdelselected)
        # btn_TS_PrevSel：        任务列表的“预览选中”按钮
        self.btn_TS_PrevSel.clicked.connect(self._task_prev_sel)
        # btn_chexcfolder:       排除列表的“选择文件夹”按钮
        self.btn_chexcfolder.clicked.connect(self._setexcludefolder)
        # btn_ClearExcfd:        排除列表的“清空”按钮
        self.btn_ClearExcfd.clicked.connect(self._clsexcfolder)
        # btn_chexcfile:         排除列表的“选择文件”按钮
        self.btn_chexcfile.clicked.connect(self._setexcludefiles)

    def _getsettingstate(self):
        '''
        获取需要保存状态的常用控件状态值。并存放到_settingstate字典。
        '''
        # 限定扩展名或排除扩展名选择框
        self._settingstate['comboBox_inexcext'] = self.comboBox_InExcExt.currentText()
        # 是否单词模式
        self._settingstate['checkBox_word'] = self.checkBox_Word.isChecked()
        # 作用范围是否包含扩展名
        self._settingstate['comboBox_spinf'] = self.comboBox_SpInf.currentText()
        # 范围替换中的是否包含左边界
        self._settingstate['checkBox_inclb'] = self.checkBox_IncludeLB.isChecked()
        # 范围替换中的是否包含右边界
        self._settingstate['checkBox_incrb'] = self.checkBox_IncludeRB.isChecked()

    def _setsettingstate(self):
        '''
        把从设置中读取的控件状态恢复到相应控件上。
        '''
        try:
            # 限定扩展名或排除扩展名选择框
            self.comboBox_InExcExt.setCurrentText(self._settingstate['comboBox_inexcext'])
            # 单词模式
            self.checkBox_Word.setChecked(self._settingstate['checkBox_word'])
            # 作用范围是否包含扩展名
            self.comboBox_SpInf.setCurrentText(self._settingstate['comboBox_spinf'])
            # 范围替换中的是否包含左边界
            self.checkBox_IncludeLB.setChecked(self._settingstate['checkBox_inclb'])
            # 范围替换中的是否包含右边界
            self.checkBox_IncludeRB.setChecked(self._settingstate['checkBox_incrb'])
            # 目标文件夹文本框
            self.lineEdit_TGPath.setText(self._settingstate['defaultdir'])
        except:
            pass

    def _loadsettings(self):
        '''
        程序运行时从文件读取上次储存的控件状态和规则列表。
        '''
        if os.path.exists(self._setspath):
            try:
                with open(self._setspath, 'rb') as sf:
                    tmp = pickle.load(sf)
                    if len(tmp) >= len(self._settingstate):
                        self._settingstate = tmp
                self._setsettingstate()
            except Exception as err:
                self.tips('设置加载出错:' + str(err))
        # 读取规则列表并刷新。
        if os.path.exists(self._rulespath):
            try:
                with open(self._rulespath, 'rb') as rsl:
                    self._packetlist = pickle.load(rsl)
                    self.ruleslistupdate()
            except Exception as err:
                self.tips('规则列表载入错误:' + str(err))

    def _savesettings(self):
        '''
        设置改变时保存控件状态到文件。
        '''
        try:
            with open(self._setspath, 'wb') as sf:
                pickle.dump(self._settingstate, sf)
        except Exception as err:
            self.tips('设置保存出错:' + str(err))
        # 保存规则列表到文件。
        try:
            with open(self._rulespath, 'wb') as rsl:
                pickle.dump(self._packetlist, rsl)
        except Exception as err:
            self.tips('规则列表保存出错:' + str(err))

    def tips(self, msg=''):
        '''
        状态栏提示信息。
        :param msg: 要显示的字符串。
        '''
        self.statusBar.showMessage(msg)

    def _setform(self):
        '''
        设置“插入”标签页的文本框预设内容。
        '''
        if self.comboBox_InsertWith.currentIndex() == 0:
            self.lineEdit_InsertForm.setText('[%Y-%m-%d]')
        else:
            self.lineEdit_InsertForm.clear()

    def _pktitle(self, pk, num='', wid=0):
        '''
        生成数据包(规则)的标题,用于显示在list_RulesList即规则列表中。
        :param pk: 从各控件读取到的用户输入的信息，见 get_repl、get_rrepl、get_insert 函数。
        :param num: 要返回的字符串前的数字字符。
        :param wid: 数字字符位数，不够位数用0填充。
        :return: 字符串，依据数据包生成。
        '''
        if pk['head'] == 'repl':
            srcs = '、'.join([i if i != ' ' else r'\k' for i in pk['srcs']])
            repl = pk['repl']
            if not repl:
                repl = '无'
            title = (f'{num:0>{wid}}替换：将 < {srcs} > '
                     f'替换成 < {repl} >，')
        elif pk['head'] == 'rrepl':
            rrepllb = pk['rrepllb']
            if not rrepllb:
                rrepllb = '无'
            rreplrb = pk['rreplrb']
            if not rreplrb:
                rreplrb = '无'
            inclb = '包含' if pk['inclb'] else '不含'
            incrb = '包含' if pk['incrb'] else '不含'
            repl = pk['repl']
            if not repl:
                repl = '无'
            title = (f'{num:0>{wid}}范围：范围内替换成 < {repl} >，'
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
        elif pk['head'] == 'regex':
            pattern = pk['pattern']
            repl = pk['repl']
            if not repl:
                repl = '无'
            count = pk['count']
            title = (f'{num:0>{wid}}正则：表达式 < {pattern} >，'
                     f'匹配项替换为 < {repl} >，次数: < {count} >，')
        inexcext = pk['inexcext']
        exts = pk['exts']
        if not exts:
            exts = '无'
        else:
            exts = ' '.join(exts)
        word = '是' if pk['word'] else '否'
        spinf = pk['spinf']
        title += (f'{inexcext} < {exts} >，'
                  f'单词模式: < {word} >，作用范围: < {spinf} >')
        return title

    def _getcommon(self):
        '''
        获取“设定规则”分组内除了 tabview 以外的其他控件的数据，
        (替换、范围替换、插入三个规则类型都共用的控件)。
        :return: 记录各控件状态的字典。
        '''
        state = dict()
        state['inexcext'] = self.comboBox_InExcExt.currentText()
        # 限定或排除的扩展名，简单处理用户输入的文本，提取扩展名
        exts = [i.strip() for i in self.lineEdit_Exts.text().split(' ')
                if i and (i != ' ')]
        state['exts'] = [i if i[0] == '.' else '.' + i for i in exts]
        state['word'] = self.checkBox_Word.isChecked()
        state['spinf'] = self.comboBox_SpInf.currentText()
        return state

    def _setcommon(self, state):
        '''
        设置“设定规则”分组内除了 tabview 以外的其他控件的数据，
        (替换、范围替换、插入三个规则类型都共用的控件)。
        :param state: 记录各控件状态的字典，跟_getcommon函数返回值是一样的。
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
        except Exception as err:
            self.tips('设置控件时出错：' + str(err))

    def get_repl(self):
        '''
        获取“替换”标签页下的用户输入数据。
        :return: bool。
        '''
        self.tips()
        state = self._getcommon()
        state['head'] = 'repl'
        srcs = [' ' if i == r'\k' else i
                for i in self.lineEdit_ReplSrc.text().split(' ') if i]
        if not srcs:
            self.tips('替换源字符不能为空！')
            self.lineEdit_ReplSrc.setFocus()
            return False
        elif not set(srcs).isdisjoint(self.__UNUSABLE):
            self.tips(
                r"替换源字符中包含不可用字符( \ / ? : * ' > < | )，请输入其他字符。")
            self.lineEdit_ReplSrc.setFocus()
            return False
        state['srcs'] = srcs
        repl = self.lineEdit_ReplWith.text()
        if not set(repl).isdisjoint(self.__UNUSABLE):
            self.tips(
                r"替换后字符中包含不可用字符( \ / ? : * ' > < | )，请输入其他字符。")
            self.lineEdit_ReplWith.setFocus()
            return False
        state['repl'] = repl
        self._packetlist.append(state)
        return True

    def _set_repl(self, state):
        '''
        设置“替换”中各控件的状态。
        :param state: 字典。
        '''
        self._setcommon(state)
        if state['srcs']:
            srcs = [i if i != ' ' else r'\k' for i in state['srcs']]
            self.lineEdit_ReplSrc.setText(' '.join(srcs))
        else:
            self.lineEdit_ReplSrc.clear()
        if state['repl']:
            self.lineEdit_ReplWith.setText(state['repl'])
        else:
            self.lineEdit_ReplWith.clear()

    def get_rrepl(self):
        '''
        获取“范围替换”标签页下的用户输入数据。
        :return: bool。
        '''
        self.tips()
        state = self._getcommon()
        state['head'] = 'rrepl'
        rrepllb = self.lineEdit_RReplLB.text()
        rreplrb = self.lineEdit_RReplRB.text()
        state['inclb'] = self.checkBox_IncludeLB.isChecked()
        state['incrb'] = self.checkBox_IncludeRB.isChecked()
        repl = self.lineEdit_RReplWith.text()
        if not any((rrepllb, rreplrb, repl)):
            self.tips('左边界、右边界、替换字符不能同时为空！')
            return False
        if not set(rrepllb).isdisjoint(self.__UNUSABLE):
            self.tips(
                r"左边界字符中包含不可用字符( \ / ? : * ' > < | )，请输入其他字符。")
            return False
        elif not set(rreplrb).isdisjoint(self.__UNUSABLE):
            self.tips(
                r"右边界字符中包含不可用字符( \ / ? : * ' > < | )，请输入其他字符。")
            return False
        elif not set(repl).isdisjoint(self.__UNUSABLE):
            self.tips(
                r"替换后字符中包含不可用字符( \ / ? : * ' > < | )，请输入其他字符。")
            return False
        state['rrepllb'] = rrepllb
        state['rreplrb'] = rreplrb
        state['repl'] = repl
        self._packetlist.append(state)
        return True

    def _set_rrepl(self, state):
        '''
        设置“范围替换”中各控件状态。
        :param state: 字典。
        '''
        self._setcommon(state)
        if state['rrepllb']:
            self.lineEdit_RReplLB.setText(state['rrepllb'])
        else:
            self.lineEdit_RReplLB.clear()
        if state['rreplrb']:
            self.lineEdit_RReplRB.setText(state['rreplrb'])
        else:
            self.lineEdit_RReplRB.clear()
        self.checkBox_IncludeLB.setChecked(state['inclb'])
        self.checkBox_IncludeRB.setChecked(state['incrb'])
        if state['repl']:
            self.lineEdit_RReplWith.setText(state['repl'])
        else:
            self.lineEdit_RReplWith.clear()

    def get_insert(self):
        '''
        获取“插入”标签页下的用户输入数据。
        :return: bool。
        '''
        self.tips()
        state = self._getcommon()
        state['head'] = 'insert'
        state['insertwith'] = self.comboBox_InsertWith.currentText()
        form = self.lineEdit_InsertForm.text()
        if not form:
            self.tips('请输入要插入的格式!')
            return False
        if self.comboBox_InsertWith.currentText() == '数字序号':
            tmp = re.search(
                    r'<([0-9]{1,10}\.[0-9]{1,10}\.[1-9]{1,10})>', form)
            if not tmp:
                self.tips('请输入正确格式！')
                return False
            if not set(form.replace(
                    tmp.group(), '', 1)).isdisjoint(self.__UNUSABLE):
                self.tips(
                    r"插入字符中包含不可用字符( \ / ? : * ' > < | )，请输入其他字符。")
                return False
        else:
            if not set(form).isdisjoint(self.__UNUSABLE):
                self.tips(
                    r"插入字符中包含不可用字符( \ / ? : * ' > < | )，请输入其他字符。")
                return False
        state['form'] = form
        insertpos = self.lineEdit_InsertPos.text()
        if not insertpos:
            self.tips('请输入插入位置(百分比或绝对数值)！')
            return False
        if ('%' in insertpos) and (insertpos[-1] == '%'):
            try:
                state['insertpos'] = abs(float(insertpos[:-1])) / 100
            except:
                self.tips('文本插入位置百分比输入有误，请重新输入！')
                return False
        else:
            try:
                state['insertpos'] = abs(int(float(insertpos)))
            except:
                self.tips('文本插入绝对位置输入有误，请重新输入！')
                return False
        self._packetlist.append(state)
        return True

    def _set_insert(self, state):
        '''
        设置“插入”中各控件状态。
        '''
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

    def get_regex(self):
        '''
        获取“正则表达式”标签页下各控件状态。
        :return: bool
        '''
        self.tips()
        state = self._getcommon()
        state['head'] = 'regex'
        pattern = self.lineEdit_RegexPattern.text()
        if not pattern:
            self.tips('没有输入表达式。')
            self.lineEdit_ReRepl.setFocus()
            return False
        state['pattern'] = pattern
        repl = self.lineEdit_ReRepl.text()
        if not set(repl).isdisjoint(self.__UNUSABLE):
            self.tips(
                r"替换字符中包含不可用字符( \ / ? : * ' > < | )，请输入其他字符。")
            self.lineEdit_ReRepl.setFocus()
            return False
        state['repl'] = repl
        count = self.lineEdit_ReReplCount.text()
        try:
            count = int(count)
            if count < 0:
                self.tips('替换次数输入不正确。')
                self.lineEdit_ReReplCount.setFocus()
                return False
        except:
            self.tips('替换次数输入不正确。')
            self.lineEdit_ReReplCount.setFocus()
            return False
        state['count'] = count
        self._packetlist.append(state)
        return True

    def _set_regex(self, state):
        '''
        设置“正则表达式”标签页下各控件状态。
        '''
        self._setcommon(state)
        self.lineEdit_RegexPattern.setText(state['pattern'])
        self.lineEdit_ReRepl.setText(state['repl'])
        self.lineEdit_ReReplCount.setText(str(state['count']))

    def _addtoruleslist(self):
        '''
        根据标签页位置运行相应函数获取用户输入的数据等操作。
        '''
        funlist = (self.get_repl, self.get_insert, self.get_rrepl, self.get_regex)
        if funlist[self.tabwid.currentIndex()]():
            self.ruleslistupdate()

    def _setstate(self, state):
        '''
        设置相应标签页的各控件状态。
        :param state: dict，储存控件状态的字典。
        '''
        tmp = state['head']
        if tmp == 'repl':
            self.tabwid.setCurrentWidget(self.tab_Repl)
            self._set_repl(state)
        elif tmp == 'rrepl':
            self.tabwid.setCurrentWidget(self.tab_RRepl)
            self._set_rrepl(state)
        elif tmp == 'insert':
            self.tabwid.setCurrentWidget(self.tab_Insert)
            self._set_insert(state)
        elif tmp == 'regex':
            self.tabwid.setCurrentWidget(self.tab_Regex)
            self._set_regex(state)

    def clearstate(self):
        '''
        清空(恢复默认)“设定规则”分组的所有文本输入控件的状态。
        '''
        self.tips()
        self.lineEdit_ReplSrc.clear()
        self.lineEdit_ReplWith.clear()
        self.lineEdit_RReplLB.clear()
        self.lineEdit_RReplRB.clear()
        self.lineEdit_RReplWith.clear()
        self.comboBox_InsertWith.setCurrentIndex(0)
        self.lineEdit_InsertForm.setText('[%Y-%m-%d]')
        self.lineEdit_InsertPos.setText('0.0%')
        self.comboBox_InExcExt.setCurrentIndex(0)
        self.lineEdit_Exts.clear()
        self.comboBox_SpInf.setCurrentIndex(0)
        self.lineEdit_RegexPattern.clear()
        self.lineEdit_ReRepl.clear()
        self.lineEdit_ReReplCount.setText('0')

    def ruleslistupdate(self, ind=None):
        '''
        更新规则列表。
        '''
        self.list_RulesList.clear()
        lth = len(self._packetlist)
        wid = len(str(lth)) + 1
        for i in range(lth):
            self.list_RulesList.addItem(
                self._pktitle(self._packetlist[i], str(i + 1) + '.', wid))
        if ind == None:
            if lth:
                self.list_RulesList.setCurrentRow(0)
        else:
            self.list_RulesList.setCurrentRow(ind)

    def tasklistupdate(self):
        '''
        更新任务列表。
        '''
        self.list_Tasks.clear()
        for i in self._tasklist:
            self.list_Tasks.addItem(i.title)

    def _select_dir(self):
        '''
        弹出选择文件夹对话框并返回选择值。
        :param rmb: bool，True or False，是否将本选择的文件夹作为下次的起始目录。
        :return: 选择文件夹则返完整回路径，取消则返回 False。
        '''
        folderpath = qfd.getExistingDirectory(
            self, '选择文件夹', self._settingstate['defaultdir'])
        if folderpath:
            folderpath = os.path.realpath(folderpath)
        else:
            return False
        self._settingstate['defaultdir'] = folderpath
        return folderpath

    def _select_files(self):
        '''
        弹出选择文件对话框并返回选择值。
        :return: list，选择文件则返回完整路径列表，取消则返回 False。
        '''
        pathlist, _ = qfd.getOpenFileNames(
            self, '多文件选择', self._settingstate['defaultdir'])
        if pathlist:
            pathlist = [os.path.realpath(i) for i in pathlist]
        else:
            return False
        return pathlist

    def _rl_delselected(self):
        '''
        获取规则当前选中的项，根据索引删除packetlist相应项并更新列表显示。
        :return: 被删除的元素。
        '''
        self.tips()
        ind = self.list_RulesList.currentRow()
        lth = len(self._packetlist)
        if ind == -1:
            if not lth:
                self.tips('规则列表为空！')
            else:
                self.tips('还未选中任何规则！')
            return False
        curit = self._packetlist.pop(ind)
        # 以下左ind是删除其中一项后要选中的项，如果右ind大于0就选中前面一项，
        # 小于等于0时：lth不为空就选中第0项，为空就不选中
        ind = (ind - 1) if (ind > 0) else (0 if lth > 0 else None)
        self.ruleslistupdate(ind)
        return curit

    def _rl_editselected(self):
        '''
        编辑规则列表中选中的项：删除相应项并把该项包含的状态设置到相应控件上。
        :return: bool。
        '''
        curit = self._rl_delselected()
        if not curit:
            return False
        self._setstate(curit)
        return True

    def _rl_clear(self):
        '''
        清空规则列表。
        '''
        self._packetlist.clear()
        self.ruleslistupdate()

    def _addtotasklist(self):
        '''
        将目标目录、排除的文件、文件夹列表打包进规则数据包并添加到任务列表。
        '''
        self.tips()
        ind = self.list_RulesList.currentRow()
        if ind == -1:
            if not len(self._packetlist):
                self.tips('规则列表为空！')
            else:
                self.tips('还未选中任何规则！')
            return False
        targets = self.lineEdit_TGPath.text()
        if (not targets) or (not os.path.exists(targets)):
            targets = self._dptarget()
        if not targets:
            return False
        pkdic = deepcopy(self._packetlist[ind])
        excfd = [i.strip()
                 for i in self.plainText_ExcludeFolder.toPlainText().split('\n')
                 if i and (i != '\n')]
        pkdic['excfd'] = [i for i in excfd if os.path.exists(i)]
        self._tasklist.append(
            Task(self._pktitle(pkdic), os.path.realpath(targets), pkdic))
        self.tasklistupdate()
        return True

    def _dptarget(self):
        '''
        “...”按钮选择路径并显示到“目标文件夹”后的文本框。
        :return: bool or str，str:目标路径，bool:False。
        '''
        target = self._select_dir()
        if not target:
            self.tips('没有选择文件夹。')
            return False
        self.lineEdit_TGPath.setText(target)
        return target

    def _taskmoveup(self):
        '''
        把选中任务往上移。
        :return: bool。
        '''
        ind = self.list_Tasks.currentRow()
        if ind < 1:
            return False
        self._tasklist[ind - 1], self._tasklist[ind] = self._tasklist[ind], self._tasklist[ind - 1]
        self.tasklistupdate()
        self.list_Tasks.setCurrentRow(ind - 1)
        return True

    def _taskmovedown(self):
        '''
        把选中任务往下移。
        :return: bool。
        '''
        ind = self.list_Tasks.currentRow()
        if (ind == -1) or (ind >= len(self._tasklist) - 1):
            return False
        self._tasklist[ind], self._tasklist[ind + 1] = self._tasklist[ind + 1], self._tasklist[ind]
        self.tasklistupdate()
        self.list_Tasks.setCurrentRow(ind + 1)
        return True

    def _taskclear(self):
        '''
        清空任务列表并刷新。
        '''
        self._tasklist.clear()
        self.tips('任务已清空。')
        self.tasklistupdate()

    def _taskdelselected(self):
        '''
        删除选中任务。
        '''
        ind = self.list_Tasks.currentRow()
        if ind == -1:
            self.tips('未选中任何任务。')
            return False
        self._tasklist.pop(ind)
        self.tasklistupdate()
        return True

    def _clsexcfolder(self):
        '''
        清空“排除”文本框。
        '''
        self.plainText_ExcludeFolder.clear()

    def _setexcludefolder(self):
        '''
        点击选择要排除的文件夹。
        '''
        curtext = self.plainText_ExcludeFolder.toPlainText()
        selected = self._select_dir()
        if selected:
            if curtext:
                curtext = '\n'.join((curtext, selected))
                self.plainText_ExcludeFolder.setPlainText(curtext)
            else:
                self.plainText_ExcludeFolder.setPlainText(selected)

    def _setexcludefiles(self):
        '''
        点击选择要排除的文件。
        '''
        curtext = self.plainText_ExcludeFolder.toPlainText()
        selected = self._select_files()
        if selected:
            selected = '\n'.join(selected)
            if curtext:
                curtext = '\n'.join((curtext, selected))
                self.plainText_ExcludeFolder.setPlainText(curtext)
            else:
                self.plainText_ExcludeFolder.setPlainText(selected)

    def _mk_res_txt(self, successful, failed, unchanged):
        '''
        根据任务返回的预览结果生成预览格式。
        :param successful: dict，预览中可以重命名的文件。
        :param failed: dict，预览中不可用重命名的文件。
        :param unchanged: list，预览中文件名无变化的文件。
        :return: 分别返回可以重命名的文件、不可重命名的文件、无变化的文件的显示格式。
        '''
        unchanged = '\n'.join(
            [f'文件路径：{os.path.dirname(i)}\n'
             f'原文件名：{os.path.basename(i)}\n'
             f'{"-" * 100}'
             for i in unchanged])
        failed = '\n'.join(
            [f'文件路径：{os.path.dirname(key)}{sep}\n'
             f'原文件名：{os.path.basename(key)}\n'
             f'重命名后：{os.path.basename(val)}\n'
             f'{"-" * 100}'
             for key, val in failed.items()])
        successful = '\n'.join(
            [f'文件路径：{os.path.dirname(key)}{sep}\n'
             f'原文件名：{os.path.basename(key)}\n'
             f'重命名后：{os.path.basename(val)}\n'
             f'{"-" * 100}'
             for key, val in successful.items()])
        return successful, failed, unchanged

    def _task_prev_all(self):
        '''
        预览全部任务。
        '''
        pass

    def _task_prev_sel(self):
        '''
        预览选中任务的执行结果并弹出预览窗口，让用户决定是否执行任务。
        '''
        self.tips()
        ind = self.list_Tasks.currentRow()
        if ind != -1:
            self._task_current = self._tasklist[ind]
            successful, failed, unchanged = self._task_current.preview()
            successfultext, failedtext, unchangedtext = self._mk_res_txt(
                successful, failed, unchanged)
            PrevWindow.tabWidget.setTabText(
                0, f"可以重命名({len(successful)})")
            PrevWindow.tabWidget.setTabText(
                1, f"无法重命名({len(failed)})")
            PrevWindow.tabWidget.setTabText(
                2, f"无变化({len(unchanged)})")
            PrevWindow.textEdit_successful.setText(successfultext)
            PrevWindow.textEdit_failed.setText(failedtext)
            PrevWindow.textEdit_unchanged.setText(unchangedtext)
            PrevWindow.tabWidget.setCurrentIndex(0)
            if self._task_current.RENAMED:
                PrevWindow.btn_confirm.setText('已完成重命名')
                PrevWindow.btn_cancel.setText('关闭')
                PrevWindow.btn_confirm.setEnabled(False)
            else:
                PrevWindow.btn_confirm.setText('重命名( 不再确认 )')
                PrevWindow.btn_cancel.setText('取消')
                if successful:
                    PrevWindow.btn_confirm.setEnabled(True)
                else:
                    PrevWindow.btn_confirm.setEnabled(False)
            PrevWindow.resize(700, 800)
            PrevWindow.show()
        else:
            self.tips('没有选中任何任务！')

    def do_rename(self, mode):
        '''
        正式进行重命名操作。
        '''
        if mode == 'sel':
            if self._task_current != None:
                self._task_current.start()
        elif mode == 'all':
            pass


class Preview(qmw, prevwd):
    def __init__(self):
        super(Preview, self).__init__()
        self.setupUi(self)
        self.btn_cancel.clicked.connect(self._cancel)
        self.btn_confirm.clicked.connect(self._confirm)
        self.tabWidget.currentChanged.connect(self._setbtn_confirm)

    def _setbtn_confirm(self):
        if self.tabWidget.currentIndex() == 0:
            if (MainWindow._task_current._successful
                    and (not MainWindow._task_current.RENAMED)):
                self.btn_confirm.setEnabled(True)
            else:
                self.btn_confirm.setEnabled(False)
        else:
            self.btn_confirm.setEnabled(False)

    def _cancel(self):
        self.close()

    def _confirm(self):
        self.btn_confirm.setEnabled(False)
        MainWindow.do_rename('sel')
        if MainWindow._task_current.RENAMED:
            self.btn_confirm.setText('已完成重命名')
            self.btn_cancel.setText('关闭')


if __name__ == '__main__':
    app = app(sys.argv)
    MainWindow = RenameTool()
    PrevWindow = Preview()
    MainWindow.show()
    sys.exit(app.exec_())
