from random import randint

names = {0:"rock", 1:"paper", 2:"scissors"}
numbers = {"rock":0, "paper":1, "scissors":2}
Decide_win = {0:"Draw",1:"Win",2:"Lose"}

def rps(name):
    if name == 'exit':
        quit()
    elif name not in numbers:
        print('That was not a valid input')
        return main()
    User_num = numbers[name]
    Computer_num = randint(0,2)
    print('Computer chose',names[Computer_num])
    print(Decide_win[(User_num - Computer_num) % 3])

def main():
    rps(input('Enter (exit), Rock, Paper or Sissors): ').lower())

while True:
    main()
    


