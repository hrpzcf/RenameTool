# coding: utf-8

# 版本：0.0.1
# 功能：RnameTool的历史记录模块。
# 作者：hrp


from time import localtime
from time import strftime
import random
import os
import sys


class wLog(object):
    def __init__(self, title):
        self.title = title
        self.time = f'操作时间：{strftime("[%Y-%m-%d，%H:%M:%S]", localtime())}'

    def write(self):
        pass

    def close(self):
        pass


class rLog(object):
    def __init__(self):
        pass

    def history(self):
        pass

    def restore(self):
        pass
