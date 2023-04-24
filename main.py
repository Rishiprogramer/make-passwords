import random
from random_module import *
from colr import clor
try:
    length = int(input(clor.OKBLUE+f"Enter the lenght of the password: "))
    leave = input(clor.OKBLUE + f"If any expections that you do not want to include:\n1)Alpable\n2)Numbers\n3)Symbols\n"
                                f"4)Only Alpabets\n5)Only Numbers\n6)Only Symbols\n7)Only Alpabets & Number\n8)Only Alpabets & Symbols\n"
                                f"9)Only Number & Symbol\n10)No Exceptions\n Enter only numbers: ")
except ValueError:
    print(clor.FAIL +f"PLEASE ENTER CORRECT VALUE")
    exit()
if leave == "1":
    wh = DIGITS +  SYMBOLS
    password = ''.join(random.choice(wh) for i in range(length))
    print(clor.OKGREEN + password)
elif leave == "2":
    wh =  SYMBOLS + LOCASE_CHARACTERS + UPCASE_CHARACTERS
    password = ''.join(random.choice(wh) for i in range(length))
    print(clor.OKGREEN + password)
elif leave == "3":
    wh = LOCASE_CHARACTERS + UPCASE_CHARACTERS + DIGITS
    password = ''.join(random.choice(wh) for i in range(length))
    print(clor.OKGREEN + password)
elif leave == "4":
    wh = LOCASE_CHARACTERS + UPCASE_CHARACTERS
    password = ''.join(random.choice(wh) for i in range(length))
    print(clor.OKGREEN + password)
elif leave == "5":
    wh = DIGITS
    password = ''.join(random.choice(wh) for i in range(length))
    print(clor.OKGREEN + password)
elif leave == "6":
    wh = SYMBOLS
    password = ''.join(random.choice(wh) for i in range(length))
    print(clor.OKGREEN + password)
elif leave == "7":
    wh = LOCASE_CHARACTERS + UPCASE_CHARACTERS + DIGITS
    password = ''.join(random.choice(wh) for i in range(length))
    print(clor.OKGREEN + password)
elif leave == "8":
    wh = LOCASE_CHARACTERS + UPCASE_CHARACTERS + SYMBOLS
    password = ''.join(random.choice(wh) for i in range(length))
    print(clor.OKGREEN + password)
elif leave == "9":
    wh = DIGITS + SYMBOLS
    password = ''.join(random.choice(wh) for i in range(length))
    print(clor.OKGREEN + password)
elif leave == "10":
    wh = LOCASE_CHARACTERS + UPCASE_CHARACTERS + DIGITS + SYMBOLS
    password = ''.join(random.choice(wh) for i in range(length))
    print(clor.OKGREEN + password)
else:
    print(clor.FAIL+f"INVALID VALUE ENTERED")


