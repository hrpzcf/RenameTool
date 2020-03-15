# coding: utf-8

# 版本：0.0.1
# 功能：RnameTool的任务模块。
# 作者：hrp

import os
import re
from time import localtime
from time import strftime


class Task(object):
    def __init__(self, title, target, statedict):
        self.target = target
        self.stdict = statedict
        excfd = '，'.join(
            statedict['excfd']) + '\\' if statedict['excfd'] else '无'
        self.title = f'目标：< {target}\\ >\n排除：< {excfd} >\n{title}\n{"-" * 50}'
        self._successful = dict()
        self._failed = dict()
        self._unchanged = list()
        self.MAX_NAME = 256
        self.RENAMED = False
        self._PREVIEWED = False
        self.ESCAPE = {
            '^': '\^', '$': '\$', '(': '\(', ')': '\)', '-': '\-', '[': '\[',
            ']': '\]', '{': '\{', '}': '\}', '.': '\.', '+': '\+'}

    def _allfile(self):
        '''返回值是排除用户要排除的文件夹、扩展名(指定或排除)后得到的所有文件路径。
        :return full_path_list: 目标目录下的完整文件路径列表，该列表排除了用户输入的需要排除的子目录。
        '''
        full_path_list = list()
        for root, dirs, files in os.walk(self.target, topdown=True):
            if root in self.stdict['excfd']:
                dirs.clear()
                continue
            for i in files:
                if self.stdict['inexcext'] == '指定扩展名':
                    if os.path.splitext(i)[1] in self.stdict['exts']:
                        full_path_list.append(os.path.join(root, i))
                elif self.stdict['inexcext'] == '排除扩展名':
                    if os.path.splitext(i)[1] not in self.stdict['exts']:
                        full_path_list.append(os.path.join(root, i))
                if not self.stdict['exts']:
                    full_path_list.append(os.path.join(root, i))
        return full_path_list

    def _rename(self):
        ''' 根据successful列表重命名文件。
        重命名失败则把'路径+文件名'从'成功'列表移到'失败'列表。
        设置任务的'已重命名'标志为True。
        '''
        for k, v in list(self._successful.items()):
            try:
                os.rename(k, v)
            except:
                self._failed[k] = self._successful.pop(k)
        self.RENAMED = True

    def _rng_str(self, string, rrepllb, rreplrb):
        ''' 寻找符合给定范围的字符串(最少匹配)，
        并返回找到的字符串列表。
        :param string: 需要匹配的原字符串。
        :param rrepllb: 范围的左边界。
        :param rreplrb: 范围的右边界。
        :return srcs: 匹配到的字符串列表。
        '''
        for k, v in self.ESCAPE.items():
            rrepllb = rrepllb.replace(k, v)
            rreplrb = rreplrb.replace(k, v)
        if not rrepllb:
            rrepllb = '^'
        if not rreplrb:
            rreplrb = '$'
        if self.stdict['word']:
            if rrepllb == '^':
                pt = f'{rrepllb}\S+{rreplrb}'
            else:
                pt = f'{rrepllb}\S+?{rreplrb}'
        else:
            if rrepllb == '^':
                pt = f'{rrepllb}.+{rreplrb}'
            else:
                pt = f'{rrepllb}.+?{rreplrb}'
        srcs = re.findall(pt, string)
        return srcs

    def _rng_num(self):
        ''' 输入数字范围进行替换的相关函数。'''
        pass

    def _repl_str(self, string, srcs, repl):
        keys = self.ESCAPE.keys()
        for i in range(len(srcs)):
            if srcs[i] in keys:
                srcs[i] = self.ESCAPE[srcs[i]]
        for src in srcs:
            if self.stdict['word']:
                string = re.sub(
                    f'(?<=\s){src}(?=\s|$)|(?<=^){src}(?=\s|$)', repl, string)
            else:
                string = re.sub(f'{src}', repl, string)
        return string

    def _ins_with_pos(self, string, instext, pos):
        string = string[:pos] + instext + string[pos:]
        return string

    def _kill_srcs(self, string, srcs, repl):
        for src in srcs:
            string = string.replace(src, repl)
        return string

    def _repl(self):
        spinf = self.stdict['spinf']
        srcs = [i.replace('%k', ' ') for i in self.stdict['srcs']]
        repl = self.stdict['repl']
        for fullpath in self._allfile():
            folder = os.path.dirname(fullpath)
            filename, ext = os.path.splitext(os.path.basename(fullpath))
            if spinf == '不含扩展名':
                filename = self._repl_str(filename, srcs, repl)
            elif spinf == '仅限扩展名':
                ext = self._repl_str(ext, srcs, repl)
            elif spinf == '全部：独立':
                filename = self._repl_str(filename, srcs, repl)
                ext = self._repl_str(ext, srcs, repl)
            elif spinf == '全部：整体':
                filename, ext = filename + ext, ''
                filename = self._repl_str(filename, srcs, repl)
            fullpath_new = os.path.join(folder, filename + ext)
            if ((set(filename + ext) != '.')
                    and (len(fullpath_new) <= self.MAX_NAME)):
                if fullpath != fullpath_new:
                    if (fullpath_new not in self._successful.values()
                            and not os.path.exists(fullpath_new)):
                        self._successful[fullpath] = fullpath_new
                    else:
                        self._failed[fullpath] = fullpath_new
                else:
                    self._unchanged.append(fullpath)
            else:
                self._failed[fullpath] = fullpath_new

    def _rrepl(self):
        repl = self.stdict['repl']
        rrepllb = self.stdict['rrepllb']
        rreplrb = self.stdict['rreplrb']
        spinf = self.stdict['spinf']
        if not self.stdict['inclb']:
            repl = rrepllb + repl
        if not self.stdict['incrb']:
            repl += rreplrb
        for fullpath in self._allfile():
            folder = os.path.dirname(fullpath)
            filename, ext = os.path.splitext(os.path.basename(fullpath))
            if spinf == '不含扩展名':
                srcs = self._rng_str(filename, rrepllb, rreplrb)
                filename = self._kill_srcs(filename, srcs, repl)
            elif spinf == '仅限扩展名':
                srcs = self._rng_str(ext, rrepllb, rreplrb)
                ext = self._kill_srcs(ext, srcs, repl)
            elif spinf == '全部：独立':
                srcs = self._rng_str(filename, rrepllb, rreplrb)
                filename = self._kill_srcs(filename, srcs, repl)
                srcs = self._rng_str(ext, rrepllb, rreplrb)
                ext = self._kill_srcs(ext, srcs, repl)
            elif spinf == '全部：整体':
                filename, ext = filename + ext, ''
                srcs = self._rng_str(filename, rrepllb, rreplrb)
                filename = self._kill_srcs(filename, srcs, repl)
            fullpath_new = os.path.join(folder, filename + ext)
            if ((set(filename + ext) != '.')
                    and (len(fullpath_new) <= self.MAX_NAME)):
                if (fullpath != fullpath_new):
                    if (fullpath_new not in self._successful.values()
                            and not os.path.exists(fullpath_new)):
                        self._successful[fullpath] = fullpath_new
                    else:
                        self._failed[fullpath] = fullpath_new
                else:
                    self._unchanged.append(fullpath)
            else:
                self._failed[fullpath] = fullpath_new

    def _ins(self):
        # TODO: 计划增加功能，插入模式支持等宽序号(前面用0填充至所有序号等宽)。
        insertwith = self.stdict['insertwith']
        form = self.stdict['form']
        spinf = self.stdict['spinf']
        instance_pos = isinstance(self.stdict['insertpos'], float)
        if insertwith == '日期时间':
            str_to_ins = strftime(form, localtime())
        elif insertwith == '普通字符':
            str_to_ins = form
        elif insertwith == '数字序号':
            re_sch = re.search(
                r'%([\+\-0-9]{1,11}\.[\+\-0-9]{1,11})%', form)
            begin, step = map(int, re_sch.group(1).split('.'))
        for fullpath in self._allfile():
            if insertwith == '数字序号':
                str_to_ins = form.replace(re_sch.group(), str(begin))
            folder = os.path.dirname(fullpath)
            filename, ext = os.path.splitext(os.path.basename(fullpath))
            filename_length = len(filename)
            ext_length = len(ext)
            insertpos = self.stdict['insertpos']
            if spinf == '不含扩展名':
                if filename:
                    if instance_pos:
                        insertpos = int(filename_length * insertpos)
                    if insertpos > filename_length:
                        insertpos = filename_length
                    filename = self._ins_with_pos(
                        filename, str_to_ins, insertpos)
                else:
                    filename = str_to_ins
            elif spinf == '仅限扩展名':
                if ext:
                    if instance_pos:
                        insertpos = int(ext_length * insertpos) + 1
                    if insertpos > ext_length:
                        insertpos = ext_length
                    ext = self._ins_with_pos(ext, str_to_ins, insertpos)
                else:
                    ext = str_to_ins
            elif spinf == '全部：独立':
                if filename:
                    if instance_pos:
                        insertpos = int(filename_length * insertpos)
                    if insertpos > filename_length:
                        insertpos = filename_length
                    filename = self._ins_with_pos(
                        filename, str_to_ins, insertpos)
                else:
                    filename = str_to_ins
                if ext:
                    if instance_pos:
                        insertpos = int(ext_length * insertpos) + 1
                    if insertpos > ext_length:
                        insertpos = ext_length
                    ext = self._ins_with_pos(ext, str_to_ins, insertpos)
                else:
                    ext = str_to_ins
            elif spinf == '全部：整体':
                filename, ext = filename + ext, ''
                if filename:
                    if instance_pos:
                        insertpos = int(
                            (filename_length + ext_length) * insertpos)
                    if insertpos > (filename_length + ext_length):
                        insertpos = filename_length + ext_length
                    filename = self._ins_with_pos(
                        filename, str_to_ins, insertpos)
                else:
                    filename = str_to_ins
            fullpath_new = os.path.join(folder, filename + ext)
            if ((set(filename + ext) != '.')
                    and (len(fullpath_new) <= self.MAX_NAME)):
                if fullpath_new != fullpath:
                    if (fullpath_new not in self._successful.values()
                            and not os.path.exists(fullpath_new)):
                        self._successful[fullpath] = fullpath_new
                        if insertwith == '数字序号':
                            begin += step
                    else:
                        self._failed[fullpath] = fullpath_new
                else:
                    self._unchanged.append(fullpath)
            else:
                self._failed[fullpath] = fullpath_new

    def preview(self):
        if not self._PREVIEWED:
            if self.stdict['head'] == 'repl':
                self._repl()
            elif self.stdict['head'] == 'rrepl':
                self._rrepl()
            elif self.stdict['head'] == 'insert':
                self._ins()
            self._PREVIEWED = True
        return self._successful, self._failed, self._unchanged

    def start(self):
        if not self._PREVIEWED:
            self.preview()
        if not self.RENAMED:
            self._rename()
        return self._successful, self._failed, self._unchanged


if __name__ == '__main__':
    exit(0)
