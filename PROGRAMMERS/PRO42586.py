#[Level 2] https://school.programmers.co.kr/learn/courses/30/lessons/42586
#스택/큐

import math

def solution(progresses, speeds):
    answer = []
    days = []   #작업 기간
    count = 1
    
    for i in range(len(progresses)):
        rest = 100 - progresses[i]
        day = math.ceil(rest / speeds[i])
        days.append(day)
        
    biggest = days[0]
    for i in range(1, len(days)):  
        if days[i] <= biggest:
            count += 1
        else:
            answer.append(count)
            count = 1
            biggest = days[i]
            
    answer.append(count)
    
    return answer