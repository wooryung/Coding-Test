#[Level 1] https://school.programmers.co.kr/learn/courses/30/lessons/1845
#해시

def solution(nums):
    return min(len(nums)/2, len(set(nums)))
