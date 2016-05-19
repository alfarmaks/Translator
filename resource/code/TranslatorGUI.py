from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from resource.code.Error import ErrorAndQuestion
from resource.code.Dictionary import Dictionary
from resource.code.AddWord import AddWord


class TranslatorGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(TranslatorGUI, self).__init__()
        self.dictionary = Dictionary()
        self.saveDict = False
        self.saveDictPath = ''
        self.saveTranslate = False
        self.saveTranslatePath = ''
        self.initUI()

    # init widget
    def initUI(self):

        #create QFileDialog and filters
        self.filters = "Text files (*.txt);;All files (*.*)"
        self.selected_filter = "Text files (*.txt)"

        #self.statusBar().showMessage('Ready')

        #create two text editors, two labels and two buttons
        label1 = QtWidgets.QLabel('Current English text: ')
        label2 = QtWidgets.QLabel('Translated text: ')
        self.translatedText = QtWidgets.QTextEdit()
        self.currentText = QtWidgets.QTextEdit()
        self.translateButton = QtWidgets.QPushButton('&Translate')
        self.saveButton = QtWidgets.QPushButton('&Save')

        #set size
        self.translateButton.setFixedSize(150, 50)
        self.saveButton.setFixedSize(150, 50)
        label1.setFixedSize(150, 20)
        label2.setFixedSize(150, 20)
        self.currentText.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.translatedText.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        #set action for button
        self.translateButton.setShortcut('Ctrl+T')
        self.translateButton.clicked.connect(self.translateButtonClicked)
        self.translateButton.setToolTip('Ctrl + T')

        self.saveButton.clicked.connect(self.saveFileDialog)
        self.saveButton.setToolTip('Ctrl + S')

        #create QHBoxLayout with two QLabels and add it to widget
        hlabel = QtWidgets.QHBoxLayout()
        hlabel.addWidget(label1)
        hlabel.addItem(QtWidgets.QSpacerItem(
            340, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        hlabel.addWidget(label2)
        topW = QtWidgets.QWidget()
        topW.setLayout(hlabel)

        # create QHBoxLayout with two QTextEdit and add it to widget
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.currentText)
        hbox.addWidget(self.translatedText)

        # create QHBoxLayout with two QPushButtons and add it to widget
        hbutton = QtWidgets.QHBoxLayout()
        hbutton.addWidget(self.translateButton)
        hbutton.addWidget(self.saveButton)
        botW = QtWidgets.QWidget()
        botW.setLayout(hbutton)

        #add labels, textEdits, buttons to QVBoXLayout
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(topW, alignment=Qt.AlignLeft)
        vbox.addLayout(hbox)
        vbox.addWidget(botW, alignment=Qt.AlignRight)

        #set Layout with elements
        widget = QtWidgets.QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.initMenuBar()
        self.setWindowTitle('Translator')
        icon = QIcon('resource/Picture/dictionary.png')
        self.setWindowIcon(icon)
        self.setFixedSize(1000, 600)
        self.center()

    # move widget to center
    def center(self):
        self.qr = self.frameGeometry()  # get frame Geometry
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()  # get center possition in our screen
        self.qr.moveCenter(cp)
        self.move(self.qr.topLeft())

    # Create Menubar
    def initMenuBar(self):
        # create button for exit action
        exitAction = QtWidgets.QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)
        exitAction.setToolTip('Ctrl + Q')

        # create button for Open action
        openAction = QtWidgets.QAction('&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.openFileDialog)
        openAction.setToolTip('Ctrl + O')

        # create button for save action
        saveAction = QtWidgets.QAction('&Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveFileDialog)
        saveAction.setToolTip('Ctrl + S')

        # create button for save as action
        saveAsAction = QtWidgets.QAction('&Save as', self)
        saveAsAction.setShortcut('Ctrl+Shift+S')
        saveAsAction.triggered.connect(self.saveAsFileDialog)
        saveAsAction.setToolTip('Ctrl + Shift + S')

        #create button open dictionary
        addDict = QtWidgets.QAction('&Dictionary', self)
        addDict.setShortcut('Ctrl+D')
        addDict.triggered.connect(self.loadDictDialog)
        addDict.setToolTip('Ctrl + D')

        #create button add word
        addWord = QtWidgets.QAction('&Word', self)
        addWord.setShortcut('Ctrl+W')
        addWord.triggered.connect(self.addWordToDictionary)
        addWord.setToolTip('Ctrl + W')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)
        fileMenu.addAction(exitAction)
        fileMenu.addAction(exitAction)

        addMenu = menubar.addMenu("&Add...")
        addMenu.addAction(addDict)
        addMenu.addAction(addWord)

    def closeEvent(self, event):
        message = ErrorAndQuestion('E')
        reply = QtWidgets.QMessageBox.question(self, message.typeOfMessage(),
                                     message.Message(), QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.saveDictDialog()
            self.saveFileDialog()
            event.accept()
        else:
            event.ignore()

    def loadDictDialog(self):
        dlg = QtWidgets.QFileDialog()
        #get file path
        fname = dlg.getOpenFileName(self, 'Open dictionry', '',
                                         self.filters, self.selected_filter)[0]
        #if all is ok save path and load dictionary to program
        if fname is not '':
            f = open(fname, 'r')
            self.saveDict = True
            self.saveDictPath = fname
            data = [str(key) for key in f.read().split()]
            f.close()
            if len(data) % 2 == 0:
                for i in range(0, len(data), 2):
                    #create dictionary from file
                    self.dictionary.addWord(data[i], data[i+1])
            else :
                for i in range(0, len(data) - 1, 2):
                    # if last word don't have translation
                    self.dictionary.addWord(data[i], data[i+1])
                self.dictionary.addWord(data[len(data)-1], '@')
        #else error with file path
        else:
            message = ErrorAndQuestion(1)
            QtWidgets.QMessageBox.question(self, message.typeOfMessage(),
                                 message.Message(), QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    #event for file + open. Load file with text for translation
    def openFileDialog(self):
        dlg = QtWidgets.QFileDialog()
        # get file path
        fname = dlg.getOpenFileName(self, 'Open file with text', '',
                                         self.filters, self.selected_filter)[0]

        # if all is ok ...
        if fname is not '':
            f = open(fname, 'r')
            self.currentText.setText(str(f.read()))
            f.close()
        # else error with file path
        else:
            message = ErrorAndQuestion(1)
            QtWidgets.QMessageBox.question(self, message.typeOfMessage(),
                                 message.Message(), QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    #event for file + save as
    def saveAsFileDialog(self):
        dlg = QtWidgets.QFileDialog()
        # get file path
        fname = dlg.getSaveFileName(self, 'Save file as ...', 'translated.txt',
                                         self.filters, self.selected_filter)[0]
        # if all is ok write to file which locate in file path and save it path
        if fname is not '':
            f = open(fname, 'w')
            f.write(str(self.translatedText.toPlainText()))
            self.saveTranslate = True
            self.saveTranslatePath = fname
            f.close()
        # else error with file path
        else :
            message = ErrorAndQuestion(1)
            QtWidgets.QMessageBox.question(self, message.typeOfMessage(),
                                 message.Message(), QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    #event for file + save. Save translation if we use save as before else we call save as
    def saveFileDialog(self):
        if self.saveTranslate == True:
            f = open(self.saveTranslatePath, 'w')
            f.write(str(self.translatedText.toPlainText()))
            f.close()
        else :
            self.saveAsFileDialog()

    #save dictionary to open file with dictionary
    def saveDictDialog(self):
        if self.saveDict == True:
            f = open(self.saveDictPath, 'w')
            data = ''
            dictionary = self.dictionary.getDict()
            for key in dictionary.keys():
                data = data + key + ' ' + dictionary[key] + '\n'
            f.write(data)
            f.close()

    #event for translateButton. Translate current text
    def translateButtonClicked(self):
        if self.saveDict == True:
            result = self.dictionary.trasnlateText(str(self.currentText.toPlainText()))
            self.translatedText.setText(result[0])
            message = ErrorAndQuestion('A')
            QtWidgets.QMessageBox.question(self, message.typeOfMessage(),
                                 message.Message() + str(result[1]) + ' words.', QtWidgets.QMessageBox.Ok,
                                           QtWidgets.QMessageBox.Ok)
        else :
            message = ErrorAndQuestion('~')
            reply = QtWidgets.QMessageBox.question(self, message.typeOfMessage(),
                                 message.Message(), QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes,
                                                   QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                self.loadDictDialog()

    #event for add... + word. Of course add word to our dictionary
    def addWordToDictionary(self):
        word = AddWord(self)
        word.setDict(self.dictionary.getDict())
        self.dictionary.setDict(word.getDict())