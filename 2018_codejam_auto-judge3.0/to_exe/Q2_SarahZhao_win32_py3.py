import copy
max_pro = 0
def find(list_foot_pmt, max_pmt):
    max_pmtn = max_pmt
    a = list_foot_pmt.pop(0)
    for i in range(0, len(list_foot_pmt)):
        max_pmt = max_pmtn
        list_foot_pmt1 = copy.deepcopy(list_foot_pmt)
        b =list_foot_pmt1.pop(i)
        max_pmt += pro_matrix[a][b]
        if len(list_foot_pmt1) > 0:
            find(list_foot_pmt1, max_pmt)
        else:
            global max_pro
            if max_pmt > max_pro:
                max_pro = max_pmt
            return

N = int(input())
pro_matrix = []
for j in range(0, N):
    str_tmp = input()
    pro_row = str_tmp.split(" ")
    pro_matrix.append(pro_row)
for i in range(0, N):
    for j in range(0, N):
        pro_matrix[i][j] = int(pro_matrix[i][j])

list_foot = []
for i in range(0, N):
    list_foot.append(i)

max = 0
max_pro_odd = 0
if len(list_foot) % 2 == 0:
    find(list_foot, max)
    print(max_pro)
else:
    for i in range(0, N):
        list_foot_tmp = copy.deepcopy(list_foot)
        list_foot_tmp.pop(i)
        find(list_foot_tmp, max)
        if max_pro > max_pro_odd:
            max_pro_odd = max_pro
    print(max_pro_odd)







