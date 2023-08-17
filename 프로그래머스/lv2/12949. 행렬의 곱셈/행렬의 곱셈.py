def solution(arr1, arr2):
    
    # column = len(arr1) 
    # row = len(arr2[0])
    # row2 = len(arr1[0])
    answer = []
    
    for i in range(len(arr1)):
        arr = []
        for c in range(len(arr2[0])):
            result = 0
            for u in range(len(arr1[0])):
                result += arr1[i][u]*arr2[u][c]
            arr.append(result)
        answer.append(arr)

    return answer