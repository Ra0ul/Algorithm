import sys

N = int(sys.stdin.readline())
answer = []
for _ in range(N):
    answer.append(int(sys.stdin.readline()))
answer.sort()
for i in answer:
    print(i)
    