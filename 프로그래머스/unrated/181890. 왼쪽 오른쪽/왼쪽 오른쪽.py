def solution(str_list):
    if "l" in str_list and "r" in str_list:
        l = str_list.index("l")
        r = str_list.index("r")
        
        if l<r:
            return str_list[:l]
        else:
            return str_list[r+1:]
        
    elif "l" in str_list:
        l = str_list.index("l")
        return str_list[:l]
    elif "r" in str_list:
        r = str_list.index("r")
        return str_list[r+1:]
    else:
        return []
        