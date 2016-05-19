from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from resource.code.Error import ErrorAndQuestion

class AddWord(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(AddWord, self).__init__(parent)
        self.dictionary = {}
        self.initUI()

    def initUI(self):
        #create two label
        label1 = QtWidgets.QLabel('Current word: ')
        label2 = QtWidgets.QLabel('Translated word: ')

        #create two TextEdit for input words
        self.currentText = QtWidgets.QTextEdit()
        self.translatedText = QtWidgets.QTextEdit()
        self.currentText.setFixedSize(300, 30)
        self.translatedText.setFixedSize(300, 30)

        #create two button for add word and cancel input of word
        addButton = QtWidgets.QPushButton('&Add')
        addButton.setFixedSize(150, 50)
        cancelButton = QtWidgets.QPushButton('&Cancel')
        cancelButton.setFixedSize(150, 50)

        # set action for button
        addButton.setShortcut('Ctrl+A')
        addButton.clicked.connect(self.addWordToDictionary)
        addButton.setToolTip('Ctrl + A')

        cancelButton.setShortcut('Ctrl+Q')
        cancelButton.clicked.connect(self.close)
        cancelButton.setToolTip('Ctrl + Q')

        #set position for elements
        vboxleft = QtWidgets.QVBoxLayout()
        vboxleft.addWidget(label1, alignment=Qt.AlignLeft)
        vboxleft.addWidget(self.currentText)
        vboxleft.addWidget(label2, alignment=Qt.AlignLeft)
        vboxleft.addWidget(self.translatedText)

        vboxright = QtWidgets.QVBoxLayout()
        vboxright.addWidget(addButton)
        vboxright.addWidget(cancelButton)

        hbox = QtWidgets.QHBoxLayout()
        hbox.addLayout(vboxleft)
        hbox.addLayout(vboxright)

        #set layout eith elements
        widget = QtWidgets.QWidget()
        widget.setLayout(hbox)
        self.setCentralWidget(widget)

        #set name of window, icon, size, centered and Modality Mode
        self.setWindowTitle('Add word')
        icon = QIcon('resource/Picture/load-file.png')
        self.setWindowIcon(icon)
        self.setFixedSize(500, 125)
        self.setWindowModality(Qt.WindowModal)
        self.center()
        self.show()

    #set dictionary with word - translation
    def setDict(self, dict):
        self.dictionary = dict

    #get dictionary with added word
    def getDict(self):
        return self.dictionary

    # add word to current dictionary
    def addWordToDictionary(self):
        current = str(self.currentText.toPlainText())
        translated = str(self.translatedText.toPlainText())
        if current == '':
            message = ErrorAndQuestion('F1')
            QtWidgets.QMessageBox.question(self, message.typeOfMessage(),
                                 message.Message(), QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        elif translated == '':
            message = ErrorAndQuestion('S1')
            QtWidgets.QMessageBox.question(self, message.typeOfMessage(),
                                           message.Message(), QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        else :
            self.dictionary[current] = translated
            self.close()

    #set window to center
    def center(self):
        self.qr = self.frameGeometry()  # get frame Geometry
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()  # get center possition in our screen
        self.qr.moveCenter(cp)
        self.move(self.qr.topLeft())