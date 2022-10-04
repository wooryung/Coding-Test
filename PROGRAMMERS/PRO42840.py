#[Level 1] https://school.programmers.co.kr/learn/courses/30/lessons/42840
#완전탐색

def solution(answers):
    answer = []    
    m1 = [1,2,3,4,5]    #5
    m2 = [2,1,2,3,2,4,2,5]  #8
    m3 = [3,3,1,1,2,2,4,4,5,5]  #10   
    c1, c2, c3 = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == m1[i%5]:
            c1 += 1
        if answers[i] == m2[i%8]:
            c2 += 1
        if answers[i] == m3[i%10]:
            c3 += 1
    
    value = max(c1, c2, c3)
    if c1 == value:
        answer.append(1)
    if c2 == value:
        answer.append(2)
    if c3 == value:
        answer.append(3)
        
    return answer