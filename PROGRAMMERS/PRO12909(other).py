#[Level 2] https://school.programmers.co.kr/learn/courses/30/lessons/12909
#스택/큐

def solution(s):
    stack = list()
    
    for c in s:
        if c == '(':
            stack.append(c)

        if c == ')':
            try:
                stack.pop()
            except IndexError:
                return False

    return len(stack) == 0