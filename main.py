#Program 1
import sys
from operator import  add, sub, truediv, mul
from functools import reduce
my_list = sys.argv[1:]

#
# def calculate(express):
#
#     try:
#         return  eval("".join(express))
#     except (TypeError, ValueError, SyntaxError):
#         return None
#
#
# print(calculate(my_list))


# Program 2

storage = {"add": add, "mul": mul, "div":truediv, "sub": sub}


def calculate(oper, operands):

    try:
        return reduce(lambda x, y: storage[oper](int(x), int(y)), operands)
    except (KeyError, ZeroDivisionError):
        return None

oper = my_list[0]
operands = my_list[1:]

print(calculate(oper, operands))