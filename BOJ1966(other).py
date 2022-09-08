#https://www.acmicpc.net/problem/1966
#큐, 구현, 그리디

#1. 데이터의 개수(N<=100)가 많지 않으므로, 단순히 문제에서 요구하는 대로 구현
#2. 현재 리스트에서 가장 큰 수가 앞에 올 때까지 회전시킨 뒤에 추출
#3. 가장 큰 수가 M이면서 가장 앞에 있을 때 프로그램을 종료

import sys

T = int(sys.stdin.readline())   #테스트케이스 개수

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    queue = list(map(int, sys.stdin.readline().split()))    #우선순위가 들어있는 큐
    queue = [(priority, idx) for idx, priority in enumerate(queue)] #우선순위와 인덱스를 함께 큐에 넣음
                                                                    #enumerate 객체는 (index, data) 순서로 저장된다.
    
    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x : x[0])[0]:   #큐의 맨 앞에 위치한 우선순위가 최댓값인 경우 문서 인쇄
            count += 1
            if queue[0][1] == M:    #인덱스가 M과 같을 때(몇 번째로 인쇄되는지 알고 싶은 문서인 경우)
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))  #맨 앞의 문서를 맨 뒤로 보냄