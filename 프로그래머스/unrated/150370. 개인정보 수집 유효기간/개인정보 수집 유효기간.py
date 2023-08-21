
def solution(today, terms, privacies):
    answer = []
    rule={}
    # end_date
    
    sign_in=today.split(".")
    today_date = int(sign_in[0]+sign_in[1]+sign_in[2])
    print("오늘",today_date)
    
    for i in terms:
        term_list = i.split()
        rule[term_list[0]] = int(term_list[1])
    
    #수집일
    for i_num, i in enumerate(privacies):
        sign_in = i.split('.')
        
        y = int(sign_in[0])
        m = int(sign_in[1])
        d = int(sign_in[2][:2])
        # print("수집", y,m,d)
        
        #만료일 계산
        m += rule[sign_in[2][-1]]
        d -= 1
        if d == 0:
            m -=1
            d = 28
        if m > 12:
            if m%12 != 0:
                y+= m//12
                m = m%12
            else:
                y+= m//12-1
                m = 12
                
        
        # print("만료", y,m,d)
        
        end_date = str(y)
        if len(str(m)) ==1:
            end_date += "0"+str(m)
        else:
            end_date += str(m)
        if len(str(d)) ==1:
            end_date += "0"+str(d)
        else:
            end_date += str(d)    
        
        print("⭐️", end_date)
        
        if int(today_date) > int(end_date):
            answer.append(i_num+1)
    return answer