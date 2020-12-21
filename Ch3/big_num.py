import time

# N, M, K를 공백으로 구분하여 입력받기
#N, M, K = int(input()).split()
n, m, k = 5, 8, 3

# N개의 수를 공백으로 구분하여 입력받기
#data = list(map(int, input().split()))
data = [2, 4, 5, 4, 6]

start_time = time.time()  # 측정 시작

data.sort(reverse=True)

count = 0
sum = 0

for _ in range(m):
  if count >= k:
    sum += data[1]
    count = 0
    continue
  sum += data[0] 
  count += 1

print(sum)

end_time = time.time()  # 측정 종료
print("my answer time :", end_time - start_time)  # 수행 시간 출력


# N, M, K를 공백으로 구분하여 입력받기
#n, m, k = map(int, input().split())
n, m, k = 5, 8, 3

# N개의 수를 공백으로 구분하여 입력받기
#data = list(map(int, input().split()))
data = [2, 4, 5, 4, 6]

start_time = time.time()  # 측정 시작

data.sort() # 입력받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
  for i in range(k):# 가장 큰 수를 k번 더하기
    if m == 0: # m이 0이라면 반복문 탈출
      break
    result += first
    m -= 1 # 더할 때마다 1씩 빼기
  if m == 0: # m
    break
  result += second # 두 번째로 큰 수를 한 번 더하기
  m -= 1 # 더할 때마다 1씩 빼기

print(result)

end_time = time.time()  # 측정 종료
print("simple answer code time :", end_time - start_time)  # 수행 시간 출력


# N, M, K를 공백으로 구분하여 입력받기
#n, m, k = map(int, input().split())
n, m, k = 5, 8, 3

# N개의 수를 공백으로 구분하여 입력받기
#data = list(map(int, input().split()))
data = [2, 4, 5, 4, 6]

start_time = time.time()  # 측정 시작

data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번재로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)

end_time = time.time()  # 측정 종료
print("answer code time :", end_time - start_time)  # 수행 시간 출력
