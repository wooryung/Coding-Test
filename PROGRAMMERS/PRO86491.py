#[Level 1] https://school.programmers.co.kr/learn/courses/30/lessons/86491
#완전탐색

def solution(sizes):
    w = 0
    h = 0
    
    for s in sizes:
        s.sort()
    
    for i in range(len(sizes)):
        if sizes[i][0] >= w:
            w = sizes[i][0]
        
        if sizes[i][1] >= h:
            h = sizes[i][1]
            
    return w * h