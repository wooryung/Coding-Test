#ascending과 descending 배열을 지정해두고 입력받은 배열과 같은지 비교하는 방식
mlist = list(map(int, input().split()))
ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

if (mlist == ascending):
    print("ascending")
elif (mlist == descending):
    print("descending")
else:
    print("mixed")