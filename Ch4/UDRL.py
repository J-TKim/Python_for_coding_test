import time


n = int(input())

start_time = time.time()  # 측정 시작

data = list(map(str, input().split()))

x = 1
y = 1

nx = x
ny = y

for ele in data:
  if ele == "R":
    ny = y + 1
  elif ele == "U":
    nx = x - 1
  elif ele == "D":
    nx = x + 1
  else:
    ny = y - 1


  if ny < 1 or nx < 1 or ny > n or nx > n:
    continue
  x, y = nx, ny

print(x, y)

end_time = time.time()  # 측정 종료
print("time :", end_time - start_time)  # 수행 시간 출력

start_time = time.time()  # 측정 시작

#n = int(input())
x, y = 1, 1
#plans = input().split()
plans = data

# L, R, U, D에 따른 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 이동수행
  x, y = nx, ny

print(x, y)

end_time = time.time()  # 측정 종료
print("time :", end_time - start_time)  # 수행 시간 출력
