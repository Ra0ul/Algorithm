homework = [i for i in range(1, 31)]

for i in range(1, 29):
    num = int(input())
    homework.remove(num)
homework.sort(reverse=True)

while homework:
    print(homework.pop())