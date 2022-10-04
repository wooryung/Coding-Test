#[Level 1] https://school.programmers.co.kr/learn/courses/30/lessons/86491
#완전탐색

def solution(sizes):
    return max(max(s) for s in sizes) * max(min(s) for s in sizes)