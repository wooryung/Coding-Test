#https://www.acmicpc.net/problem/1966
#큐, 구현, 그리디
#문제 이해가 어려웠다 ㅠ.ㅠ
import sys, queue

T = int(sys.stdin.readline())    #테스트케이스 개수
nmList = []
priority = []

for _ in range(T):  #입력 받기
    nmList.append(list(map(int, sys.stdin.readline().split()))) #N,M
    priority.append(list(map(int, sys.stdin.readline().split())))   #N개 문서의 중요도

for i in range(T):
    printer = queue.PriorityQueue(maxsize=nmList[i][0]) #N
    
    for j in range(nmList[i][0]):   #N
        printer.put((-priority[i][j], j))   #내림차순으로 우선순위를 정하기 위해 -를 붙여줌
            
    result = 0  
    for _ in range(nmList[i][0]):   #N
        result += 1
        num = printer.get()[1]
        
        if num == nmList[i][1]: #M
            print(result)
            # continue
      