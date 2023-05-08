"""
This program encrypts and decrypts text using Ceaser Cipher.
First input and output is only in console.
Text can be encrypted both from console and from file.
"""

from os import startfile
from os.path import exists


class NotWholeNumber(Exception):
    """NotWholeNumber: is raised when a string is nor a whole number"""


class NotYesOrNo(Exception):
    """NotYesOrNo: is raised when a string is not (y or n)"""


def encrypt(text, shift_by):
    """
    This function encrypts text by shift number.
    For examples if shift is 2 and text is 'a', the encrypted text will be 'c'.
    """
    all_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key_value_pair = {}
    j = 0
    if shift_by > 26:  # if shift is greater than 26, new shift number is shift mod 26
        shift_by %= 26
    for i, letter in enumerate(all_letters):
        if shift_by + i < 26:  # if within range
            key_value_pair[letter] = all_letters[i + shift_by]
        else:  # if out of range
            key_value_pair[letter] = all_letters[j]
            j += 1
    temp = ''
    for character in text:  # string traversal
        if character in key_value_pair:  # checking if character is in key_value_pair
            temp += key_value_pair[character]
        else:  # if not then add character unchanged
            temp += character
    return temp


def decrypt(text, shift_by):
    """
    This function decrypts text by shift number.
    For examples if shift is 2 and text is 'c', the encrypted text will be 'a'.
    """
    all_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key_value_pair = {}
    j = 0
    if shift_by > 26:  # if shift is greater than 26, new shift number is shift mod 26
        shift_by %= 26
    for i, letter in enumerate(all_letters):
        if shift_by + i < 26:
            key_value_pair[all_letters[i + shift_by]] = letter
        else:
            key_value_pair[all_letters[j]] = letter
            j += 1
    temp = ''
    for character in text:  # string traversal
        if character in key_value_pair:  # checking if character is in key_value_pair
            temp += key_value_pair[character]
        else:  # if not then add character unchanged
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
            '\nWould you like to encrypt (e) or decrypt (d): ').lower()
        if not(choice_ed == 'e' or choice_ed == 'd'):  # if choice is not encryption or decryption
            print('Invalid Mode')
        else:
            if choice_ed == 'e':  # if choice is encryption
                text_input = input(
                    '\nWhat message would you like to encrypt: ').upper()
            else:  # if choice is decryption
                text_input = input(
                    '\nWhat message would you like to decrypt: ').upper()
            return choice_ed, text_input


def message_or_file():
    """
    This is the message_or_file function.
    Prompts user to input encrypt or decrypt.
    Prompts user to enter message.
    Prompts user to enter filename.
    Returns choice (encrypt / decrypt), text input, file name from user.
    """
    choice_ed, text_input, file_name = '', '', ''
    while True:
        choice_cf = input(
            '\nWould you like enter in console (c) or file (f): '
            ).lower()
        if choice_cf not in ('c', 'f'):  # if not encryption and file
            print('Invalid Mode')
            continue
        if choice_cf == 'c':
            choice_ed, text_input = enter_message()  # call enter message function
            file_name = None
            break
        while True:
            #  prompts user to enter encrypt or decrypt
            choice_ed = input(
                '\nWould you like to encrypt (e) or decrypt (d): ').lower()
            if choice_ed not in ('e', 'd'):  # if choice is not e or d
                print('Invalid Mode')
                continue
            text_input = None
            if choice_ed == 'e':
                #  prompts user to enter filename to encrypt
                file_name = input(
                    '\nWhat is the file name that you would encrypt: ').upper()
            else:
                #  prompts user to enter filename to decrypt
                file_name = input(
                    '\nWhat is the file name that you would decrypt: ').upper()
            break
        break
    return choice_ed, text_input, file_name


def process_file(file_name, mode, shift_number):
    """
    This is process_file function.
    It takes in file_name, mode, shift_number and makes list of encrypted string.
    Returns list of encrypted / decrypted characters.
    """
    # opening file to read with utf-8 encoding
    with open(file_name, 'r', encoding='utf-8') as file1:
        temp_list = []
        if mode == 'e':  # if choice is encryption
            for line in file1:  # file traversal
                for character in line:  # string traversal
                    #  call encrypt function
                    temp_character = encrypt(character.upper(), shift_number)
                    temp_list.append(temp_character)
        else:  # if choice is decryption
            for line in file1:  # file traversal
                for character in line:  # string traversal
                    #  call decrypt function
                    temp_character = decrypt(character.upper(), shift_number)
                    temp_list.append(temp_character)
        return temp_list


def write_messages(all_characters):
    """
    This is write_message function.
    It takes a list and writes in an external file and opens the file in notepad.
    """
    while True:
        write_file = input('\nOutput written to: ')
        # opening file to read with utf-8 encoding
        with open(write_file, 'w', encoding='utf-8') as file2:
            for character in all_characters:  # list traversal
                file2.write(character)
            print('\nFile saved successfully')
        startfile(write_file)  # to open file in notepad after writing
        break


def enter_shift():
    """
    This is the enter_shift function.
    Prompts user to enter shift number for the cipher.
    Handles exception and returns shift number.
    """
    shift_num = 0
    while True:
        try:
            # prompt user to input shift number
            shift_num = int(input('\nEnter the shift number: '))
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


def welcome():
    """This is the Welcome function to this program."""
    print('''
Welcome to the Ceaser Cipher
This program encrypts and decrypts text with the Ceaser Cipher.''')


def main():
    """This is the main function of the program"""
    welcome()  # call welcome function
    still_continue = True
    while still_continue:
        choice, message, file1 = message_or_file()  # call message_or_file function
        shift_number = enter_shift()  # call enter_shift function
        if file1 is None:
            if choice == 'e':
                print(encrypt(message, shift_number))
            else:
                print(decrypt(message, shift_number))
        else:
            while not is_file(file1):
                print('File not found')
                file1 = input(
                    '\nWhat is the name of the file: ').upper()
            # call process_file function
            changed_text_list = process_file(file1, choice, shift_number)
            write_messages(changed_text_list)  # call write_messages function
        if still_continue:
            while True:
                try:
                    # prompt user to input y or n
                    again = input('Do you want to continue (y)es or (n)o: ').lower()
                    if not (again == 'y' or again == 'n'):  # check if again is not (y or no)
                        raise NotYesOrNo
                    if again == "y":
                        still_continue = True  # returns True if again is y
                        break
                    if again == "n":
                        still_continue = False  # returns False if again is n
                        break
                except NotYesOrNo:  # exception is raised if again is not y or n
                    print('Please enter only yes or no')
                    continue
    print('''
Thank you for using my program
''')


main()  # call main function
