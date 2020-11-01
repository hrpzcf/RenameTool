# -*- encoding: utf-8 -*-
'''
    RenameTool 的命令行工具。
    RenameTool's command line tool.

    支持 Windows 和 Linux 系统（需安装 Python3.6 或更新版本）。
    Supports Windows and Linux systems (requires Python3.6 or later).
'''
# 尚未完成。

import os
# import re
import sys

import click

__author__ = 'hrp'
__email__ = 'pphrp@qq.com'
__version__ = '2020.0510.00 Alpha'
__file_here__ = os.path.realpath(__file__)

if len(sys.argv) >= 2 and sys.argv[1] == '-v':
    print('RenameTool %s from %s. \nAuthor: %s\nEmail: %s' %
          (__version__, __file_here__, __author__, __email__))
    sys.exit(0)


################################################################################
@click.group()
@click.option('-v',
              default=None,
              help='Show the version information of RenameTool.')
def main(v):
    ''' This is a rename tool.'''
    pass


################################################################################
@click.command('replace', help='Type <python rnt replace --help> for help.')
@click.option('--mtgs',
              prompt='Please input the targets',
              help='The target dirs or files.')
@click.option('--srcs',
              prompt='The source character string',
              help='The source strings to replace.')
@click.option('--repl',
              default='',
              help='<repl> is the character string to be \
replaced with, without the <repl> option means to delete all <srcs>.')
def __replace(mtgs, srcs, repl):
    head = 'repl'
    print('Your options are %s、%s、%s、%s。' % (head, mtgs, srcs, repl))


################################################################################
@click.command('range', help='Type <python rnt range --help> for help.')
@click.option('--mtgs',
              prompt='Please input the targets',
              help='The target dirs or files.')
@click.option('-l',
              default=None,
              help='The left bound string of the range, without the \
<-l> option means that the range starts at the beginning of the file name.')
@click.option('-r',
              default=None,
              help='The right bound string of the range, without \
the <-r> option means that the range ends at the end of the file name.')
@click.option('--repl',
              default='',
              help='<repl> is the character string to be replaced with, \
without the <repl> option means to delete all strings in the range.')
def __rangerepl(mtgs, l, r, repl):
    head = 'rrepl'
    print('Your options are %s、%s、%s、%s、%s。' % (head, mtgs, l, r, repl))


################################################################################
@click.command('insert', help='Type <python rnt insert --help> for help.')
@click.option('--mtgs',
              prompt='Please input the targets',
              help='The target dirs or files.')
@click.option('--time',
              default=None,
              help='Insert the date and time in the specified \
position of the file name, the date and time format can be customized \
(free combination of %Y,%y,%m,%d,%H,%M,%S and ordinary character string)')
@click.option('--string',
              default=None,
              help='Insert a character \
string at the specified position of the file name.')
@click.option('--serial',
              default=None,
              help='Insert the serial \
number at the specified position of the file name.')
@click.option(
    '--pos',
    default=0,
    help='The percentage or absolute value of the position to insert.')
def __insert(mtgs, time, string, serial, pos):
    head = 'insert'
    print('Your options are %s、%s、%s、%s、%s、%s。' %
          (head, mtgs, time, string, serial, pos))


################################################################################
@click.command('repy', help='Type <python rnt repy --help> for help.')
@click.option('--mtgs',
              prompt='Please input the targets',
              help='The target dirs or files.')
@click.option('--pat',
              default=None,
              help='Regular expression used to match strings.')
@click.option('--repl',
              default=None,
              help='<repl> is the string to be replaced with, without the \
<repl> option means to delete all the strings matched by the regular expression.'
              )
@click.option('--limit',
              default=None,
              help='Limit the number of replacements, the default value is 0 \
(unlimited number of times).')
def __regexpy(mtgs, pat, repl, limit):
    head = 'regex'
    print('Your options are %s、%s、%s、%s、%s。' % (head, mtgs, pat, repl, limit))


main.add_command(__replace)
main.add_command(__rangerepl)
main.add_command(__insert)
main.add_command(__regexpy)

if __name__ == '__main__':
    main()
