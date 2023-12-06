def solution(data, ext, val_ext, sort_by):
    answer = []
    m = {"code":0, "date":1, "maximum":2, "remain":3}
    
    #val_ext 보다 작은데이터만 뽑기
    for db in data:
        #print(db[m[ext]])
        if db[m[ext]] < val_ext:
            answer.append(db)
    
    #sort_by 기준으로 정렬하기
   # print("이전", answer)
    answer.sort(key=lambda x : x[m[sort_by]])
    #print("이후", answer)
    return answer