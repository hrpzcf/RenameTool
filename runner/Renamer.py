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
        self.title = f'目标：< {target}\\ >\n{title}\n{"-" * 50}'
        self._successful, self._failed, self._unchanged = dict(), dict(), list()
        self._PREVIEWED, self._RENAMED = False, False

    def _allfile(self):
        ''' 返回值是排除用户要排除的文件夹、扩展名(指定或排除)后得到的所有文件路径。'''
        fplst = list()
        for root, dirs, files in os.walk(self.target, topdown=True):
            if root in self.stdict['excfd']:
                dirs.clear()
                continue
            for i in files:
                if self.stdict['inexcext'] == '指定扩展名':
                    if os.path.splitext(i)[1] in self.stdict['exts']:
                        fplst.append(os.path.join(root, i))
                elif self.stdict['inexcext'] == '排除扩展名':
                    if os.path.splitext(i)[1] not in self.stdict['exts']:
                        fplst.append(os.path.join(root, i))
                if not self.stdict['exts']:
                    fplst.append(os.path.join(root, i))
        return fplst

    def _rename(self):
        self._RENAMED = True
        print('renamed!')

    def _rng_str(self, string, rrepllb, rreplrb):
        ''' 寻找符合给定范围的字符串(从左至右一次匹配，既不是最短匹配，也不是最长匹配)，并返回找到的字符串列表。'''
        # 还不会用正则表达式，只能应付一下了 :)
        tglist, lthlb, lthrb = list(), len(rrepllb), len(rreplrb)
        while (lth := len(string)):
            begin, end = None, None
            if rrepllb:
                if (tmp := string.find(rrepllb)) == -1:
                    break
                begin = tmp
            else:
                begin = 0
            if begin is None:
                break
            if rreplrb:
                if (tmp := string[begin + lthlb:].find(rreplrb)) == -1:
                    break
                end = begin + lthlb + tmp + lthrb
            else:
                end = lth
            if end is None:
                break
            tglist.append(string[begin: end])
            string = string[end:]
        return tglist

    def _rng_pos(self):
        pass

    def _repl_word(self, string, replsrc, replwith):
        if replsrc not in string:
            return string
        # 以空格为分隔的单词模式没那么简单，这里先应付一下。
        if self.stdict['word']:
            tmp = string.split(' ')
            if replsrc in tmp:
                for i in range(len(tmp)):
                    if tmp[i] == replsrc:
                        tmp[i] = replwith
                tmp = [i for i in tmp if i]
                string = ' '.join(tmp)
        else:
            string = string.replace(replsrc, replwith)
        return string

    def _kill_srcs(self, string, replsrcs, replwith):
        for src in replsrcs:
            string = self._repl_word(string, src, replwith)
        return string

    def _repl(self):
        replsrcs = self.stdict['replsrcs']
        replwith = self.stdict['replwith']
        spinf = self.stdict['spinf']
        for fullpath in self._allfile():
            folder = os.path.dirname(fullpath)
            filename, ext = os.path.splitext(os.path.basename(fullpath))
            if spinf == '不含扩展名':
                filename = self._kill_srcs(filename, replsrcs, replwith)
            elif spinf == '仅限扩展名':
                ext = self._kill_srcs(ext, replsrcs, replwith)
            elif spinf == '全部：独立':
                filename = self._kill_srcs(filename, replsrcs, replwith)
                ext = self._kill_srcs(ext, replsrcs, replwith)
            elif spinf == '全部：整体':
                filename, ext = filename + ext, ''
                filename = self._kill_srcs(filename, replsrcs, replwith)
            fullpath_new = os.path.join(folder, filename + ext)
            # TODO win10支持只有扩展名没有前缀的文件名形式。这里需要改动。
            if len(filename) and (len(fullpath_new) in range(1, self.MAXLENGTH)):
                if fullpath != fullpath_new:
                    self._successful[fullpath] = fullpath_new
                else:
                    self._unchanged.append(fullpath)
            else:
                self._failed[fullpath] = fullpath_new

    def _rrepl(self):
        rrepllb = self.stdict['rrepllb']
        rreplrb = self.stdict['rreplrb']
        spinf = self.stdict['spinf']
        replwith = self.stdict['rreplwith']
        if not self.stdict['inclb']:
            replwith = rrepllb + replwith
        if not self.stdict['incrb']:
            replwith += rreplrb
        for fullpath in self._allfile():
            folder = os.path.dirname(fullpath)
            filename, ext = os.path.splitext(os.path.basename(fullpath))
            if spinf == '不含扩展名':
                replsrcs = self._rng_str(filename, rrepllb, rreplrb)
                filename = self._kill_srcs(filename, replsrcs, replwith)
            elif spinf == '仅限扩展名':
                replsrcs = self._rng_str(ext, rrepllb, rreplrb)
                ext = self._kill_srcs(ext, replsrcs, replwith)
            elif spinf == '全部：独立':
                replsrcs = self._rng_str(filename, rrepllb, rreplrb)
                filename = self._kill_srcs(filename, replsrcs, replwith)
                replsrcs = self._rng_str(ext, rrepllb, rreplrb)
                ext = self._kill_srcs(ext, replsrcs, replwith)
            elif spinf == '全部：整体':
                filename, ext = filename + ext, ''
                replsrcs = self._rng_str(filename, rrepllb, rreplrb)
                filename = self._kill_srcs(filename, replsrcs, replwith)
            fullpath_new = os.path.join(folder, filename + ext)
            # TODO win10支持只有扩展名没有前缀的文件名形式。这里需要改动。
            if len(filename) and (len(fullpath_new) in range(1, self.MAXLENGTH)):
                if fullpath != fullpath_new:
                    self._successful[fullpath] = fullpath_new
                else:
                    self._unchanged.append(fullpath)
            else:
                self._failed[fullpath] = fullpath_new

    def _ins(self):
        # TODO 插入日期时间
        insertwith, form = self.stdict['insert'], self.stdict['form']
        insertpos, spinf = self.stdict['insertpos'], self.stdict['spinf']
        if insertwith == '日期时间':
            pass
        elif insertwith == '普通字符':
            replwith = form
        elif insertwith == '数字序号':
            pass
        for fullpath in self._allfile():
            folder = os.path.dirname(fullpath)
            filename, ext = os.path.splitext(os.path.basename(fullpath))
            if spinf == '不含扩展名':
                pass
            elif spinf == '仅限扩展名':
                pass
            elif spinf == '全部：独立':
                pass
            elif spinf == '全部：整体':
                pass

    def reset(self):
        ''' 重置任务的预览和重命名状态(不还原文件名)，没什么作用。'''
        self._RENAMED = False
        self._PREVIEWED = False

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
        if not self._RENAMED:
            self._rename()
        return self._successful, self._failed, self._unchanged


if __name__ == '__main__':
    exit(0)
    # self = Task("test",r'D:\zz_Python\testarea',{'inclb':True,'incrb':True})
    # for i in os.listdir(r'D:\zz_Python\testarea'):
    #     self._rng_str(i[:-4],"6","5")
