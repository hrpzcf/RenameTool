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
        self.title = title + f"\n目标文件夹：{target}"
        self.succeslist, self.presucceslist = list(), list()
        self.failedlist, self.prefailedlist = list(), list()

    def walkpath(self):
        pass

    def _rename(self):
        pass

    def _rep(self):
        """
        {'excfd': ['D:\\zz_Python\\learning'],
        'inexcext': '指定扩展名',
        'exts': ['.txt'],
        'word': True,
        'spinf': '不含扩展名',
        'head': 'rep',
        'repsrc': '1',
        'repwith': '2'}
        """
        excfd = self.stdict["excfd"]
        inexcext = self.stdict["inexcext"]
        exts = self.stdict["exts"]
        word = self.stdict["word"]
        spinf = self.stdict["spinf"]
        repsrc = self.stdict["repsrc"]
        repwith = self.stdict["repwith"]

    def _rrep(self):
        pass

    def _ins(self):
        pass

    def preview(self):
        if self.stdict["head"] == "rep":
            preresult = self._rep()
        elif self.stdict["head"] == "rrep":
            preresult = self._rrep()
        elif self.stdict["head"] == "insert":
            preresult = self._ins()
        return preresult

    def start(self):
        preresult = self.preview()


if __name__ == "__main__":
    exit(1)
