

import random
from datetime import datetime
import string




class Wordle:
    def __init__(self):
        self.word = None
        self.matrix = []
        self.user_input = None
        self.trys = 0
        self.check = True
        self.wordLength = 5


    def getUserInput(self):
        self.user_input = input("Give me a " + str(self.wordLength) + " letter word: ")


    def drawTryMatrix(self):
        print(f"Debug: {self.user_input}, {self.word}")
        for i in range(self.wordLength):
            num = 0
            if self.user_input[i] == self.word[i]:
                self.matrix[self.trys][i] = self.user_input[i]
                num += 1
                print(num)
            else:
                self.matrix[self.trys][i] = "_"
                num = 0
        if (num == 5):
            self.check = False
    def wordLength1(self):
        while True:
            self.wordLength = input("Word Length: ")
            if self.wordLength.isdigit():
                self.wordLength = int(self.wordLength)
                if 0 < self.wordLength < 12:
                    break
                else:
                    print("Please enter a word length from 1 to 12.")
            else:
                print("Please enter a valid integer.")


    def Start(self):
        self.wordLength1()
        self.get_words(self.wordLength)
        print(f"Check Now: {self.word}")
        for i in range(self.wordLength):
            row = []
            for j in range(self.wordLength):
                row.append("_")
            self.matrix.append(row)
        while (self.check):
            self.getUserInput()
            if (len(self.user_input) != self.wordLength):
                self.getUserInput()
            else:
                print("Before: " + str(self.user_input) + ", " + str(self.word))
                self.drawTryMatrix()
                self.printMatrix()
                self.trys += 1
                self.checkfullword()
               


    def printMatrix(self):
        for r in self.matrix:
            print(r)


    def checkfullword(self):
        for i in range(self.wordLength):
            if(self.user_input[i] != self.word[i]):
                break
            else:
                self.check = False
                print("Contrats you got the Word in " + str(self.trys))
    def get_words(self, length):
        random_number = random.randint(1, 4671)
        number = 1
        word_list = ""
        with open('words.txt') as file:
            file_content = file.read()
            for word in file_content.split():
                if len(word) == length:
                    if (number == random_number):
                        word_list = word
                        break
                    else:
                        number += 1
        if word_list is None:
            print(f"No word found with length {length}")
            return None
        else:
            self.word = word_list
'''
    def words(self, numbers):
        number = 0
        with open('words.txt') as file:
            file_content = file.read()
            for word in file_content.split():
                if len(word) == 6:
                    number += 1
        return number


'''
word = Wordle()
word.Start()





