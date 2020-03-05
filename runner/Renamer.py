# coding:utf-8

"""
    版本：0.0.1
    功能：RnameTool的执行模块。
    作者：hrp
"""
import os
import sys
from time import strftime
from time import localtime


class Task(object):
    UNUSABLE = r'\/?:*"><|'

    def __init__(self, title, target, statedict):
        self.MAXLENGTH = 255
        self.target = target
        self.stdict = statedict
        self.title = title + f"\n目标文件夹：{target}\n{'-' * 42}"
        self.succesdict, self.presuccesdict = dict(), dict()
        self.faileddict, self.prefaileddict = dict(), dict()

    def allfiles(self):
        """
        返回值是排除用户要排除的文件夹、扩展名(指定或排除)后得到的所有文件路径。
        # BUG：作用范围不生效（只显示整个文件名）。
        """
        fplst = list()
        for root, dirs, files in os.walk(self.target, topdown=True):
            if root in self.stdict["excfd"]:
                # continue只能阻止walk root目录下的文件，并不能阻止继续深入root的子文件夹，配合topdown=True并实时清空dirs以阻止深入。
                dirs.clear()
                continue
            for i in files:
                if self.stdict["inexcext"] == "指定扩展名":
                    if os.path.splitext(i)[1] in self.stdict["exts"]:
                        fplst.append(os.path.join(root, i))
                else:
                    if os.path.splitext(i)[1] not in self.stdict["exts"]:
                        fplst.append(os.path.join(root, i))
                if not self.stdict["exts"]:
                    fplst.append(os.path.join(root, i))
        return fplst

    def _rename(self):
        pass

    def _replace(self, string, repsrc, repwith):
        if repsrc not in string:
            return string
        if self.stdict["word"]:
            string = string.split(" ")
            for i in range(len(string)):
                if string[i] == repsrc:
                    string[i] = repwith
            string = [i for i in string if i]
            string = " ".join(string)
        else:
            string = string.replace(repsrc, repwith)

        return string

    def _rep(self):
        spinf = self.stdict["spinf"]
        repsrc, repwith = self.stdict["repsrc"], self.stdict["repwith"]

        for file in self.allfiles():
            folder = os.path.dirname(file)
            filename, ext = os.path.splitext(os.path.basename(file))
            if spinf == "不含扩展名":
                if filename:
                    filename = self._replace(filename, repsrc, repwith)
            elif spinf == "仅限扩展名":
                if ext:
                    ext = "." + self._replace(ext[1:], repsrc, repwith)
            elif spinf == "整个文件名":
                if filename:
                    filename = self._replace(filename, repsrc, repwith)
                if ext:
                    ext = "." + self._replace(ext[1:], repsrc, repwith)

            if len(filename):
                self.presuccesdict[file] = os.path.join(folder, filename + ext)
            else:
                self.prefaileddict[file] = os.path.join(folder, filename + ext)
        print(self.presuccesdict)

    def _rrep(self):
        pass

    def _ins(self):
        pass

    def preview(self):
        if self.stdict["head"] == "rep":
            self._rep()
        elif self.stdict["head"] == "rrep":
            self._rrep()
        elif self.stdict["head"] == "insert":
            self._ins()

    def start(self):
        self.preview()
        self._rename()


if __name__ == "__main__":
    exit(1)
