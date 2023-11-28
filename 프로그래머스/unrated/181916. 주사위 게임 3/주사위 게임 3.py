
def solution(a, b, c, d):
    answer = 0
    lst = [a,b,c,d]
    length = len(set(lst))
    
    if length == 1:
        return a*1111
    elif length == 4:
        return min(lst)
      
    else:
        max_num_list = []
        num_list = []
        count_num = {}
        for i in lst:
            try:
                count_num[i] += 1
            except:
                count_num[i] = 1
        
        
        for key, value in count_num.items():
            if max(count_num.values()) == value:
                max_num_list.append(key)
            num_list.append(key)
        
        arr = set(num_list) - set(max_num_list)
        p = max_num_list.pop()
        if not arr:
            q = max_num_list.pop()
            return (p + q) * abs(p - q)
        
        elif len(arr) == 1:
            q = arr.pop()
            return (10 * p + q)**2
            
        else: 
            q = arr.pop()
            r = arr.pop()
            return  q*r
            