import sys

n = int(sys.stdin.readline())
list = sys.stdin.readline().rstrip().split()
num = sys.stdin.readline().rstrip()
count = 0

for i in range(n):
    if list[i] == num:
        count += 1

print(count)