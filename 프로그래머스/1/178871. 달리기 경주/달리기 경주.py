#OUTOFTIME1
"""
def solution(players, callings):
    for i in callings:
        num = players.index(i)
        players[num-1], players[num] = players[num], players[num-1]
    
    return players
"""

#OUTOFTIME2
"""
from collections import deque
rank = {}

def rank_update(n):
    for i,j in enumerate(n):
        rank[j] = i

def solution(players,callings):
    answer = []
    call = deque(callings)
    
    rank_update(players)
    
    
    while call:
        i = call.popleft()
        num = rank[i]
        new_list = list(reversed(players[num-1:num+1]))
        players[num-1:num+1] = new_list
        
        rank_update(players)
        
"""

def solution(players,callings):
    answer = []
    rank = {}
    for i ,j in enumerate(players):
        rank[j] = i
    
    for i in callings:
        num = rank[i]
        rank[i] -=1
        rank[players[num-1]] +=1
        
        players[num], players[num-1] = players[num-1], players[num]    
    return players