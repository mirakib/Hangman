import random

print("H A N G M A N\n")

word_list = ('python', 'java', 'kotlin', 'javascript')
answer = random.choice(word_list)
hidden_ans = len(answer) * '-'
temp = list(hidden_ans)

tries = 8

while tries >= 1:
    print(hidden_ans)
    word = input("Input a letter: ")
    i = 0

    if word not in answer:
        print("No such letter in the word")
        tries -= 1

    if word in answer and word in hidden_ans:
        print("No improvements")
        tries -= 1
    else:
        for letters in answer:
            if word == letters:
                temp[i] = word
            i = i + 1
        hidden_ans = "".join(temp)

    if tries != 0:
        print()

    if hidden_ans == answer:
        print(hidden_ans)
        print("You guessed the word!")
        print("You survived!")
        break

if hidden_ans != answer:
    print("You are hanged!")
