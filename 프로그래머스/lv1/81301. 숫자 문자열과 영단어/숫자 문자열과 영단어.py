def solution(s):
    
    alpha_num = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    for i_num, i in enumerate(alpha_num):
        s = s.replace(i,str(i_num))
    
    return int(s)