import time


start_time = time.time()  # 측정 시작

n, m = map(int, input().split())

data = list(map(int, input().split()))
data.sort()
biggest = data[0]

for _ in range(n-1):
  data = list(map(int, input().split()))
  data.sort()

  if data[0] > biggest:
    biggest = data[0]

print(biggest)

end_time = time.time()  # 측정 종료
print("my answer time :", end_time - start_time)  # 수행 시간 출력


start_time = time.time()  # 측정 시작

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = min(data)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)

end_time = time.time()  # 측정 종료
print("answer with min() time :", end_time - start_time)  # 수행 시간 출력


start_time = time.time()  # 측정 시작

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  for a in data:
    min_value = min(min_value, a)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)

end_time = time.time()  # 측정 종료
print("answer with double loop time :", end_time - start_time)  # 수행 시간 출력