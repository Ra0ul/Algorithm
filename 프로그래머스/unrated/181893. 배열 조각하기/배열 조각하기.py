def solution(arr, query):
    answer = []
    for i, j in enumerate(query):
        if i%2:
            arr = arr[j:]
        else:
            arr = arr[:j+1]
    return arr