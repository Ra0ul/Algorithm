def solution(num_list):
    count = 0
    count_list = []

    for i in num_list:
        num = i
        while num != 1:
            if num%2==0:
                num=num/2
            else:
                num=(num-1)/2
            count += 1
        
    count_list.append(count)
    
    print(count)
            
    
    return count