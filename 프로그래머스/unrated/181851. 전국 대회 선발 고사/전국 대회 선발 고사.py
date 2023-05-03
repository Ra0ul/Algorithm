def solution(rank, attendance):
    """
    일단 참석가능한 학생들 중에서 순위가 높은 순서대로 세명을 선발!
    1. 참석 가능한 학생들의 list 인덱스를 뽑아낸다
    2. 해당 인덱스를 기준으로 rank 리스트를 다시 정의하고
    3. 리스트에서 숫자가 작은 순서대로 3명을 선발한다.
    $$$4. 선발한 등수의 인덱스가 필요함
    10000 × a + 100 × b + c 식에 넣어주면 될듯!
    """
    #1. 참석 가능한 학생들의 list 인덱스를 뽑아낸다
    edit_rank = {}
    rank_list = []
    
    for i in range(len(attendance)):
        if attendance[i] == True: 
            edit_rank[rank[i]] = i
    
    for i in sorted(edit_rank)[:3]:
        rank_list.append(edit_rank[i]) 
        
    
    return 10000*rank_list[0] + 100*rank_list[1] + rank_list[2]