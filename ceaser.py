"""
This program encrypts and decrypts text using Ceaser Cipher.

Colorama module has been used to color text in console.
Welcome and goodbye message is given in Green.
Input prompts are given in Cyan.
Input are in White.
Ouput are given in Yellow.
"""

from os import startfile
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
            again = input(
                f'\n{Fore.CYAN}Do you want to continue (y)es or (n)o: {Fore.RESET}').lower()
            if not (again == 'y' or again == 'n'):  # check if again is not (y or no)
                raise NotYesOrNo
            elif again == "y":
                return True  # returns True if again is y
            elif again == "n":
                return False  # returns False if again is n
        except NotYesOrNo:  # exception is raised if again is not y or n
            print(f'{Fore.RED}Please enter only yes or no{Fore.RESET}')


def encrypt_decrypt_key_generator(encrypt_or_decrypt, shift_number):
    """This function generates the key to encrypt an decrypt"""
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
    # calling encrypt_decrypt_key_generator function
    encryption_key = encrypt_decrypt_key_generator('e', shift_by)
    temp = ''

    for character in text:
        if character in encryption_key:
            temp += encryption_key[character]
        else:
            temp += character
    return temp


def decrypt(text, shift_by):
    """This function decrypts text by shift number.
    For examples if shift is 2 and text is 'c', the encrypted text will be 'a'.
    """
    decryption_key = encrypt_decrypt_key_generator(
        'd', shift_by)  # calling encrypt_decrypt_key_generator function
    temp = ''
    for character in text:
        if character in decryption_key:
            temp += decryption_key[character]
        else:
            temp += character
    return temp


def enter_shift():
    """This is the enter_shift function.
    Prompts user to enter shift number for the cipher.
    Handles exception and returns shift number.
    """
    while True:
        try:
            # prompt user to input shift number
            shift_num = int(input(
                f'{Fore.CYAN}\nEnter the shift number: {Fore.RESET}'))
            if shift_num < 0:  # checks if shift_num is negative
                raise NotWholeNumber
        except NotWholeNumber:  # exception is raised if shift_number is negative
            print(f'{Fore.RED}Please enter a number greater than zero{Fore.RESET}')
            continue
        except ValueError:  # exception is raised for value error
            print(f'{Fore.RED}Invalid Shift number{Fore.RESET}')
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
            choice_ed = input(
                f'{Fore.CYAN}\nWould you like to encrypt (e) or decrypt (d): {Fore.RESET}').lower()
            choice_cf = input(
                f'{Fore.CYAN}\nWould you like enter in console (c) or file (f): {Fore.RESET}').lower()
            if not ((choice_ed == 'e' or choice_ed == 'd') and
                    (choice_cf == 'c' or choice_cf == 'f')):
                raise NotRequiredString
            else:
                shift = enter_shift()  # calls enter_shift function
                if choice_ed == 'e' and choice_cf == 'c':
                    # prompts user for text input
                    text_input = input(
                        f'{Fore.CYAN}\nWhat message would you like to encrypt: {Fore.RESET}').lower()
                    print(Fore.YELLOW + encrypt(text_input, shift) + Fore.RESET)
                elif choice_ed =='d' and choice_cf == 'c':  # calls decrypt function if choice is d
                    # prompts user for text input
                    text_input = input(
                        f'{Fore.CYAN}\nWhat message would you like to decrypt: {Fore.RESET}').lower()
                    print(Fore.YELLOW + decrypt(text_input, shift) + Fore.RESET)
                else:
                    read_file = input(f'{Fore.CYAN}\nEnter the file name: {Fore.RESET}')
                    with open(read_file, 'r', encoding = 'utf-8') as file1:
                        all_text = ''
                        if choice_ed == 'e':
                            for line in file1:
                                current_line = encrypt(line.lower(), shift)
                                all_text += current_line
                        else:
                            for line in file1:
                                current_line = decrypt(line.lower(), shift)
                                all_text += current_line
                    write_file = input(f'{Fore.CYAN}\nOutput written to: {Fore.RESET}')
                    with open(write_file, 'w', encoding = 'utf-8') as file2:
                        file2.writelines(all_text)
                    startfile(write_file)
        # exception is triggered if choice is not (y or n)
        except NotRequiredString:
            print(f'{Fore.RED}Invalid Mode{Fore.RESET}')
            continue
        except IOError:
            print(f'{Fore.RED}File not found{Fore.RESET}')
        is_continue = want_to_continue()  # call want_to_function
        if not is_continue:
            print(f'''{Fore.GREEN}
Thank you for using this program, goodbye!''')
            break


def welcome():
    """This is the Welcome function to this program."""
    print(f'''{Fore.GREEN}
Welcome to the Ceaser Cipher
This program encrypts and decrypts text with the Ceaser Cipher.''')


def main():
    """This is the main function of the program"""
    colorama_init(autoreset=True)
    welcome()  # calls welcome function
    enter_message()  # calls enter message function


main()  # calls main function
