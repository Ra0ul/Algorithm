def solution(arr, queries):
    answer = []

    for lst in queries:
        table = []
        for i in range(lst[0],lst[1]+1):
            if arr[i] > lst[2]:
                table.append(arr[i])
        if table:
            answer.append(min(table))
        else:
            answer.append(-1)
        
    
    return answer