list = [12,38,27,62,7,12]

for i in range(0, len(list)):
    for j in range(i+1, len(list)):
        if list[j] < list[i]:
            list[i], list[j] = list[j], list[i]

print(list)