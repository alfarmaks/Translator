import re
class Dictionary():

    def __init__(self):
        super(Dictionary, self).__init__()
        self.dictionary = {}

    #add word to dictionary
    def addWord(self, word, traslation):
        self.dictionary[word] = traslation

    #get dictionary
    def getDict(self):
        return self.dictionary

    #set dictionary with word - translation
    def setDict(self, dictionary):
        self.dictionary = dictionary

    #translate current text using loaded dictionary
    def trasnlateText(self, text):
        res = ()
        num = 0
        for key in self.dictionary.keys():
            word = r'\b'+re.escape(re.escape(key))+ r'\b'
            #replace word to translation and get tuple(text, replace_words). Ignore case
            res = re.subn(word, self.dictionary[key], text, flags=re.IGNORECASE)
            text = res[0]
            num = num + res[1]
        res = (res[0], )
        res = res + (num, )
        return res