a, b = map(int, input().strip().split(' '))

answer = []

for i in range(b): 
    answer.append("*"*a)

for num in range(len(answer)):
    star = answer[num]
    
    print(star)