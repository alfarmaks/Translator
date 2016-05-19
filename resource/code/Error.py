class ErrorAndQuestion():

    def __init__(self, typeOfQuery):
        super(ErrorAndQuestion, self).__init__()
        self.error = typeOfQuery
        self.message = ''
        self.checkType()

    #check type of message
    def checkType(self):
        if self.error == 1:
            self.error = 'Error 1'
            self.message = 'Incorrect file path'
        elif self.error == 'E':
            self.error = 'Exit'
            self.message = 'Are you sure to quit?'
        elif self.error == '~':
            self.error = 'There are no words in the dictionary'
            self.message = 'Do you want to load dictionary?'
        elif self.error == 'A':
            self.error = 'Successful translation'
            self.message = 'In summary was translated '
        elif self.error == 'F1':
            self.error = 'Error adding'
            self.message = 'Please, add word for translation.'
        elif self.error == 'S1':
            self.error = 'Error adding'
            self.message = 'Please, add translation of the word.'

    #get type of query
    def typeOfMessage(self):
        return str(self.error)

    #get message which connected with query
    def Message(self):
        return str(self.message)