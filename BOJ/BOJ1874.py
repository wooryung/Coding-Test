#https://www.acmicpc.net/problem/1874
#스택, 그리디
#결과는 맞으나 계속 시간초과가 났다 ㅠ.ㅠ
import sys

n = int(input())
num_list = [int(sys.stdin.readline().strip()) for i in range(n)] #엔터를 기준으로 입력받을 때

candidate = list()
possible = True
check = True

for i in range(num_list[0]):    #첫 번째 수 출력
    candidate.append('+')
candidate.append('-')
max = num_list[0]   #지금까지 가장 큰 수

for i in range(1, n):
    # if num_list[i] == n:    #가장 큰 수가 나온 경우 다음 숫자들은 모두 내림차순이어야 함
    #     for _ in range(max, num_list[i]):
    #         candidate.append('+')
    #     candidate.append('-')

    #     for j in range(i+1, n):
    #         if num_list[j] > num_list[j-1]: #내림차순이 아닐 경우
    #             possible = False
    #             break  
    #         else:
    #             candidate.append('-')
    #     break
    
    if num_list[i] < num_list[i-1]: #다음 수가 작으면 pop. 단, 스택에 들어있는 순서대로여야 함
                                    #지금까지의 num_list 중에 현재 숫자와 다음 숫자 사이의 숫자가 없으면 불가능
        if num_list[i-1] == num_list[i] + 1:    #1 차이 나면 체크 안 해도 됨
            candidate.append('-')
        else:
            for j in range(num_list[i]+1, num_list[i-1]):
                for k in range(i):
                    check = False
                    if num_list[k] == j:
                        check = True 
                        j += 1
            if check:
                candidate.append('-')
            else:
                possible = False
                break
        
    elif num_list[i] > num_list[i-1]:   #다음 수가 크면 그 수까지 push한 후 pop
        for _ in range(max, num_list[i]):
            candidate.append('+')
        candidate.append('-')
        max = num_list[i]

if possible:
    for cand in candidate:
        print(cand)     
else:
    print('NO')
