import time

n = int(input())

start_time = time.time()  # 측정 시작


total = 0
for i in range(1, n+2):
  if i == 3 or i == 13:
    total += 60 * 60
  else:
    mini = 0
    sec = 0
    time_c = str(mini) + str(sec)
    for _ in range(3600 - 1):
      sec += 1
      if sec >= 60:
        sec -= 60
        mini += 1

      time_c = str(mini) + str(sec)
      if "3" in time_c:
        total += 1

print(total)

end_time = time.time()  # 측정 종료
print("my answer time :", end_time - start_time)  # 수행 시간 출력

start_time = time.time()  # 측정 시작

# H를 입력받기
#h = int(input())
h = n

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)

end_time = time.time()  # 측정 종료
print("answer time :", end_time - start_time)  # 수행 시간 출력
