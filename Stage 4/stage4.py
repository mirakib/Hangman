import random

words = ['python', 'java', 'kotlin', 'javascript']
random.seed()
secret_word = random.choice(words)

incomplete_word = secret_word[0:3] + "-" * (len(secret_word) - 3)

print("H A N G M A N")
guess = input("Guess the word {}: > ".format(incomplete_word))

if guess == secret_word:
    print("You survived!")
else:
    print("You are hanged!")
