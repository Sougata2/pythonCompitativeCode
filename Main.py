import sys
import os
inpt = os.path.abspath(os.path.dirname(__file__) + "\\input.txt")
output = os.path.abspath(os.path.dirname(__file__) + "\\output.txt")
err = os.path.abspath(os.path.dirname(__file__) + "\\error.txt")
sys.stdin = open(inpt, "r")
sys.stdout = open(output, "w")
sys.stderr = open(err, "w")


def fibonacci(n, first=0, second=1):
    if n == 0:
        return 0
    if n <= 2:
        return second

    return fibonacci(n-1, second, first+second)


num = int(input())
name = input()
print(f"Hello {name}, your fibonacci number is {fibonacci(num)}")
