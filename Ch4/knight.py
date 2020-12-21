import time

xy = input()

start_time = time.time()  # 측정 시작

x, y = int(ord(xy[0])-96), int(xy[1])

move_types = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
count = 0

for move in move_types:
  nx = move[0] + x
  ny = move[1] + y
  if nx < 1 or nx > 8 or ny < 1 or ny > 8:
    continue
  count += 1

print(count)

end_time = time.time()  # 측정 종료
print("my answer time :", end_time - start_time)  # 수행 시간 출력

start_time = time.time()  # 측정 시작

# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1

row = y
column = x

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
  # 이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = column + step[1]
  # 해당 위치로 이동이 가능하다면 카운트 증가
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

print(result)

end_time = time.time()  # 측정 종료
print("answer time :", end_time - start_time)  # 수행 시간 출력
