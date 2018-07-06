import sys
blind_num = int(input())
if blind_num <= 1 or blind_num >= 50:
    sys.exit(0)
s = input()
blind = s.split(" ")
dict_blind = []; sick_num = 1
for item in range(0, len(blind)):
    blind_pro = {}
    if item == 0:
        blind_pro["issick"] = 1
    else:
        blind_pro["issick"] = -1
    blind_pro["pos"] = int(blind[item])
    dict_blind.append(blind_pro)
dict_blind.sort(key=lambda e: abs(e.__getitem__("pos")))

while(1):
    if len(dict_blind) <= 1:
        break
    for i in range(0, len(dict_blind)):
        dict_blind[i]['pos'] += 0.5  # change to 0.5
    j = 0
    while j < len(dict_blind)-1:
        if dict_blind[j]["pos"] == 0 or dict_blind[j]["pos"] == 100:
            dict_blind.pop(j)
            continue
        elif dict_blind[j]["pos"] + dict_blind[j+1]["pos"] == 0:
            dict_blind[j]["pos"] = -dict_blind[j]["pos"]
            dict_blind[j + 1]["pos"] = -dict_blind[j + 1]["pos"]
            if dict_blind[j]["issick"] + dict_blind[j+1]["issick"] == 0:
                sick_num += 1
                dict_blind[j]["issick"] = 1
                dict_blind[j+1]["issick"] = 1
        j += 1
print(sick_num)
