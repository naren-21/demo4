list1 = [10,20,25,30,35]
list2 = [40,45,60,75,90]
list_oddeven = []
dump = []

for i in list1:
    if i%2 != 0:
        list_oddeven.append(i)
    else:
        dump.append(i)

for j in list2:
    if j%2 == 0:
        list_oddeven.append(j)
    else:
        dump.append(j)

print("req_list is",list_oddeven)


