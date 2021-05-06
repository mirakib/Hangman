import random
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
guess = input()
print("H A N G M A N")
if guess == word:
    print("Guess the word: > {}".format(guess))
    print("You survived!")
else:
    print("Guess the word: > {}".format(guess))
    print("You are hanged!")
