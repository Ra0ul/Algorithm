"""
왼손* 오른손# 엄지손가락 
왼손만사용 147
오른만 사용 369
가운데는 가까운 손이 2580
오른손잡이 /왼손잡이 같은거리면

numbers : 순서대로 누르기
hand : 손잡이
result : 왼손오른손(문자열)

[[0,0,0],
[0,0,0],
[0,0,0],
[*,0,#]]

"""
# 키패드 만들기
keypad = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), '*':(3,0), 0:(3,1), '#':(3,2)}

def solution(numbers, hand):
    # 오른손 왼손 현재 위치 저장
    state = {"L":(3,0),"R":(3,2)}
    answer = ''
    
    # 147 일괄 L | 369 일괄 R 지정
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            state["L"] = keypad[i]
            answer += "L"
        elif i == 3 or i == 6 or i == 9:
            state["R"] = keypad[i]
            answer += "R"
        else: #2,5,8,0
            left_side = abs(state["L"][0] - keypad[i][0]) + abs(state["L"][1] - keypad[i][1])
            right_side = abs(state["R"][0] - keypad[i][0]) + abs(state["R"][1] - keypad[i][1])
            
            #둘이 같으면
            if left_side == right_side:
                answer += hand[0].swapcase()
                state[hand[0].swapcase()] = keypad[i]
                
            #오른쪽이 가까우면
            elif left_side > right_side:
                answer += "R"
                state["R"] = keypad[i]
                
            #왼쪽이 가까우면
            else:
                answer += "L"
                state["L"] = keypad[i]
        
    return answer