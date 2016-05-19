#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from resource.code.TranslatorGUI import TranslatorGUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TranslatorGUI()
    ex.show()
    sys.exit(app.exec_())