"""
this program encrypts and decrypts text using Ceaser Cipher
"""

class NotSring(Exception):
    pass

class NotWholeNumber(Exception):
    pass

class NotYesOrNo(Exception):
    pass

def want_to_continue():
    while True:
        try:
            again = input("Do you want to continue (y)es or (n)o: ").lower()
            if not (again == "y" or again == "n"):
                raise NotYesOrNo
        except NotYesOrNo:
            print("Please enter only yes or no")
        finally:
            if again == "y":
                return True
            else:
                return False
                        
def encrypt(text, shift_by):
    print("encrypt", text, shift_by)
    
def decrypt(text, shift_by):
    print("decrypt", text, shift_by)

def enter_shift():
    while True:
        try:
            shift_num = int(input("Enter the shift number: "))
            if shift_num < 0:
                raise NotWholeNumber
        except NotWholeNumber:
                print("Please enter a number greater than zero")
                continue
        except:
            print("Invalid Shift number")
            continue
        finally:
            return shift_num
                        
def enter_message():
    while True:
        try:
            choice = input("Would you like to encrypt (e) or decrypt (d): ").lower()
            if not (choice == "e" or choice == "d"):
                raise NotSring
            else:
                shift = enter_shift()
                if choice == "e":
                    text_input = input("What message would you like to encrypt: ")
                    encrypt(text_input, shift)
                else:
                    text_input = input("What message would you like to decrypt: ")
                    decrypt(text_input, shift)
        except NotSring:
            print("Invalid Mode")
            continue
        if want_to_continue():
            enter_message()
        else:
            break

def welcome():
    print("""
Welcome to the Ceaser Cipher
This program encrypts and decrypts text with the Ceaser Cipher. 
          """)

def main():
    """this is the main function of the program"""
    welcome()
    enter_message()
    
main()