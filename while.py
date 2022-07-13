print("\033c")
secretWord = "Tomoto"
guess = ""
guessCount = 0
guessLimit = 3

while guess != secretWord and guessCount < guessLimit:
    guess = input("Enter guess: ")
    guessCount += 1

if guessCount <= guessLimit and guess == secretWord:
    print("You win!")
else:
    print("You lose!")
