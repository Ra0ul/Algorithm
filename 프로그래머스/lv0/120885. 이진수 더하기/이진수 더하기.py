def solution(bin1, bin2):
    answer = ''
    sum_bin =''
    new_list ={}
    count =0 
    
    sum_bin = str(int(bin1)+int(bin2))
    for i in sum_bin[::-1]:
        new_list[count] = int(i)
        count+=1
    print("원본:", new_list)
    count = 0
    for key, value in new_list.items():
        try:
            if value >= 2:
                new_list[key+1] +=1
                new_list[key] = new_list[key]-2
        except:
            count +=1
            new_list[key] = new_list[key]-2   
    print(new_list)   
    
    for value in new_list.values():
        answer += str(value)
    if count == 1:
        answer +="1"
    return answer[::-1]