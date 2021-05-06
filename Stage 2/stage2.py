word = "python"
guess = input()

print("H A N G M A N")
if guess == word:
    print("Guess the word: > {}".format(guess))
    print("You survived!")
else:
    print("Guess the word: > {}".format(guess))
    print("You are hanged!")
