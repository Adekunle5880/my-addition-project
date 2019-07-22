import json
import random

data = json.load(open("dictionary.json"))

words = []
meaning = []
score = 0
retry = 5

for key, value in data.items():
    words.append(key)
    meaning.append(value)

while retry != 0:

    answer = random.choice(words)
    print(answer)
    a = [i for i in answer]

    scrambled = random.shuffle(a)

    for b in a:
        print(b.upper(), end=' ')

    print("\nHINT: Meaning => {}".format(data[answer]))
    guess = input("\nEnter a word >> ").lower()

    if len(guess) == 0 or guess.isdigit():
        print("\nSorry! Invalid input.")

    elif guess == answer:
        print("\nGbebo di eh")
        score += 5
        print("Score = {}".format(score))

    elif guess != answer:
        while retry > 0:
            print("\nWrong ooo, ")
            guess = input("Try again >> ")
            score -= 2
            retry -= 1

            if len(guess) == 0 or guess.isdigit():
                print("\nSorry! Invalid input.")

            elif guess == answer:
                print("\nGbebo di eh")
                score += 5
                print("Score = {}".format(score))
                break

            else:
                print("Wrong")
                print("Score = {}, {} Retries left".format(score, retry))
