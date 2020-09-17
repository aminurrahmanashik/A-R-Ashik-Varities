
n = int(input())
s = set(map(int,input().split()))
op_n = int(input())
lst = []
for i in range(op_n):
    lst = input().split()
    if len(lst) == 1:
        getattr(s,lst[0])()
    else:
        getattr(s,lst[0])(int(lst[1]))

print(sum(s))

