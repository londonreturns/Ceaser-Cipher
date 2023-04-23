"""
this program encrypts and decrypts text using Ceaser Cipher
"""


class NotRequiredString(Exception):
    """NotRequiredString: is raised when a string contains characters other than alphabets"""
    pass


class NotWholeNumber(Exception):
    """NotWholeNumber: is raised when a string is nor a whole number"""
    pass


class NotYesOrNo(Exception):
    """NotYesOrNo: is raised when a string is not (y or n)"""
    pass


def want_to_continue():
    """This is want_to_continue function.
    Prompts user to enter y or n.
    Handles exception and continues / ends the program respectively.
    """
    while True:
        try:
            # prompt user to input y or n
            again = input('Do you want to continue (y)es or (n)o: ').lower()
            if not (again == 'y' or again == 'n'):  # check if again is not (y or no)
                raise NotYesOrNo
            elif again == "y":
                return True  # returns True if again is y
            elif again == "n":
                return False  # returns False if again is n
        except NotYesOrNo:  # exception is raised if again is not y or n
            print('Please enter only yes or no')


def encrypt(text, shift_by):
    """this function encrypts text by shift forward.
    For examples if shift is 2 and text is 'a', the encrypted text will be 'c'.
    """
    all_letters = 'abcdefghijklmnopqrstuvwxyz'
    encryption_key = {} # initialising encryption key
    j = 1
    if shift_by > 26:
        shift_by %= 26
    for i in range(len(all_letters)):
        if i < len(all_letters) - shift_by:
            encryption_key[all_letters[i]] = all_letters[i + shift_by]
        else:
            encryption_key[all_letters[i]] = all_letters[j]
            j += 1
    temp = ''

    for character in text:
        if character in encryption_key:
            temp += encryption_key[character]
        else:
            teno += character
    print(temp)

def decrypt(text, shift_by):
    """lorem ipsum
    """
    print('decrypt', text, shift_by)


def enter_shift():
    """This is the enter_shift function.
    Prompts user to enter shift number for the cipher.
    Handles exception and returns shift number.
    """
    while True:
        try:
            # prompt user to input shift number
            shift_num = int(input('Enter the shift number: '))
            if shift_num < 0:  # checks if shift_num is negative
                raise NotWholeNumber
        except NotWholeNumber:  # exception is raised if shift_number is negative
            print('Please enter a number greater than zero')
            continue
        except ValueError:  # exception is raised for value error
            print('Invalid Shift number')
            continue
        else:
            break
    return shift_num  # shift_number is returned


def enter_message():
    """This is the enter_message function.
    Prompts user to input encrypt or decrypt."""
    is_continue = True
    while is_continue:
        try:
            # prompt user for choice
            choice = input(
                'Would you like to encrypt (e) or decrypt (d): ').lower()
            if not (choice == 'e' or choice == 'd'):  # checks if choice is (e or d) or not
                raise NotRequiredString
            else:
                shift = enter_shift()  # calls enter_shift function
                if choice == "e":  # calls encrypt function if choice is e
                    # prompts user for text input
                    text_input = input(
                        'What message would you like to encrypt: ').lower()
                    encrypt(text_input, shift)
                else:  # calls decrypt function if choice is d
                    # prompts user for text input
                    text_input = input(
                        'What message would you like to decrypt: ').lower()
                    decrypt(text_input, shift)
        # exception is triggered if choice is not (y or n)
        except NotRequiredString:
            print('Invalid Mode')
            continue
        is_continue = want_to_continue()  # call want_to_function
        if not is_continue:
            break


def welcome():
    """This is the Welcome function to this program."""
    print('''
Welcome to the Ceaser Cipher
This program encrypts and decrypts text with the Ceaser Cipher. 
          ''')


def main():
    """This is the main function of the program"""
    welcome()  # calls welcome function
    enter_message()  # calls enter message function


main()  # calls main function
