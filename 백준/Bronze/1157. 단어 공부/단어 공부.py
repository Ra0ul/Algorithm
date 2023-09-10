from sys import stdin

input = stdin.readline

word_doc = {}
max_list = []

word = input().rstrip()
word = word.upper()

for i in word:
    try:
        word_doc[i] += 1
    except:
        word_doc[i] = 1

max_num = max(word_doc.values())

for i, j in word_doc.items():
    if j == max_num and len(max_list) == 0:
        max_list.append(i)
    elif j == max_num and len(max_list) > 0:
        max_list.pop()
        max_list.append("?")
print(*max_list)