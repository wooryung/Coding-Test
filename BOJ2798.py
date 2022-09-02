#https://www.acmicpc.net/problem/2798
#조합을 사용하여 풀이
from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

candidates = list(combinations(cards, 3))
max = 0
for candidate in candidates:
    sum = candidate[0] + candidate[1] + candidate[2]
    if (sum <= M and sum > max):
        max = sum
        
print(max)