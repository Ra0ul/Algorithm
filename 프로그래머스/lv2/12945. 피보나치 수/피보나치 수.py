
def solution(n):
	answer = [0,1]
	"""
	1. 피보나치 수를 가진 리스트를 만들기
	-> n번째 수는 (n-2번째 수 + n-1번째 수) 
	2. 리스트에서 n번째 수를 꺼내기
	3. 나누어 나머지를 리턴
	"""
	for i in range(n+1):
		if i >= 2:
			answer.append(answer[i-2] + answer[i-1])
		else:
			pass

    # 나머지를 구하라 %1234567
	return answer[n]%1234567

