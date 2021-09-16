
import sys
from operator import  add, sub, truediv, mul
from functools import reduce
my_list = sys.argv[1:]


def calculate(express):

    try:
        return  eval("".join(express))
    except (TypeError, ValueError, SyntaxError):
        return None


print(calculate(my_list))