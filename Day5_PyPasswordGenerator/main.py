import random


print("Welcome to the PyPassword Generator!\n")
number_of_letters = int(input("How many letters would you like in your password?\n "))
number_of_symbols = int(input("How many symbols would you like in your password?\n "))
number_of_numbers = int(input("How many numbers would you like in your password?\n "))


letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]  # 52 variante
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]  # 10 variante
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]  # 9 variante

lista = [letters, numbers, symbols]
password = []
password_len = number_of_letters + number_of_symbols + number_of_numbers

LETTER = 52
NUMBER = 10
SYMBOL = 9

for rand in range(0, password_len):
    char_type = random.choice(lista)
    if len(char_type) == LETTER and number_of_letters != 0:
        password.append(random.choice(char_type))
        number_of_letters -= 1
    else:
        if number_of_numbers != 0:
            password.append(random.choice(numbers))
            number_of_numbers -= 1
        elif number_of_symbols != 0:
            password.append(random.choice(symbols))
            number_of_symbols -= 1

    if len(char_type) == NUMBER and number_of_numbers != 0:
        password.append(random.choice(char_type))
        number_of_numbers -= 1
    else:
        if number_of_letters != 0:
            password.append(random.choice(letters))
            number_of_letters -= 1
        elif number_of_symbols != 0:
            password.append(random.choice(symbols))
            number_of_symbols -= 1

    if len(char_type) == SYMBOL and number_of_symbols != 0:
        password.append(random.choice(char_type))
        number_of_symbols -= 1
    else:
        if number_of_letters != 0:
            password.append(random.choice(letters))
            number_of_letters -= 1
        elif number_of_numbers != 0:
            password.append(random.choice(numbers))
            number_of_numbers -= 1

    # print(char_type)
    # print(len(char_type))


final_password = ""
random.shuffle(password)  # last random order of the password list for good luck :D
for pas in password:
    final_password = final_password + pas

print(f"Your new password is: {final_password}")
