# -*- encoding: utf-8 -*-
'''
--------------------------------------
@Version   : 20.0413.00
@Author    : hrp
@Desciption: RnameTool的任务模块。
--------------------------------------
'''

import os
import re
from time import localtime
from time import strftime
from Logger import wLog

sep = os.sep


class Task(object):
    MAX_NAME = 255
    __ESCAPE = {'^': '\^', '$': '\$', '(': '\(', ')': '\)', '-': '\-', '[': '\[',
                ']': '\]', '{': '\{', '}': '\}', '.': '\.', '+': '\+', ',': '\,', }

    def __init__(self, title, target, statedict):
        self.target = target
        self.stdict = statedict
        excfd = '，'.join([i + sep if os.path.isdir(i)
                          else i for i in statedict['excfd']]) if statedict['excfd'] else '无'
        self.title = f'目标：< {target}{sep} >\n排除：< {excfd} >\n{title}\n{"-" * 50}'
        self._successful = dict()
        self._failed = dict()
        self._unchanged = list()
        self._PREVIEWED = False
        self.RENAMED = False

    def __allfile(self):
        '''
        返回值是排除用户要排除的文件或文件夹、扩展名(指定或排除)后得到的所有文件路径。
        :return full_path_list: 目标目录下的完整文件路径列表，该列表排除了用户输入的需要排除的子目录。
        '''
        full_path_list = list()
        for root, dirs, files in os.walk(self.target, topdown=True):
            if root in self.stdict['excfd']:
                dirs.clear()
                continue
            for i in files:
                if os.path.join(root, i) in self.stdict['excfd']:
                    continue
                if not self.stdict['exts']:
                    full_path_list.append(os.path.join(root, i))
                elif self.stdict['inexcext'] == '指定文件格式':
                    if os.path.splitext(i)[1] in self.stdict['exts']:
                        full_path_list.append(os.path.join(root, i))
                elif self.stdict['inexcext'] == '排除文件格式':
                    if os.path.splitext(i)[1] not in self.stdict['exts']:
                        full_path_list.append(os.path.join(root, i))
                else:
                    raise ValueError('指定或排除扩展名选项出错了…')
        return full_path_list

    def __rename(self):
        '''
        根据successful列表重命名文件。
        重命名失败则把'路径+文件名'从'成功'列表移到'失败'列表。
        设置任务的'已重命名'标志为True。
        '''
        rnlog = wLog('历史记录测试')
        for k, v in self._successful.items():
            try:
                os.rename(k, v)
                rnlog.write(k, v)
            except OSError:
                self._failed[k] = self._successful.pop(k)
        rnlog.close()
        self.RENAMED = True

    def __rng_str(self, string, rrepllb, rreplrb):
        '''
        寻找符合给定范围的字符串(最少匹配)，
        并返回找到的字符串列表。
        :param string: 需要匹配的原字符串。
        :param rrepllb: 范围的左边界。
        :param rreplrb: 范围的右边界。
        :return srcs: 匹配到的字符串列表。
        '''
        if self.stdict['word']:
            pt = f'{rrepllb}\S+{rreplrb}'
        else:
            pt = f'{rrepllb}.+{rreplrb}'
        srcs = re.findall(pt, string)
        return srcs

    def __rng_num(self):
        '''
        输入数字范围进行替换。
        '''
        pass

    def __repl_str(self, string, srcs, repl):
        for src in srcs:
            if self.stdict['word']:
                string = re.sub(
                    f'(?<=\s){src}(?=\s|$)|(?<=^){src}(?=\s|$)', repl, string)
            else:
                string = re.sub(f'{src}', repl, string)
        return string

    def __ins_with_pos(self, string, instext, pos):
        string = ''.join((string[:pos], instext, string[pos:]))
        return string

    def __kill_srcs(self, string, srcs, repl):
        for src in srcs:
            string = string.replace(src, repl)
        return string

    def __repl(self):
        spinf = self.stdict['spinf']
        srcs = [i.replace(r'\k', ' ') for i in self.stdict['srcs']]
        for ind in range(len(srcs)):
            for k, v in self.__ESCAPE.items():
                srcs[ind] = srcs[ind].replace(k, v)
        repl = self.stdict['repl']
        for fullpath in self.__allfile():
            folder = os.path.dirname(fullpath)
            filename, ext = os.path.splitext(os.path.basename(fullpath))
            if spinf == '不含扩展名':
                filename = self.__repl_str(filename, srcs, repl)
            elif spinf == '仅限扩展名':
                ext = self.__repl_str(ext, srcs, repl)
            elif spinf == '全部：独立':
                filename = self.__repl_str(filename, srcs, repl)
                ext = self.__repl_str(ext, srcs, repl)
            elif spinf == '全部：整体':
                filename, ext = filename + ext, ''
                filename = self.__repl_str(filename, srcs, repl)
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

    def __rrepl(self):
        rrepllb = self.stdict['rrepllb']
        rreplrb = self.stdict['rreplrb']
        for k, v in self.__ESCAPE.items():
            rrepllb = rrepllb.replace(k, v)
            rreplrb = rreplrb.replace(k, v)
        if not rrepllb:
            rrepllb = '^'
        if not rreplrb:
            rreplrb = '$'
        repl = self.stdict['repl']
        spinf = self.stdict['spinf']
        if not self.stdict['inclb']:
            repl = rrepllb + repl
        if not self.stdict['incrb']:
            repl += rreplrb
        for fullpath in self.__allfile():
            folder = os.path.dirname(fullpath)
            filename, ext = os.path.splitext(os.path.basename(fullpath))
            if spinf == '不含扩展名':
                srcs = self.__rng_str(filename, rrepllb, rreplrb)
                filename = self.__kill_srcs(filename, srcs, repl)
            elif spinf == '仅限扩展名':
                srcs = self.__rng_str(ext, rrepllb, rreplrb)
                ext = self.__kill_srcs(ext, srcs, repl)
            elif spinf == '全部：独立':
                srcs = self.__rng_str(filename, rrepllb, rreplrb)
                filename = self.__kill_srcs(filename, srcs, repl)
                srcs = self.__rng_str(ext, rrepllb, rreplrb)
                ext = self.__kill_srcs(ext, srcs, repl)
            elif spinf == '全部：整体':
                filename, ext = filename + ext, ''
                srcs = self.__rng_str(filename, rrepllb, rreplrb)
                filename = self.__kill_srcs(filename, srcs, repl)
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

    def __ins(self):
        # 已知欠考虑的问题：插入序号时目标文件夹内的文件，包括子文件夹内的文件，只会按一条序号线递增，
        # 不会按子文件夹为分类来新建不同的序号线。
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
                r'<([0-9]{1,10}\.[0-9]{1,10}\.[1-9]{1,10})>', form)
            begin, step, wid = map(int, re_sch.group(1).split('.'))
        for fullpath in self.__allfile():
            if insertwith == '数字序号':
                str_to_ins = form.replace(
                    re_sch.group(), f'{str(begin):0>{wid}}')
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
                    filename = self.__ins_with_pos(
                        filename, str_to_ins, insertpos)
                else:
                    filename = str_to_ins
            elif spinf == '仅限扩展名':
                if ext:
                    if instance_pos:
                        insertpos = int(ext_length * insertpos) + 1
                    if insertpos > ext_length:
                        insertpos = ext_length
                    ext = self.__ins_with_pos(ext, str_to_ins, insertpos)
                else:
                    ext = str_to_ins
            elif spinf == '全部：独立':
                if filename:
                    if instance_pos:
                        insertpos = int(filename_length * insertpos)
                    if insertpos > filename_length:
                        insertpos = filename_length
                    filename = self.__ins_with_pos(
                        filename, str_to_ins, insertpos)
                else:
                    filename = str_to_ins
                if ext:
                    if instance_pos:
                        insertpos = int(ext_length * insertpos) + 1
                    if insertpos > ext_length:
                        insertpos = ext_length
                    ext = self.__ins_with_pos(ext, str_to_ins, insertpos)
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
                    filename = self.__ins_with_pos(
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

    def __regex(self):
        spinf = self.stdict['spinf']
        repl = self.stdict['repl']
        pattern = self.stdict['pattern']
        count = self.stdict['count']
        for fullpath in self.__allfile():
            folder = os.path.dirname(fullpath)
            filename, ext = os.path.splitext(os.path.basename(fullpath))
            if spinf == '不含扩展名':
                filename = re.sub(fr'{pattern}', repl, filename, count=count)
            elif spinf == '仅限扩展名':
                ext = re.sub(fr'{pattern}', repl, ext, count=count)
            elif spinf == '全部：独立':
                filename = re.sub(fr'{pattern}', repl, filename, count=count)
                ext = re.sub(fr'{pattern}', repl, ext, count=count)
            elif spinf == '全部：整体':
                filename, ext = filename + ext, ''
                filename = re.sub(fr'{pattern}', repl, filename, count=count)
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

    def preview(self):
        '''
        预览任务执行结果。
        :return: list，成功、失败、无变化 列表。
        '''
        if not self._PREVIEWED:
            if self.stdict['head'] == 'repl':
                self.__repl()
            elif self.stdict['head'] == 'rrepl':
                self.__rrepl()
            elif self.stdict['head'] == 'insert':
                self.__ins()
            elif self.stdict['head'] == 'regex':
                self.__regex()
            self._PREVIEWED = True
        return self._successful, self._failed, self._unchanged

    def start(self):
        '''
        根据预览生成的列表执行重命名任务。
        :return: list，成功、失败、无变化 列表。
        '''
        if not self._PREVIEWED:
            self.preview()
        if not self.RENAMED:
            self.__rename()
        return self._successful, self._failed, self._unchanged


if __name__ == '__main__':
    exit('请以模块方式调用。')
