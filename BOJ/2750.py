n = int(input())

lst = [int(input()) for _ in range(n)]

"""
리스트와 enumerate를 이용해 반복하여 문제를 해결하는 방법을 접근 해 보았는데 실패했다.
이런 정렬 문제는 인덱스만 접근해 푸는 방법이 가장 쉬운 방법인 것 같다.
"""
for i in range(0, n):
    for idx in range(n-1, i, -1):
        if lst[idx] < lst[idx-1]:
            lst[idx], lst[idx-1] = lst[idx-1], lst[idx]

print('\n'.join(map(str, lst)))
