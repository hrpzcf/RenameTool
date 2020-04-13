# -*- encoding: utf-8 -*-
'''
--------------------------------------
@Version   : 20.0413.00
@Author    : hrp
@Desciption: RnameTool的历史记录模块。
--------------------------------------
'''
# TODO: 这个模块刚开始写，想法不成熟，写的很乱，预想的功能有：
#   *有限的文件重命名跟踪记录(同一个文件: 文件名1 -> 文件名2 -> 文件名3 ...)；
#   记录文件以文本方式保存，可以用记事本打开查看；
#   有友好的文本格式，方便查看；
#   历史记录管理接口，方便主程序调用、显示；
#   模块单独拿出来也可以给别的程序使用；
#   等等…

from time import localtime
from time import strftime
import random
import os
import sys


class wLog(object):
    def __init__(self, title):
        self.setspath = os.path.join(os.path.realpath('..'), 'logs')
        if not os.path.exists(self.setspath):
            # 无法创建文件夹则报错退出。
            os.mkdir(self.setspath)
        elif os.path.isfile(self.setspath):
            raise Exception('logs文件夹名被文件占用！')
        self.time = strftime("[%Y-%m-%d %H-%M-%S]", localtime())
        self.title = ''.join((self.time, title))
        self.filehd = None
        self.filename = self.__mkfilename()
        if self.filename:
            # 无法创建文件则报错退出。
            self.filehd = open(os.path.join(
                self.setspath, self.filename), 'wt', encoding='utf-8')
            self.filehd.write(''.join((self.title, f'\n{"-" * 50}')))

    def __mkfilename(self):
        filename = '-'.join((self.title, f'{str(abs(hash(self.title))):0>10}',
                             str(random.randrange(10000, 100000)))) + '.log'
        if os.path.exists(os.path.join(self.setspath, filename)):
            return self.__mkfilename()
        else:
            return filename

    def write(self, string1, string2):
        if self.filehd:
            self.filehd.write('\n')
            string = ''.join((
                '重命名前：', string1, '\n', '重命名后：', string2, f'\n{"-" * 50}'))
            self.filehd.write(string)
        # return self.filename

    def close(self):
        if self.filehd:
            self.filehd.close()


class rLog(object):
    def __init__(self):
        pass

    def history(self):
        pass

    def restore(self):
        pass
