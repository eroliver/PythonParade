

mistakesRemaining = 6
letters = []

def main():
    # Ask how many players
    numberOfPlayers = int(input("How many players?(enter 1 or 2) "))

    if numberOfPlayers == 2:
        TwoPlayerLoop()



def TwoPlayerLoop():
    global mistakesRemaining
    secretWord = input("Player 1, please enter the word for player 2 to guess: ")
    while(mistakesRemaining > 0):

        print("Player 2, you have {} guesses remaining.".format(mistakesRemaining))
        letterGuessed = input("Player 2 please guess a letter: ")
        letters.append(letterGuessed)
        if letterGuessed in secretWord:
            print("Correct!")
        else:
            print("Incorrect!")
            mistakesRemaining = mistakesRemaining - 1

        print(GetHiddenstring(secretWord, letters))

    if mistakesRemaining <= 0:
        print("Congratulations Player 1!")
    else:
        print("Congratulations Player 2!")
    
def  GetHiddenstring(word: str, letters: list):
    encodedWord = word
    for letter in word:
        if letter not in letters:
            encodedWord = encodedWord.replace(letter, "*")
    return encodedWord

if __name__ == "__main__":
    main()
