import random
import time
animals = ['alligator', 'baboon', 'badger', 'buffalo',
           'bull', 'camel', 'chimpanzee', 'crocodile',
           'giraffe', 'hamster', 'jaguar', 'kangaroo',
           'koala', 'lion', 'monkey', 'ocelot', 'panda',
           'panther', 'porcupine', 'rabbit', 'raccoon',
           'rhinoceros', 'skunk', 'snake', 'squirrel',
           'tiger', 'walrus', 'weasel', 'zebra']


def shuffle(word):
    word = list(word)
    for item in range(0,len(word)):
        tempchar = word[item]
        word.pop(item)
        word.insert(random.randint(0,len(word)), tempchar)
    return ''.join(word)

playagain = 'yes'
while playagain == 'yes':
    animal =(random.choice(animals))
    shuff = (shuffle((shuffle((shuffle(animal))))))
    print ('welcome to Word Jumble!')
    time.sleep(2)
    print ('You must guess the animal from the jumbled word')
    time.sleep(3)
    print ('Good Luck')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print ('The jumbled word is: '+shuff)
    start = time.time()
    count = 0
    guess = 'null'
    while guess != animal:
        guess = input('guess the animal')
        count += 1
    end = time.time()
    timetaken = (round(end-start,2))
    print('Well done it took you '+str(count)+' guesses and '+str(timetaken)+' seconds')
    playagain = input('Do you want to play again (yes/no)?')
    while playagain not in ['yes', 'no']:
        playagain = input('type yes or no:')
        print(playagain)
if playagain == 'no':
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('bye') 
    exit()
    


           
           
