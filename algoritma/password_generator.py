import random

char_lowercase = [x for x in range(97, 123)]
char_uppercase = [x for x in range(65, 90)]
char_number = [x for x in range(48, 57)]
char_symbol = [x for x in range(32, 48)] + [y for y in range(57, 65)]
list_of_char = [char_lowercase,
                char_uppercase,
                char_number,
                char_symbol
                ]
print(len(char_number))

def password_generator(length) :
    password = ""
    for i in range (length) :
        select_list = random.randint(0, 3)
        # print(select_list)
        selected_list = list_of_char[select_list]
        # print(selected_list)
        # print(selected_list[0])
        # print(selected_list[-1])
        password += chr(selected_list[random.randint(0, len(selected_list) - 1)])
        
    return password

print(password_generator(5))