import random

print("H A N G M A N\n")

word_list = ('python', 'java', 'kotlin', 'javascript')
answer = random.choice(word_list)
hidden_ans = len(answer) * '-'
temp = list(hidden_ans)
reply_check = []  # store every word
tries = 8

while tries >= 1:
    print(hidden_ans)
    word = input("Input a letter: ")
    i = 0

    if len(word) != 1:  # Remember that zero is also not one!
        print("You should input a single letter")

    elif not word.isalpha():
        print("It is not an ASCII lowercase letter")

    elif word.isalpha():
        if word.islower():
            if word in hidden_ans or word in reply_check:
                print("You already typed this letter")

            elif word in answer:
                for letters in answer:
                    if word == letters:
                        temp[i] = word
                    i = i + 1
                hidden_ans = "".join(temp)

            else:
                print("No such letter in the word")
                tries -= 1
                reply_check.append(word)
        else:
            print("It is not an ASCII lowercase letter")

    # this block need to debug
    if hidden_ans != answer and not tries < 1:
        print()

    if hidden_ans == answer:
        print("You guessed the word {}!".format(hidden_ans))
        print("You survived!")
        break

if hidden_ans != answer:
    print("You are hanged!")
