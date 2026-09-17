def check_length(password):
    if len(password) > 8:
        return True
    else:
        return False

def has_number(password):
    for character in password:
        if character in "0123456789":
            return True
    return False

def has_special(password):
    for character in password:
        if character in "!@#$%^&*":
            return True
    return False

password = input("Enter your password: ")

length_check = check_length(password)
number_check = has_number(password)
special_check = has_special(password)

score = 0
if length_check == True:
    score = score + 1
if number_check == True:
    score = score + 1
if special_check == True:
    score = score + 1

if score == 3:
    print("Your password strength is: Strong! 💪")
elif score == 2:
    print("Your password strength is: Medium!")
else:
    print("Your password strength is: Weak! 😱")
