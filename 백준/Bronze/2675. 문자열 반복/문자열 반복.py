import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    answer = ""
    num, s = input().rstrip().split()

    for u in s:
        answer += u * int(num)
    print(answer)