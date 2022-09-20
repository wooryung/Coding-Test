#[Level1] https://school.programmers.co.kr/learn/courses/30/lessons/12928
def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
    #약수는 n 자기 자신을 제외하고 n/2 이상의 값은 나올 수 없다!
    #ex) 12의 약수는 1, 2, 3, 4, 6, 12 -> 7~11 중에서는 12의 약수가 나올 수 없다.