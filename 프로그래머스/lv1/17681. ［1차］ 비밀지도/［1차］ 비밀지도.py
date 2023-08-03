def solution(n, arr1, arr2):
    answer = []
    map1=[]
    map2=[]
    secret_map=[]
    
    
    for i in range(n):
        map1.append(int(bin(arr1[i])[2:]))
        map2.append(int(bin(arr2[i])[2:]))
        secret_map.append(str(map1[i]+map2[i]))
        
        if len(secret_map[i]) < n:
            blank = '0'*(n-len(secret_map[i]))
            secret_map[i] = blank+secret_map[i]
            
        line =''
        
        for u in secret_map[i]:
            if int(u) >= 1:
                line += '#'
            else:
                line += ' '
        
        answer.append(line)
        
    return answer