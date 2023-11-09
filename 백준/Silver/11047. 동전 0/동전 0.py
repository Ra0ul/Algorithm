from sys import stdin

input = stdin.readline
n, k = map(int, input().split())
num = []
answer = 0
for i in range(n):
    b = int(input())
    if b <= k:
        num.append(b)

while num and k >= 0:
    number = num.pop()
    answer += k // number
    k = k % number

print(answer)