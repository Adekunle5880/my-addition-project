import random
words = []
with open('words.txt', 'r') as dictionary:
    for word in the dictionary:
        if '-' in word:
            continue
        words.append(word.replace('\n', ''))
answer = random.choice(words).lower()
print(answer)
def scramble(i):
    i = list(i)
    random.shuffle(i)
    print(i)
    scrambled_word = ''.join(i)
    return scrambled_word
shuffled = scramble(answer)
print(shuffled)

guess = input('guess the word:')
guess = guess.lower()

while True:
    if guess == answer:
        print('bravo!!!')
        break
    else:
        print('what a pity!!!....lol u got it wrong')
        break
