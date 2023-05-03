def solution(rank, attendance):

    edit_rank = {}
    rank_list = []
    
    for i in range(len(attendance)):
        if attendance[i] == True: 
            edit_rank[rank[i]] = i
    
    for i in sorted(edit_rank)[:3]:
        rank_list.append(edit_rank[i]) 
        
    
    return 10000*rank_list[0] + 100*rank_list[1] + rank_list[2]