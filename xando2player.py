from time import sleep
def drawboard(positions):
    print('\n'*50)
    print('   |   |  ')
    print(' '+positions[0]+' | '+
          positions[1] + ' | ' + positions[2])
    print('   |   |  ')
    print('-----------')
    print('   |   |  ')
    print(' '+positions[3]+' | '+
          positions[4] + ' | ' + positions[5])
    print('   |   |  ')
    print('-----------')
    print('   |   |  ')
    print(' '+positions[6]+' | '+
          positions[7] + ' | ' + positions[8])
    print('   |   |  ')

def getplayermove():
     postion = input('Where do you want to go? : ')
     return(int(postion)-1)


def getvalidmove(positions, player):
    while True:
        drawboard(positions)
        x = input('Player ' + player + ' where do you want to go? : ')
        
        try: 
            position = (int(x))-1
        except ValueError:
            print('\n\nInvalid move: Enter a number 1-9')
            sleep(2)
            return getvalidmove(positions, player)
            
        if position > 8 or position < 0:
            print('\n\nInvalid move: Enter a number 1-9')
            sleep(1)
        elif positions[position] == 'X' or positions[position] == 'O':
            print('\n\nInvalid move: Position already taken')
            sleep(1)
        else:
            print (position)
            return position

       
    

    
def checkwin(positions, player):
    letters = ['X','O']
    for i in letters:
        if (positions[0:3] == [i,i,i] or # top row
        positions[3:6] == [i,i,i] or # middle row
        positions[6:9] == [i,i,i] or # bottom row
        positions[0]+positions[3]+positions[6] == i+i+i or # left side 
        positions[1]+positions[4]+positions[7] == i+i+i or # mid side
        positions[2]+positions[5]+positions[8] == i+i+i or # right side
        positions[0]+positions[4]+positions[8] == i+i+i or # top left to bot right
        positions[2]+positions[4]+positions[6] == i+i+i):  # top right bot left
            print('Congratulations ' + player + '\'s You WIN!!!!')
            return True
    return False
def checkdraw(positions):
    letters = ['X','O']
    for i in positions:
        if i not in letters:
            return False
    print('It\'s a draw')
    return True

def gameloop(positions, first_player, second_player):
    positions[getvalidmove(positions, first_player)] = first_player
    drawboard(positions)
    if checkwin(positions, first_player):
        return True
    if checkdraw(positions):
        return True
    positions[getvalidmove(positions, second_player)] = second_player
    drawboard(positions)
    if checkwin(positions, second_player):
        return True
    if checkdraw(positions):
        return True

def getplayerletters():
    first_player = (input('Who is going first X or O? : ')).upper()
    if first_player != 'X' and first_player != 'O':
        return(getplayerletters())
    elif first_player == 'X':
        second_player = 'O'
        return[first_player,second_player]
    else:
        second_player = 'X'
        return[first_player,second_player]

        
def wantgrid():
    userinput = input ('do you want the grid of numbers?').lower()
    if userinput[0] == 'n':
        return([' ']*9)
    else:
        return(['1','2','3','4','5','6','7','8','9'])


playagain = True
while playagain:
    positions = wantgrid()
    playerletters = getplayerletters()
    while True:
        if(gameloop(positions,playerletters[0],playerletters[1])):
            break
    useranswer = (input("Do you want to play again? y/n")).lower()
    if useranswer[0] == 'n':
        playagain = False
        print('Thanks for playing!!')
    
  
    
    

        

