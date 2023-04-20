"""
this program encrypts and decrypts text using Ceaser Cipher
"""

class NotSring(Exception):
    pass


class NotWholeNumber(Exception):
    pass

def enter_message():
    while True:
        try:
            choice = input("Would you like to encrypt (e) or decrypt (d)")
            if not (choice.lower() == "e" or choice.lower() == "d"):
                raise NotSring
            else:
                while True:
                    try:
                        shift = int(input("Enter the shift number"))
                        if shift < 0:
                            raise NotWholeNumber
                    except NotWholeNumber:
                          print("Please enter a number greater than zero")
                    except:
                        print("Invalid Mode")      
        except NotSring:
            print("Invalid Mode")
            continue

        


def main():
    """this is the main function of the program"""
    print("""
          Welcome to the Ceaser Cipher
          This program encrypts and decrypts text with the Ceaser Cipher. 
          """)
    enter_message()
    
main()