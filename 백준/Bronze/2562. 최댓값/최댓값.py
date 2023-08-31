count = 1
num = int(input())

for i in range(2, 10):
    n = int(input())
    if num < n:
        num = n
        count = i

print(num)
print(count)