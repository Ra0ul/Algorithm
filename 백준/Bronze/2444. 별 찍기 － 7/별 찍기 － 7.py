num = int(input())

for i in range(1, num + 1):
    answer = ""
    answer = (" " * (num - i)) + ("*" * (2 * i - 1))
    print(answer)

for i in range(num - 1, 0, -1):
    answer = ""
    answer = (" " * (num - i)) + ("*" * (2 * i - 1))
    print(answer)