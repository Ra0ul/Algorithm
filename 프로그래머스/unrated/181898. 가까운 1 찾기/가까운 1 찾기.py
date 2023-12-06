def solution(arr, idx):
    for i, j in enumerate(arr[idx:]):
        if j:
            return i+idx
    return -1