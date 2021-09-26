from os import error
import sys
import operator

def calc(str):
    try:
        choice = str[1]
        if choice == 'add':return operator.add(int(str[2]), int(str[3]))
        elif choice == 'mul':return operator.mul(int(str[2]), int(str[3]))
        elif choice == 'divide':return operator.truediv(int(str[2]), int(str[3]))
        elif choice == 'sub':return operator.sub(int(str[2]), int(str[3]))
    except:
        return False

print(calc(sys.argv[:]))