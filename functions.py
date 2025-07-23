import random

def get_random_number():
    random_number = random.randint(1000, 9999)
    random_division = random.randint(100, 999)
    random_list = list(str(random_number//random_division))
    if len(random_list) > 1:
        encrypt_num = random_list[1]
        return int(encrypt_num)
    else:
        encrypt_num = random_list[0]
        return int(encrypt_num)

def get_random_list(enum, letters, sym, num):
    if enum == 0 or enum == 3 or enum == 6:
        return sym
    elif enum == 1 or enum == 4 or enum == 7:
        return num
    elif enum == 2 or enum == 5 or enum == 8 or enum == 9:
        return letters
    else:
        return letters

def encrypt_msg(msg, index_list, new_list, shift_num):
    encrypted_msg = []
    for char in msg:
        if char == " ":
            encrypted_msg.append(" ")
        else:
            letters_index = index_list.index(char)
            shift_list_index = new_list[int(letters_index) + int(shift_num)]
            encrypted_msg.append(shift_list_index)
    return "".join(encrypted_msg)

def decrypt_msg(msg, index_list, new_list, shift_num):
    decrypted_msg = []
    for char in msg:
        if char == " ":
            decrypted_msg.append(" ")
        else:
            letters_index = new_list.index(str(char))
            shift_list_index = index_list[int(letters_index) - int(shift_num)]
            decrypted_msg.append(shift_list_index)
    return "".join(decrypted_msg)

