from string import ascii_uppercase
import sys

num_doc = {}
answer = 0

for i in ascii_uppercase:
    if i in ["A", "B", "C"]:
        num_doc[i] = 2
    elif i in ["D", "E", "F"]:
        num_doc[i] = 3
    elif i in ["G", "H", "I"]:
        num_doc[i] = 4
    elif i in ["J", "K", "L"]:
        num_doc[i] = 5
    elif i in ["M", "N", "O"]:
        num_doc[i] = 6
    elif i in ["P", "Q", "R", "S"]:
        num_doc[i] = 7
    elif i in ["T", "U", "V"]:
        num_doc[i] = 8
    elif i in ["W", "X", "Y", "Z"]:
        num_doc[i] = 9

num = sys.stdin.readline().rstrip()

for i in num:
    answer += num_doc[i] + 1

print(answer)
