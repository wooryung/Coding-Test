#[Level 2] https://school.programmers.co.kr/learn/courses/30/lessons/12909
#스택/큐

def solution(s):
    count = 0
    
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
            
        if count < 0:
            break
            
    return count == 0