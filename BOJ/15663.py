n, m = map(int, input().split())


origin_n_list = list(map(int, input().split()))
origin_n_list.sort() # 리스트 정렬

def make_print_list(print_list, n_list):
    if len(print_list) == m: 
        print(' '.join(map(str, print_list)))
    
    else: 
        b4 = 0 # 이전에 삭제했던 원소 체크 용
        for ele in n_list:
            if ele not in print_list or n_list.count(ele) > 1: # print_list에 없거나, origin_n_list에 두개 이상 있으면 진행
                if ele == b4 or print_list.count(ele) >= n_list.count(ele): # 이전에 삭제한 원소랑 지금 원소랑 같거나, 갯수 넘어가면 패스
                    continue
                    
                print_list.append(ele) # 원소 일단 추가

                make_print_list(print_list, n_list) # 다시 함수 불러서 이용
                b4 = print_list.pop() # 다 했으면 삭제 (이전 원소 저장)
                

            
make_print_list([], origin_n_list) # 처음 print_list = []