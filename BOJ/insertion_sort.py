import bisect

n = int(input())
lst = [int(input()) for _ in range(n)]

print_lst = [lst.pop()]

for _ in range(0, n-1): # n
    pop = lst.pop()
    bisect.insort(print_lst, pop) # n
        
print('\n'.join(map(str, print_lst)))
