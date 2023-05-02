def solution(chicken):
    answer = 0
    coupon = chicken

    while coupon >= 10:
        onhouse= coupon//10 
        answer += onhouse
        coupon = coupon%10 + onhouse
    return answer 
