# Python program to check the validity of password input by users.
password = input('Enter password: ')

has_valid_lenght = False
has_lower_case = False
has_upper_case = False
has_digits = False
has_special_characters = False

if len(password) >= 8 and len(password) <= 16:
    has_valid_lenght = True
    for i in password:
        if i.islower():
            has_lower_case = True
        if i.isupper():
            has_upper_case = True
        if i.isdigit():
            has_digits = True

        if i == '@' or i == '$' or i == '#' or i == '^' or i == '&' or i == '*':
            has_special_characters = True

if has_valid_lenght == True and has_lower_case == True and has_upper_case == True and has_digits == True and has_special_characters == True:
    print("Valid Password.")
else:
    print('Invalid Password.')
