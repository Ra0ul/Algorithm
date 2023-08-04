def solution(arr1, arr2):
    answer = arr1
    for i in range(len(arr1)):
        for u in range(len(arr1[i])):
            answer[i][u] = arr1[i][u]+arr2[i][u]
    return answer