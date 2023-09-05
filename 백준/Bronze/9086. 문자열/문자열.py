import sys

T = int(sys.stdin.readline())

for i in range(T):
    text = sys.stdin.readline().rstrip()
    print(text[0] + text[-1])