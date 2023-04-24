"""
This program encrypts and decrypts text using Ceaser Cipher.

Colorama module has been used to color text in console.
Welcome message is given in Green.
Input prompts are given in Cyan.
Input are in White.
Ouput are given in Yellow.
"""

from colorama import Fore
from colorama import init as colorama_init

class NotRequiredString(Exception):
    """NotRequiredString: is raised when a string contains characters other than alphabets"""


class NotWholeNumber(Exception):
    """NotWholeNumber: is raised when a string is nor a whole number"""


class NotYesOrNo(Exception):
    """NotYesOrNo: is raised when a string is not (y or n)"""
      
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


def encrypt_decrypt_key_generator(encrypt_or_decrypt, shift_number):
    all_letters = 'abcdefghijklmnopqrstuvwxyz'
    key_dictionary = {}
    j = 0
    if shift_number > 26:
        shift_number %= 26
    if encrypt_or_decrypt == 'e':
        for i in range(len(all_letters)):
            if shift_number + i < 26:
                key_dictionary[all_letters[i]] = all_letters[i + shift_number]
            else:
                key_dictionary[all_letters[i]] = all_letters[j]
                j += 1
    else:
        for i in range(len(all_letters)):
            if shift_number + i < 26:
                key_dictionary[all_letters[i + shift_number]] = all_letters[i]
            else:
                key_dictionary[all_letters[j]] = all_letters[i]
                j += 1
    return key_dictionary


def encrypt(text, shift_by):
    """This function encrypts text by shift number.
    For examples if shift is 2 and text is 'a', the encrypted text will be 'c'.
    """
    encryption_key = encrypt_decrypt_key_generator(
        'e', shift_by)  # calling encrypt_decrypt_key_generator function
    print(encryption_key)
    temp = ''

    for character in text:
        if character in encryption_key:
            temp += encryption_key[character]
        else:
            temp += character
    print(temp)


def decrypt(text, shift_by):
    """This function decrypts text by shift number.
    For examples if shift is 2 and text is 'c', the encrypted text will be 'a'.
    """
    decryption_key = encrypt_decrypt_key_generator(
        'd', shift_by)  # calling encrypt_decrypt_key_generator function
    print(decryption_key)
    temp = ''

    for character in text:
        if character in decryption_key:
            temp += decryption_key[character]
        else:
            temp += character
    print(temp)


def enter_shift():
    """This is the enter_shift function.
    Prompts user to enter shift number for the cipher.
    Handles exception and returns shift number.
    """
    while True:
        try:
            # prompt user to input shift number
            shift_num = int(input(
                f'{Fore.CYAN}Enter the shift number: {Fore.RESET}'))
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
    Prompts user to input encrypt or decrypt.
    Prompts user to enter message."""
    is_continue = True
    while is_continue:
        try:
            # prompt user for choice
            choice = input(
                f'{Fore.CYAN}Would you like to encrypt (e) or decrypt (d): {Fore.RESET}').lower()
            if not (choice == 'e' or choice == 'd'):  # checks if choice is (e or d) or not
                raise NotRequiredString
            else:
                shift = enter_shift()  # calls enter_shift function
                if choice == "e":  # calls encrypt function if choice is e
                    # prompts user for text input
                    text_input = input(
                        f'{Fore.CYAN}What message would you like to encrypt: {Fore.RESET}').lower()
                    encrypt(text_input, shift)
                else:  # calls decrypt function if choice is d
                    # prompts user for text input
                    text_input = input(
                        f'{Fore.CYAN}What message would you like to decrypt: {Fore.RESET}').lower()
                    decrypt(text_input, shift)
        # exception is triggered if choice is not (y or n)
        except NotRequiredString:
            print(f'{Fore.RED}Invalid Mode{Fore.RESET}')
            continue
        is_continue = want_to_continue()  # call want_to_function
        if not is_continue:
            break


def welcome():
    """This is the Welcome function to this program."""
    print(f'''{Fore.GREEN}
Welcome to the Ceaser Cipher
This program encrypts and decrypts text with the Ceaser Cipher. 
          ''')


def main():
    """This is the main function of the program"""
    colorama_init(autoreset=True)
    welcome()  # calls welcome function
    enter_message()  # calls enter message function


main()  # calls main function
