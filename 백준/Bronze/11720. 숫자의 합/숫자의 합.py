import sys

n = int(sys.stdin.readline())
str = sys.stdin.readline().rstrip()
answer = 0

for i in str:
    answer += int(i)

print(answer)