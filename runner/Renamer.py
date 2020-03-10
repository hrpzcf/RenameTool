# coding:utf-8

# 版本：0.0.1
# 功能：RnameTool的任务模块。
# 作者：hrp

import os
from time import localtime, strftime


class Task(object):
    def __init__(self, title, target, statedict):
        self.MAXLENGTH = 256
        self.target = target
        self.stdict = statedict
        self.title = f'目标：< {target} >\n{title}\n{"-" * 50}'
        self.successful, self.failed, self.unchanged = dict(), dict(), list()
        self._PREVIEWED, self._RENAMED = False, False

    def _allfiles(self):
        ''' 返回值是排除用户要排除的文件夹、扩展名(指定或排除)后得到的所有文件路径 '''
        fplst = list()
        for root, dirs, files in os.walk(self.target, topdown=True):
            if root in self.stdict['excfd']:
                # 配合topdown=True并实时清空dirs以阻止深入子目录。
                dirs.clear()
                continue
            for i in files:
                if self.stdict['inexcext'] == '指定扩展名':
                    if os.path.splitext(i)[1] in self.stdict['exts']:
                        fplst.append(os.path.join(root, i))
                else:
                    if os.path.splitext(i)[1] not in self.stdict['exts']:
                        fplst.append(os.path.join(root, i))
                if not self.stdict['exts']:
                    fplst.append(os.path.join(root, i))
        return fplst

    def _rename(self):
        self._RENAMED = True
        print('renamed!')

    def _rg_str(self, string, rreplb, rreprb):
        ''' 寻找符合给定范围的字符串(从左至右一次匹配，不是最短匹配，也不是最长匹配)，并返回找到的字符串列表 '''
        tglist = list()
        lthlb, lthrb = len(rreplb), len(rreprb)
        while (lth := len(string)):
            begin, end = None, None
            if rreplb:
                if (tmp := string.find(rreplb)) == -1:
                    break
                begin = tmp
            else:
                begin = 0
            if begin is None:
                break
            if rreprb:
                if (tmp := string[begin + lthlb:].find(rreprb)) == -1:
                    break
                end = begin + lthlb + tmp + lthrb
            else:
                end = lth
            if end is None:
                break
            tglist.append(string[begin: end])
            string = string[end:]
        return tglist

    def _rg_num(self):
        ''' 空函数。'''
        pass

    def _replace(self, string, repsrc, repwith):
        if repsrc not in string:
            return string
        if self.stdict['word']:
            tmp = string.split(' ')
            if repsrc in tmp:
                for i in range(len(tmp)):
                    if tmp[i] == repsrc:
                        tmp[i] = repwith
                tmp = [i for i in tmp if i]
                string = ' '.join(tmp)
        else:
            string = string.replace(repsrc, repwith)
        return string

    def _rep(self):
        spinf = self.stdict['spinf']
        repsrc, repwith = self.stdict['repsrc'], self.stdict['repwith']
        for fullpath in self._allfiles():
            folder = os.path.dirname(fullpath)
            filename, ext = os.path.splitext(os.path.basename(fullpath))
            if spinf == '不含扩展名':
                if filename:
                    filename = self._replace(filename, repsrc, repwith)
            elif spinf == '仅限扩展名':
                if ext:
                    ext = '.' + self._replace(ext[1:], repsrc, repwith)
            elif spinf == '整个文件名':
                if filename:
                    filename = self._replace(filename, repsrc, repwith)
                if ext:
                    ext = '.' + self._replace(ext[1:], repsrc, repwith)
            fullpath_new = os.path.join(folder, filename + ext)
            if len(filename) and (len(fullpath_new) in range(1, self.MAXLENGTH)):
                if fullpath != fullpath_new:
                    self.successful[fullpath] = fullpath_new
                else:
                    self.unchanged.append(fullpath)
            else:
                self.failed[fullpath] = fullpath_new

    def _rrep(self):
        rreplb, rreprb = self.stdict['rreplb'], self.stdict['rreprb']
        spinf, rrepwith = self.stdict['spinf'], self.stdict['rrepwith']
        if not self.stdict['inclb']:
            rrepwith = rreplb + rrepwith
        if not self.stdict['incrb']:
            rrepwith += rreprb
        for fullpath in self._allfiles():
            folder = os.path.dirname(fullpath)
            filename, ext = os.path.splitext(os.path.basename(fullpath))
            if spinf == '不含扩展名':
                if filename:
                    srcs = self._rg_str(filename, rreplb, rreprb)
                    for i in srcs:
                        filename = self._replace(filename, i, rrepwith)
            elif spinf == '仅限扩展名':
                if ext:
                    srcs = self._rg_str(ext[1:], rreplb, rreprb)
                    for i in srcs:
                        ext = self._replace(ext, i, rrepwith)
                    ext = '.' + ext
            elif spinf == '整个文件名':
                if filename:
                    srcs = self._rg_str(filename, rreplb, rreprb)
                    for i in srcs:
                        filename = self._replace(filename, i, rrepwith)
                if ext:
                    srcs = self._rg_str(ext[1:], rreplb, rreprb)
                    for i in srcs:
                        ext = self._replace(ext, i, rrepwith)
                    ext = '.' + ext
            fullpath_new = os.path.join(folder, filename + ext)
            if len(filename) and (len(fullpath_new) in range(1, self.MAXLENGTH)):
                if fullpath != fullpath_new:
                    self.successful[fullpath] = fullpath_new
                else:
                    self.unchanged.append(fullpath)
            else:
                self.failed[fullpath] = fullpath_new

    def _ins(self):
        pass

    def preview(self):
        if not self._PREVIEWED:
            if self.stdict['head'] == 'rep':
                self._rep()
            elif self.stdict['head'] == 'rrep':
                self._rrep()
            elif self.stdict['head'] == 'insert':
                self._ins()
            self._PREVIEWED = True
        return self.successful, self.failed, self.unchanged

    def start(self):
        if not self._PREVIEWED:
            self.preview()
        if not self._RENAMED:
            self._rename()
        return self.successful, self.failed, self.unchanged


if __name__ == '__main__':
    exit(0)
    # self = Task("test",r'D:\zz_Python\testarea',{'inclb':True,'incrb':True})
    # for i in os.listdir(r'D:\zz_Python\testarea'):
    #     self._rg_str(i[:-4],"6","5")
