import random
words = ['boy', 'girl', 'apple']
answer = random.choice(words)
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
