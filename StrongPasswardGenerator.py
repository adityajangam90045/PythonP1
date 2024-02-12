import random
import string

lower_len = int(input("Enter the lowerNO: "))
upper_len = int(input("Enter the upperNO: "))
digit_len = int(input("Enter the digitNO: "))
symbol_len = int(input("Enter the symbolNO: "))

pwd_len = lower_len + upper_len + digit_len + symbol_len

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit =string.digits
symbol =string.punctuation

pwd = lower + upper + digit+ symbol

str = random.choices(pwd,k = pwd_len)
random.shuffle(str)
password = "".join(str)
print("Passward is : ",password)


