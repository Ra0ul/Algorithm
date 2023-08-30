import sys

num = int(sys.stdin.readline().rstrip())
for i in range(num):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(f"Case #{i+1}: {a+b}")