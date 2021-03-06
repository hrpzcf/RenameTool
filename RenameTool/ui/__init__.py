# coding: utf-8

'''
RnameTool的UI包。
'''

__all__ = list()

try:
    from RenameTool.ui.previewwd import Ui_prevwd as prevwd
    __all__.append('prevwd')
except ImportError:
    print('Importing Ui_prevwd from ui.previewwd failed.')

try:
    from RenameTool.ui.renametoolwd import Ui_rentwd as rentwd
    __all__.append('rentwd')
except ImportError:
    print('Importing Ui_rentwd from ui.renametoolwd failed.')
