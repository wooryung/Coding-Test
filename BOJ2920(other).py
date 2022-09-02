#https://www.acmicpc.net/problem/2920
#배열 내에서 오름차순과 내림차순을 체크하는 방식
mlist = list(map(int, input().split()))
ascending = True
descending = True

for i in range(1, 8):
    if (mlist[i] < mlist[i-1]):
        ascending = False
    elif (mlist[i] > mlist[i-1]):
        descending = False
        
if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed') 