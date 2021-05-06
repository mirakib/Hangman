import random

print("H A N G M A N\n")

word_list = ('python', 'java', 'kotlin', 'javascript')
answer = random.choice(word_list)
hidden_ans = len(answer) * '-'
temp = list(hidden_ans)


for x in range(8):
    i = 0
    print(hidden_ans)
    guess = (input("Input a letter:  "))
    if guess not in answer:
        print("No such letter in the word")
    else:
        for letters in answer:
            if guess == letters:
                temp[i] = guess
            i = i + 1
        hidden_ans = "".join(temp)
    print()

print("Thanks for playing!")
print("We'll see how well you did in the next stage")
