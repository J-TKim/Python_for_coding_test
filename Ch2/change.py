import time

# 내가 작성한 코드
start_time = time.time()

#money = int(input("돈 입력: "))
money = 1260
count = 0 # 동전 몇가지를 사용했는지 카운트

# 동전 종류의 리스트
lis = [500, 100, 50, 10]

for coin in lis: # 500, 100, 50, 10을 반복
  count += money // coin # coin이 몇개가 필요한지 추가
  money = money % coin # coin으로 거슬러 주고 남은 돈 계산

print(count)

end_time = time.time()
print("my code time :", end_time - start_time)


# 책 답안 코드
start_time = time.time()

n = 1260
count = 0

# 큰 단위의 화폐부터 차례로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
  n %= coin

print(count)

end_time = time.time()
print("answer code time :", end_time - start_time)