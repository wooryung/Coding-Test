#https://www.acmicpc.net/problem/2798
#단순 3중 반복문을 사용하여 풀이
#순열을 직접 구현하는 경우

N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
for i in range(0, len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= M:
                result = max(result, sum)
                
print(result)