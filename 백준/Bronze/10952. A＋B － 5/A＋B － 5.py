import sys

while True:
    a, b = map(int, sys.stdin.readline().split())
    answer = a + b
    if answer != 0:
        print(a + b)
    else:
        break