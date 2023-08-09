def solution(d, budget):
    d_twin =[]
   
    # 모든 팀을 지원 가능한 경우    
    if sum(d) <= budget:
        return len(d)
    
    #일부 팀만 지원 가능한 경우
    else:
        #지원금액이 큰 팀부터 정렬
        d.sort(reverse=True)
        print("원본 :", d)
        
        #큰 순서대로 제외하고 전부 더해보기
        for i in d:
            d_twin.append(i)
            if sum(d)-sum(d_twin) <= budget:
                return (len(d)-len(d_twin))