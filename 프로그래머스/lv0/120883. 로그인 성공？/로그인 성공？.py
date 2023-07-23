def solution(id_pw, db):
    answer = ''
    id = id_pw[0]
    pw = id_pw[1]
    id_list=[]
    pw_list=[]
    
    for i in range(len(db)):
        if id == db[i][0]:
            id_list.append(i)
        if pw == db[i][1]:
            pw_list.append(i)
            
    if id_list == []:
        return "fail"
    
    for i in id_list:
        if i in pw_list:
            return "login"
        else:
            return "wrong pw"