
import random
from datetime import datetime
import string


def get_words(length):
    random_number = random.randint(1, 4671)
    number = 1
    with open('words.txt') as file:
        file_content = file.read()
        for word in file_content.split():
            if len(word) == length:
                if (number == random_number):
                    word_list = word
                    break
                else:
                    number += 1
    return word_list


def words(numbers):
    number = 0
    with open('words.txt') as file:
        file_content = file.read()
        for word in file_content.split():
            if len(word) == 6:
                number += 1
    return number


class Wordle:
    def __init__(self):
        self.word = get_words(5)
        self.matrix = []
        for i in range(5):
            row = []
            for j in range(5):
                row.append("_")
            self.matrix.append(row)
        self.user_input = None
        self.trys = 0
        self.check = True

    def getUserInput(self):
        self.user_input = input("Give me a 5 letter word: ")

    def drawTryMatrix(self, user_input):
        print(self.user_input, self.word)
        for i in range(5):
            print(i)
            if self.user_input[i] == self.word[i]:
                self.matrix[self.trys][i] = self.user_input[i]
            else:
                self.matrix[self.trys][i] = "_"

    def Start(self):
        while (self.check):
            self.getUserInput()
            self.drawTryMatrix(self.user_input)
            self.printMatrix()
            self.trys += 1
        print(self.trys)
    
    #def stop(self):
   #     for i in self
#
    def printMatrix(self):
        for r in self.matrix:
            print(r)

        print('test')
        print(r)    
word = Wordle()
word.Start()
