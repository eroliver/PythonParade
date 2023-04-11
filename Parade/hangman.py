from random import randint
from os import listdir, getcwd, path
from getpass import getpass

mistakesMade = 0
letters = []
parentFolder = "word_list"
fileNames = listdir(parentFolder)
fileList = [(path.join(getcwd(), parentFolder, fileName)) for fileName in fileNames]

HANGMAN_PICS = ['''
  3.   +---+
  4.       |
  5.       |
  6.       |
  7.      ===''', '''
  8.   +---+
  9.   O   |
 10.       |
 11.       |
 12.      ===''', '''
 13.   +---+
 14.   O   |
 15.   |   |
 16.       |
 17.      ===''', '''
 18.   +---+
 19.   O   |
 20.  /|   |
 21.       |
 22.      ===''', '''
 23.   +---+
 24.   O   |
 25.  /|\  |
 26.       |
 27.      ===''', '''
 28.   +---+
 29.   O   |
 30.  /|\  |
 31.  /    |
 32.      ===''', '''
 33.   +---+
 34.   O   |
 35.  /|\  |
 36.  / \  |
 37.      ===''']

def main():
    # Ask how many players
    numberOfPlayers = int(input("How many players?(enter 1 or 2) "))

    if numberOfPlayers == 2:
        TwoPlayerLoop()
    elif numberOfPlayers == 1:
        SinglePlayerLoop()
    else:
        print("Sorry, but only 1 and 2 player versions are available.")

def TwoPlayerLoop():
    global mistakesMade
    print("Player 1, please enter the word for player 2 to guess: ")
    secretWord = getpass()
    while(mistakesMade < 6):

        print("Player 2, you have {} guesses remaining.".format(6 - mistakesMade))
        letterGuessed = input("Player 2 please guess a letter: ")
        letters.append(letterGuessed)
        if letterGuessed in secretWord:
            print("Correct!")
        else:
            print("Incorrect!")
            mistakesMade += 1

        print(letters)
        encodedWord = GetHiddenstring(secretWord, letters)
        print(encodedWord)
        print(HANGMAN_PICS[mistakesMade])
        if '*' not in encodedWord:
            break

    if mistakesMade >= 6:
        print("Congratulations Player 1! The word was {}!".format(secretWord))
    else:
        print("Congratulations Player 2!")
    
def  GetHiddenstring(word: str, letters: list):
    encodedWord = word
    for letter in word:
        if letter not in letters:
            encodedWord = encodedWord.replace(letter, "*")
    return encodedWord

def SinglePlayerLoop():
    global mistakesMade
    secretWord = GetSecretWord()
    while(mistakesMade < 6):

        print("Player, you have {} guesses remaining.".format(6 - mistakesMade))
        letterGuessed = input("Please guess a letter: ")
        letters.append(letterGuessed)
        if letterGuessed in secretWord:
            print("Correct!")
        else:
            print("Incorrect!")
            mistakesMade += 1

        print(letters)
        encodedWord = GetHiddenstring(secretWord, letters)
        print(encodedWord)
        print(HANGMAN_PICS[mistakesMade])
        if '*' not in encodedWord:
            break

    if mistakesMade >= 6:
        print("Too Bad! The word was {}!".format(secretWord))
    else:
        print("Congratulations Player!")
    
def  GetHiddenstring(word: str, letters: list):
    encodedWord = word
    for letter in word:
        if letter not in letters:
            encodedWord = encodedWord.replace(letter, "*")
    return encodedWord

def GetSecretWord():
    wordList = fileList[randint(0, len(fileList))]
    with open(wordList,'r') as file:
        words = file.readlines()
    return((words[randint(0,len(words))]).strip())

if __name__ == "__main__":
    main()
