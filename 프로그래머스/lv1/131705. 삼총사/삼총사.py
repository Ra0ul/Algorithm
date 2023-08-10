"""
학생 번호 3명 더해서 = 0 : 삼총사!
삼총사 멤버는 중복가능
"""
from itertools import combinations
def solution(number):
    answer = 0
    # number 리스트에서 세명짝꿍으로 뽑아낼 수있는 경우의 수 구하기
    trio = list(combinations(number,3))
    # 나온 수를 모두 더해서 0 이 된다면 삼총사!
    for i in trio:
        if sum(i) == 0:
            answer += 1
    return answer