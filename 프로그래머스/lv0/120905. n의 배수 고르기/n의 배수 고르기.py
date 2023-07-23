def solution(n, numlist):
    answer = []
    for i in numlist:
        print(i)
        if i%n == 0:
            answer.append(i)
    return answer