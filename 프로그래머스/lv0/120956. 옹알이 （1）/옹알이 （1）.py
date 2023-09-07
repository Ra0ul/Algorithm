from itertools import permutations

def solution(babbling):
    answer = 0
    
    new_words = []
    words = ["aya", "ye", "woo", "ma"]
    
    for i in range(2,5):
        mixed_word = list(permutations(words, i))
        
        for j in mixed_word:
            blank = ''
            for k in j:
                blank += k
                
            new_words.append(blank)
            
    new_words += words
    
    for i in babbling:
        if i in new_words:
            answer += 1
    return answer