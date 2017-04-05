
# necessary module imports
import winsound
import sys
from time import sleep

# The Morse Code alphabet to translate to and from
morse_alph = {
    'A': '.-',       'B': '-...',     'C': '-.-.',     'D': '-..',      'E': '.',
    'F': '..-.',     'G': '--.',      'H': '....',     'I': '..',       'J': '.---',
    'K': '-.-',      'L': '.-..',     'M': '--',       'N': '-.',       'O': '---',
    'P': '.--.',     'Q': '--.-',     'R': '.-.',      'S': '...',      'T': '-',
    'U': '..-',      'V': '...-',     'W': '.--',      'X': '-.--',     'Y': '-.--',
    'Z': '--..',     '0': '-----',    '1': '.----',    '2': '..---',    '3': '...--',
    '4': '....-',    '5': '.....',    '6': '-....',    '7': '--....',   '8': '---..',
    '9': '----.',    ' ': '/',        '.': '.-.-.-',   ',': '--..--'
}


#########################################################################################
#                              Begin defining function's                                #
#########################################################################################


def menu():
    """
    Summary: Presents the user with a menu giving the option of a
             direct translation, translation from a file, or quiting. If there
             is an invalid input the function will be called again so the user
             can make another selection


    Arguments: None

    Returns: None

    """
    print('Do you want to:\n\
        1) Translate from a file\n\
        2) Translate from direct input\n\
        9) quit the program')
    
    choice = input('Option:')

    if choice is '1':
        # The string is translated and stored in morse_code.
        morse_code = translate_from_file()
        # The morse_code is printed to the screen for the user.
        print(morse_code)
        # The sound of the Morse code is played tot he user.
        play_morse(morse_code)
        # Asks the user if they want the Morse code to be written to a file.
        to_write = input('Do you want to write this Morse code to a text file?').lower()
        if to_write == 'yes' or to_write == 'y':
        # If the user responds yes the write_to_file function is called
            write_to_file(morse_code)

    elif choice is '2':
        # The string is translated and stored in morse_code.
        morse_code = translate_directly()
        # The morse_code is printed to the screen for the user.
        print(morse_code)
        # The sound of the Morse code is played tot he user.
        play_morse(morse_code)

    elif choice is '9':
        # If the user inputs '9' the program will quit.
        quit()

    else:
        # If '1','2' or '9' is not entered the else is trigged
        print('invalid choice')
        # Bring the user back to the menu to reselect.
        menu()


def translate_from_file():
    """
    Summary: Runs read_from_file() storing the user's input this is then verified
             in verify_input() if an invalid char is detected True is returned
             and the user is brought back to the start of the function. If there
             is no invalid characters the input is passed to translate()

    Arguments: None

    Returns: A Morse code message

    """
    user_input = read_from_file()
    # If there is an error verify_input(user_input) will be True
    if verify_input(user_input):
        print('You tried to translate Invalid characters')
        translate_from_file()
    else:
        pass
    return (translate(user_input))

def translate_directly():
    """
    Summary: Runs get_user_input storing the user's input this is then verified
             in verify_input() if an invalid char is detected True is returned
             and the user is brought back to the start of the function. If there
             is no invalid characters the input is passed to translate()

    Arguments: None

    Returns: A Morse code message

    """
    user_input = get_user_input()
    # If there is an error verify_input(user_input) will be True
    if verify_input(user_input):
        print('You tried to translate Invalid characters')
        translate_from_file()
    else:   
        pass
    return (translate(user_input))

def read_from_file():
    """
    Summary: Prompts the user to enter a filename. The last 4 char's are
             checked to see if they are .txt if they are not .txt is appended
             to the end. This sets the f variable and the file is read and the
             value stored in user_input. This is then capitalized and returned.


    Arguments: None

    Returns: user_input(An Upper case string)

    """
    print('NOTE: FILE MUST BE IN SAME DIRECTORY AS THIS PROGRAM')
    filename = input('Enter the filename to read from: ').lower()
    if filename[-4:] != '.txt':
        filename += '.txt'
    f = open(filename, 'r')
    user_input = f.read()
    f.close()
    return user_input.upper()


def get_user_input():
    """
    Summary: Gets an imput from the user converts and capitalizes it

    Arguments: None

    returns: An upper case user input
    """
    user_input = input('Enter text to be translated:')
    return user_input.upper()


def verify_input(user_input):
    """
    Summary: Takes the users input checks each character to see if it's in the morse_alph if it is not the test_bool
             is set to True indicating an invalid character and the
             loop broken.

    Arguments: user_input(should be taken form get_user_input)

    Returns: True or False
    """
    test_bool = False
    word = " "
    for char in user_input:
        if char in morse_alph:
            pass
        else:
            #test_bool = True
            break
    return test_bool


def translate(user_input):
    """
    Summary: Translates string into Morse code

    Arguments: user_input(should be verified)

    Returns: The inputed string in Morse code
    """
    string = ''
    for letter in user_input:
        string += morse_alph[letter]
        string += ' '
    return(string)


def play_morse(morse_code):
    for char in morse_code:
        if char is '.':
            winsound.Beep(700, 100)
        elif char is '-':
            winsound.Beep(700, 300)
        elif char is '/':
            sleep(0.2)
    sleep(0.05)



def write_to_file(morse_code):
    print('NOTE: IF YOU HAVE A FILE WITH THE SAME NAME IT WILL BE \n\
        OVERWTITTEN IF YOU DON\'T THE FILE WILL BE CREATED')
    filename = input('Enter the filename to write to: ').lower()
    if filename[-4:] != '.txt':
        filename += '.txt'
    f = open(filename, 'w')
    print(morse_code)
    user_input = f.write(morse_code)
    f.close()
    


def main():
    while True:
        menu()


if __name__ == '__main__':
    main()

