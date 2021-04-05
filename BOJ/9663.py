import bisect

n = int(input())

# 만점 갯수 카운팅
cnt = 0
d1 = set()
d2 = set()
cl=[i for i in range(n)]
def check(queen, rs=0):
    
    # 퀸이 모두 놓이면 cnt += 1
    if queen >= n:
        global cnt
        cnt += 1
        return
    
    
    for idx, col in enumerate(cl):
        rpw = rs+col
        cmr = col-rs
        # 말이 놓인 대각선이 아니면 실행
        global d1, d2
        if rpw not in d1 and cmr not in d2:
            
            # 말이 놓인 col은 리스트에서 삭제
            del cl[idx]
            
            # 말이 놓인 대각선은 제외하기 위한 코드
            d1.add(rpw)
            d2.add(cmr)
            
            # 바뀐 체스판으로 다음 수 확인 (다음 행에 한정해서 찾음))
            check(queen=queen+1, rs=rs+1)
            
            bisect.insort(cl, col)  

            d1.remove(rpw)
            d2.remove(cmr)

check(0)
print(cnt)
