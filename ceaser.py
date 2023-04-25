"""
This program encrypts and decrypts text using Ceaser Cipher.
First input is only in console, only after second time files can be also be encrpted / decrypted.
Welcome and goodbye message is given in Green.
Input prompts are given in Cyan.
Input are in White.
Ouput are given in Yellow.
Colorama module has been used to color text in console. 
Colorama must be installed for this program to run.
Install colorama in windows by
pip install colorama
"""

from os import startfile
from os.path import exists
from colorama import Fore
from colorama import init as colorama_init

class NotWholeNumber(Exception):
    """NotWholeNumber: is raised when a string is nor a whole number"""


class NotYesOrNo(Exception):
    """NotYesOrNo: is raised when a string is not (y or n)"""

def want_to_continue():
    """
    This is want_to_continue function.
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
    """
    This function generates the key to encrypt an decrypt.
    Returns keys in dictionary.
    """
    all_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key_value_pair = {}
    j = 0
    if shift_number > 26: # if shift is greater than 26, new shift number is shift mod 26
        shift_number %= 26
    if encrypt_or_decrypt == 'e': # for encryption
        for i, letter in enumerate(all_letters):
            if shift_number + i < 26: # if within range
                key_value_pair[letter] = all_letters[i + shift_number]
            else: # if out of range
                key_value_pair[letter] = all_letters[j]
                j += 1
    else: # for decryption
        for i, letter in enumerate(all_letters):
            if shift_number + i < 26:
                key_value_pair[all_letters[i + shift_number]] = letter
            else:
                key_value_pair[all_letters[j]] = letter
                j += 1
    return key_value_pair


def encrypt(text, shift_by):
    """
    This function encrypts text by shift number.
    For examples if shift is 2 and text is 'a', the encrypted text will be 'c'.
    """
    # call encrypt_decrypt_key_generator function
    encryption_key = encrypt_decrypt_key_generator('e', shift_by)
    temp = ''
    for character in text: # string traversal
        if character in encryption_key: # checking if character is in encryption_key
            temp += encryption_key[character]
        else: # if not then add character unchanged
            temp += character
    return temp


def decrypt(text, shift_by):
    """
    This function decrypts text by shift number.
    For examples if shift is 2 and text is 'c', the encrypted text will be 'a'.
    """
    decryption_key = encrypt_decrypt_key_generator(
        'd', shift_by)  # call encrypt_decrypt_key_generator function
    temp = ''
    for character in text: # string traversal
        if character in decryption_key: # checking if character is in decryption_key
            temp += decryption_key[character]
        else: # if not then add character unchanged
            temp += character
    return temp


def is_file(file_name):
    """This function checks if file exists or not and returns Boolean value"""
    return exists(file_name)


def enter_message():
    """
    This is the enter_message function.
    Prompts user to input encrypt or decrypt.
    Prompts user to enter message.
    Returns choice (encrypt / decrypt) and text input from user.
    """
    while True:
        choice_ed = input(
            f'{Fore.CYAN}\nWould you like to encrypt (e) or decrypt (d): {Fore.RESET}').lower()
        if not(choice_ed == 'e' or choice_ed == 'd'): # if choice is not encryption or decrption
            print(f'{Fore.RED}Invalid Mode{Fore.RESET}')
        else:
            if choice_ed == 'e': # if choice is encryption
                text_input = input(
                    f'{Fore.CYAN}\nWhat message would you like to encrypt: {Fore.RESET}').upper()
            else: # if choice is decryption
                text_input = input(
                    f'{Fore.CYAN}\nWhat message would you like to decrypt: {Fore.RESET}').upper()
            return choice_ed, text_input


def message_or_file():
    """
    This is the message_or_file function.
    Prompts user to input encrypt or decrypt.
    Prompts user to enter message.
    Prompts user to enter filename.
    Returns choice (encrypt / decrypt), text input, file name from user.
    """
    while True:
        choice_ed = input(
            f'{Fore.CYAN}\nWould you like to encrypt (e) or decrypt (d): {Fore.RESET}').lower()
        if not (choice_ed =='e' or choice_ed =='d'):
            print(f'{Fore.RED}Invalid Mode{Fore.RESET}')
            continue
        else:
            while True:
                choice_cf = input(
                    f'{Fore.CYAN}\nWould you like enter in console (c) or file (f): {Fore.RESET}'
                    ).lower()
                if not (choice_cf =='c' or choice_cf == 'f'): # if encrption and file
                    print(f'{Fore.RED}Invalid Mode{Fore.RESET}')
                    continue
                else:
                    if choice_cf == 'c' and choice_ed == 'e': # if encrption and console
                        text_input = input(
                            f'{Fore.CYAN}\nWhat message would you like to encrypt: {Fore.RESET}'
                            ).upper()
                        file_name = None
                    elif choice_cf == 'c' and choice_ed == 'd':  # if decryption and console
                        text_input = input(
                            f'{Fore.CYAN}\nWhat message would you like to encrypt: {Fore.RESET}'
                            ).upper()
                        file_name = None
                    else: # if decryption and console
                        file_name = input(
                            f'{Fore.CYAN}\nWhat message would you like to decrypt: {Fore.RESET}'
                            ).upper()
                        text_input = None
                return choice_ed, text_input, file_name


def process_file(file_name, mode, shift_number):
    """
    This is process_file function.
    It takes in file_name, mode, shift_number and makes list of encrypted string.
    Returns list of encrypted / decrypted characters.
    """
    # opening file to read with utf-8 encoding
    with open(file_name, 'r', encoding = 'utf-8') as file1:
        temp_list = []
        if mode == 'e': # if choice is encryption
            for line in file1: # file traversal
                for character in line: # string traversal
                    # call encrypt function
                    temp_character = encrypt(character.upper(), shift_number)
                    temp_list.append(temp_character)
        else: # if choice is decryption
            for line in file1: # file traversal
                for character in line: # string traversal
                     # call decrypt function
                    temp_character = decrypt(character.upper(), shift_number)
                    temp_list.append(temp_character)
        return temp_list


def write_messages(all_characters):
    """
    This is write_message function.
    It takes a list and writes in an external file and opens the file in notepad.
    """
    while True:
        write_file = input(f'{Fore.CYAN}\nOutput written to: {Fore.RESET}')
        # opening file to read with utf-8 encoding
        with open(write_file, 'w', encoding = 'utf-8') as file2:
            for character in all_characters: # list traversal
                file2.write(character)
            print(Fore.YELLOW + '\nFile saved successfully' + Fore.RESET)
            break


def enter_shift():
    """
    This is the enter_shift function.
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


def welcome():
    """This is the Welcome function to this program."""
    print(f'''{Fore.GREEN}
Welcome to the Ceaser Cipher
This program encrypts and decrypts text with the Ceaser Cipher.''')


def main():
    """This is the main function of the program"""
    welcome()  # call welcome function
    still_continue = True
    run_file = False
    while still_continue:
        colorama_init(autoreset=True)
        if run_file:
            choice, message, file1 = message_or_file() # call message_or_file function
        else:
            choice, message = enter_message()  # call enter message function
            file1 = None
        shift_number = enter_shift() # call enter_shift function
        if file1 is None:
            if choice == 'e':
                print(Fore.YELLOW + encrypt(message, shift_number) + Fore.RESET)
            else:
                print(Fore.YELLOW + decrypt(message, shift_number) + Fore.RESET)
        else:
            while not is_file(file1):
                print(f'{Fore.RED}File not found{Fore.RESET}')
                file1 = input(
                    f'{Fore.CYAN}\nWhat is the name of the file: {Fore.RESET}').upper()
            # call process_file function
            changed_text_list = process_file(file1, choice, shift_number)
            write_messages(changed_text_list) # call write_messages function
            startfile(file1) # to open file in notepad after writing
        if still_continue:
            run_file = True
            still_continue = want_to_continue() # call want_to_continue function
            continue
    print(f'''{Fore.GREEN}
Thank you for using my program{Fore.RESET}''')


main()  # call main function
