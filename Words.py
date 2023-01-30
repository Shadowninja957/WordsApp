from Categories import *
import random

class Word:

    def __init__(self, word):
        self.word = word

    def getWord(self):
        return self.word


class WordBank:

    def __init__(self):
        self.wordPool = {
                Anatomy().getCategory(): [],
                People().getCategory(): [],
                Animal().getCategory(): [],
                Place().getCategory(): [],
                Thing().getCategory(): [],
                Movie().getCategory(): [],
                TvShow().getCategory(): [],
                Anime().getCategory(): [],
                Cartoon().getCategory(): [],
                Music().getCategory(): [],
                Art().getCategory(): [],
                Verb().getCategory(): [],
                Adjective().getCategory(): [],
                Food().getCategory(): [],
                Drink().getCategory(): [],
                CustomWord().getCategory(): [],
                LeagueOfLegends().getCategory(): [],
                Apex().getCategory(): [],
                Overwatch().getCategory(): [],
                Color().getCategory(): [],
                Astrology().getCategory(): []
            }


    def getAllWords(self):
        return self.wordPool

    def getSelectedWordList(self, category):
        value = self.wordPool.get(category.getCategory())
        return value
        
    def checkDuplicate(self, word, category):
        words = self.getSelectedWordList(category)
        if words is None:
            return False

        for item in words:
            if item.getWord() == word:
                return True
        return False

    def addWordsToCategory(self, word, category):
        if self.checkDuplicate(word, category) is False:
            self.wordPool[category.getCategory()].append(Word(word))

                    
class WordGeneratorClient:

    def __init__(self):
        self.wordBank = WordBank()

    def loadWords(self):

        wordP = self.wordBank.getAllWords()
        file = open("allWords", "r")
        word = file.readline()
        while word is not "":
            if word.__contains__("*"):
                category = word.strip("*").strip().strip("\n")
            else:
                word.strip().strip("\n")
                wordP[category].append(Word(word))
            word = file.readline()
                            
        file.close()

    def saveWords(self):

        file = open("allWords", "w")
        for key, value in self.wordBank.wordPool.items():
            key = "*" + key
            file.write(key + "\n")
            for item in value:
                file.write(item.getWord()+"\n")

        file.close()

    # 25 words Pack Name is just the name of the txt file
    # check for duplicate words 
    def generateSmallWordPack(self, packName, categories):
        file = open(packName, "w")
        # numWords = int(25/len(categories))
        # reminder = int(25%len(categories))
        ranWords = []

        for category in categories:
            wordList = self.wordBank.getSelectedWordList(category)  
            ranWords.extend(wordList)
        
        ranWords = random.choices(ranWords, k=25)
            # if reminder > 0:
            #     randomNumber = random.randint(1, reminder)
            #     ranWords.extend(random.choices(wordList, k=randomNumber))
            #     reminder -= randomNumber
        
        for item in ranWords:
            file.write(item.getWord())
        file.close()

    # 400 words Pack Name is just the name of the txt file
    def generateLargeWordPack(self, packName, categories):
        file = open(packName, "w")
        ranWords = []

        for category in categories:
            wordList = self.wordBank.getSelectedWordList(category)  
            ranWords.extend(wordList)
        
        ranWords = random.choices(ranWords, k=400)
        
        for item in ranWords:
            file.write(item.getWord())
        file.close()


# c1 = WordBank()
# print(c1.addWordsToCategory("Comet", Astrology()))
# print(c1.getSelectedWordList(Astrology()))
# print(c1.checkDuplicate("Comet", Astrology()))


# word = WordGeneratorClient()
# word.loadWords()
# word.generateLargeWordPack("5words.txt", [Anatomy(), People(), Animal(), Place(), Thing()])
# word.saveWords()
# list = word.wordBank.getSelectedWordList(People())
# for item in list:
#     print(item.getWord())
