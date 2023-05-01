def solution(array):
    doc = {}
    list = []

    for i in array:
# list에 i번째에 value 1추가하기 
# 3의 경우에는 3번 count되니까 value가 3
        try:
            doc[i] += 1
        except:
            doc[i] = 1

        # doc = {"1" : 1, "2" : 1, "3" : 3}

    count = max(doc.values())  # 가장 큰 value 체크하기 : 2
    index = doc.items()  # 딕셔너리에 키값과 value값 동시에 불러오기
    
    
    for i, value in index:
        if count == value:     # if 2 == value:
            list.append(i)    # list = ["1", "2"]
            

    if len(list) == 1:
        print(list)
        return list[0]
        
    
    else:
        print(list)
        return -1


