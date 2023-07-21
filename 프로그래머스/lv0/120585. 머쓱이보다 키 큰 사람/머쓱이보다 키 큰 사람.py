def solution(array, height):
    answer = 0
    # for i in array:
    #     if i > height:
    #         answer +=1
    array.append(height)
    array.sort(reverse=True)     
    print(array.index(height))
    return array.index(height)