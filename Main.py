from functions import get_random_number, get_random_list, encrypt_msg, decrypt_msg
from shift_list import letters, numbers, symbols, allchars, acii_art

enum = get_random_number()
encrypt_list = get_random_list(enum = enum, letters = letters, sym = symbols, num=numbers)
print (acii_art)
is_unsecure = True

while is_unsecure:
    user_input = input("Welcome. Do you want to (d)ecrypt or (e)encrypt your message: ").lower().strip()
    user_input_isalpha = user_input.isalpha()
    if user_input_isalpha == True and user_input == "e":
        user_msg = input("Enter your Message: ")
        shift_number =  input("Enter shift number from 1 to 20: ")
        shift_number_isdigit = shift_number.isdigit()
        if int(shift_number) <= 20 and shift_number_isdigit == True:
            enum = get_random_number()
            new_list = get_random_list(enum = enum , letters = letters, sym = symbols, num = numbers)
            message = encrypt_msg(msg = user_msg , index_list = allchars, new_list = new_list, shift_num = shift_number)
            print(f"Your encrypted message is:\n{message}\nYour secret key is: {enum}. To decrypt your message, please remember both the shift number you chose and this secret key.")
            is_unsecure = False
        else:
            print("Please enter a valid shift number between 1 to 20.")

    elif user_input_isalpha == True and user_input == "d":
        user_msg = input("Enter Message: ")
        shift_number =  input("Enter shift number from 1 to 20: ")
        shift_number_isdigit = shift_number.isdigit()
        if int(shift_number) <= 20 and shift_number_isdigit == True:
            enum = input("Enter secret number: ")
            new_list = get_random_list(enum=enum, letters=letters, sym=symbols, num=numbers)
            message = decrypt_msg(msg=user_msg, index_list=allchars, new_list=new_list, shift_num=shift_number)
            print(f"Your decrypted message is:\n{message}")
            is_unsecure = False
        else:
            print("Please enter a valid shift number between 1 to 20.")
    else:
        print("Please choose either to (e)ncrypt or (d)ecrypt a message")
