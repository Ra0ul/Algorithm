def solution(n):
    arr = [[]]
    arr = [[0]*n for i in range(n)]
    
    for i in range(n):
        arr[i][i] = 1
    
    return arr