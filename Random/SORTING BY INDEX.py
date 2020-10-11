#SORTING BY INDEX:

orglst = [2,5,3,1,44,5,33,66,7]
idx_lst = [0]*100005

for x in orglst:
    idx_lst[x] += 1

for i in range(len(idx_lst)):
    if idx_lst[i] != 0:
        freq = idx_lst[i]
        for _ in range(freq):
            print(i, end = " ")
