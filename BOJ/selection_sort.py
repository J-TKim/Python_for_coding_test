n = int(input())

lst = [int(input()) for _ in range(n)]
print_lst = []

for i in range(0, n):
    min_ele = min(lst)
    print_lst.append(min_ele)
    lst.remove(min_ele)
        

print('\n'.join(map(str, print_lst)))
