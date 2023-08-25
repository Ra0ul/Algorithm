"""
불량 이용자 신고 처리결과 발송

한번에 한명의 유저를 신고
신고 횟수 제한 없음 - 서로 다른 유저를 신고 가능

k번 이상 신고된 유저는 이용정지
신고한 모든 유저에게 정지 사실을 메일로 발송

유저가 신고한 모든 내용 취합하여 마지막에 한꺼번에 정지하면서 메일 발송

id_list : 이용자의 id 배열
report : 이용자가 신고한 이용자의 id
k : 정지 기준이 되는 신고 횟수

result :  각 유저별 처리결과 메일을 받는 횟수를 배열에 담기
"""


def solution(id_list, report, k):
    answer = []
    print(id_list)
    print(report)
    print(k)
    return answer