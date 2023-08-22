def solution(n, lost, reserve):
    answer = 0
    check_list = {}
    lost.sort()

    # 도난 전 체크
    for i in range(1, n+1):
        if i in reserve:
            check_list[i] = 2
        else:
            check_list[i] = 1
        if i in lost:
            check_list[i] -=1
    print("전 : ", check_list, reserve)
    
    
    #빌려주기
    for i in lost:
        if check_list[i] == 0:
            if i-1 in reserve and check_list[i-1]==2:
                check_list[i-1] -=1
                check_list[i] +=1
            elif i+1 in reserve and check_list[i+1]==2:
                check_list[i+1] -=1
                check_list[i] +=1
        print("⭐️:",i, check_list)
    
    for i in check_list.values():
        if i >0:
            answer += 1
        
    print("후 : ", check_list)
    return answer