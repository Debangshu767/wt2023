# # avengerslist = ["aae","bsada","ddc","daaa","ewww"]
# # print(avengerslist)
# # print(type(avengerslist))
# # print(avengerslist[2])

# alist = ['item0','item1','item2','item3','item4']
# rlist = [1,2,3,4,5]

# newlist = []

# for i in range(0,len(alist)):
#     newlist.append(alist[i])
#     newlist.append(rlist[i])

# print(newlist)

# #to print last element
# print(newlist[-1])

# #to print item 4 and its rating

# print(newlist[-2:])

ral = [["Spiderman",1],["froot",2],["Blackwidow",3]]

for i in range(0,len(ral) ):
    for j in range(0,len(ral[i])):
        print(ral[i][j])

for item in ral :
    for inneritem in item:
        print(inneritem)