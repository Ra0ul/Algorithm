def solution(d, budget):
    answer = 0
    d_twin =[]
    """
    지원해 줄 수 있는 최대 부서 구하기
    순열/조합 문제?!  .... 그런데 몇그룹씩 묶는지가 나와야해서 조합쓰는데 제약이 있음...
    경우의 수를 모두 구하려명?!
    
    모두 지원하는 경우부터 5>4>3>2>1순으로?!
    부분탐색 - 팀별 예산이 작은 순서로 고르면 상대적으로 많은 팀에 지원 가능
    
    for i in d:
         sum(d) == budget 
         
    1. 지원할 수 있는 모든 부서 경우의 수를 구하고
    2. 여기서 부서 수가 max인거 찾기?!
    3. 중복은 피해서 고르기
    """
    
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
                
            # print(sum(d)-sum(d_twin))
        print(d_twin)
    
    return answer