#https://www.acmicpc.net/problem/1874
#스택에 원소를 삽입할 때는 단순히 특정 수에 도달할 때까지 삽입
#스택에서 원소를 연달아 빼낼 때 내림차순을 유지할 수 있는지 확인
n = int(input())

count = 1
stack = []
result = []

for _ in range(n): #원소 개수만큼 반복
    num = int(input())
    while count <= num:    #입력받은 숫자에 도달할 때까지 삽입
        stack.append(count)
        count += 1
        result.append('+')
           
    if stack[-1] == num:   #스택의 최상위 원소가 입력받은 숫자와 같을 때 출력
        stack.pop()
        result.append('-')
    else:   #불가능한 경우
        print('NO')
        exit(0) #프로그램 종료
        
print('\n'.join(result))    #가능한 경우