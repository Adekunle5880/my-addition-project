import random
number = random.randint(0,100)
print (number)

while True:
    guess = input('guess the number')
    guess = int(guess)

    if guess == number:
        print('bravo!!!')
        break
    else:
        print('what a pity...lol u got it wrong')
        

