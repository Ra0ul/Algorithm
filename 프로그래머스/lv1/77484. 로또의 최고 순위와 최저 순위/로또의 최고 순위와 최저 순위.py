"""
1-45까지 숫자 중 6개 찍기
왜 낙서!!
최고와 최저 순위 맞추기

맞는 번호는 순서 상관 없음
lottos= 민우 구매한 길이 6인 정수 배열
0은 알아볼 수 없는 숫자
같은 숫자 중복 없음

win_nums =당첨스

1,31 일단 2개 무조건 맞음 // 2개 무조건 틀림 ==> 4개 맞거나(3등) 2개만 맞거나(5등)
"""



def solution(lottos, win_nums):
    answer = []
    count_num = {'in':0, 'guess':0}
    grade ={6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    for i in lottos:
        if i == 0:
            count_num['guess'] +=1
        elif i in win_nums:
            count_num['in'] +=1
            
    answer = [grade[count_num['in']+count_num['guess']], grade[count_num['in']] ]
    return answer