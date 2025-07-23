from functions import password_seed, encrypt_msg, decrypt_msg
from shift_list import allchars, acii_art

print (acii_art)
is_unsecure = True

while is_unsecure:
    user_input = input("Welcome. Do you want to (d)ecrypt or (e)encrypt your message: ").lower().strip()
    user_input_isalpha = user_input.isalpha()
    if user_input_isalpha == True and user_input == "e":
        user_msg = input("Enter your Message: ").strip()
        user_pwd = input("Password (12-20 characters required): ").strip()
        if len(user_pwd) <= 20 and len(user_pwd) >= 12:
            new_list = password_seed(allchars, user_pwd)
            message = encrypt_msg(msg = user_msg , index_list = allchars, new_list = new_list)
            print(f"Your encrypted message is:\n{message}\nTo decrypt your message, please remember both the password you chose and your encrypted message.")
            is_unsecure = False
        else:
            print("Please enter a valid password.")

    elif user_input_isalpha == True and user_input == "d":
        user_msg = input("Enter Message: ").strip()
        user_pwd =  input("Enter password: ").strip()
        if len(user_pwd) <= 20 and len(user_pwd) >= 12:
            new_list = password_seed(allchars, user_pwd)
            message = decrypt_msg(msg=user_msg, index_list=allchars, new_list=new_list)
            print(f"Your decrypted message is:\n{message}")
            is_unsecure = False
        else:
            print("Please enter a valid password.")
    else:
        print("Please choose either to (e)ncrypt or (d)ecrypt a message")
