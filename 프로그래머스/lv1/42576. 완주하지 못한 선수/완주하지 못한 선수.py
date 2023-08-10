#효율성 테스트 시간 초과ㅠㅠ

"""
def solution(participant, completion):
    answer = ''
    for i in completion:
        participant.remove(i)
    return participant[0]
    
"""

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i_num, i in enumerate(completion):
        if i != participant[i_num]:
            print(i)
            return participant[i_num]
    return participant[len(participant)-1]
    
   