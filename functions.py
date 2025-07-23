import random

def password_seed(allchars, user_password: str):
    random.seed(user_password)
    new_list = random.sample(allchars, len(allchars))
    return new_list

def encrypt_msg(msg, index_list, new_list):
    encrypted_msg = []
    for char in msg:
        if char == " ":
            encrypted_msg.append(" ")
        else:
            letters_index = index_list.index(char)
            random_list = new_list[int(letters_index)]
            encrypted_msg.append(random_list)
    return "".join(encrypted_msg)

def decrypt_msg(msg, index_list, new_list):
    decrypted_msg = []
    for char in msg:
        if char == " ":
            decrypted_msg.append(" ")
        else:
            letters_index = new_list.index(str(char))
            random_list = index_list[int(letters_index)]
            decrypted_msg.append(random_list)
    return "".join(decrypted_msg)

