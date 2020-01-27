arr=[]
for i in range(5):
    row=list(map(int,input().split()))
    arr.append(row)

for i in range(5):
    for j in range(5):
        if arr[i][j]==1:
            index_i=i
            index_j=j
store=abs(index_j-2)+abs(index_i-2)
print(store)
#
# print(index_i)
# print(index_j)
#
# save_x=min(abs(3-index_i),abs(3-index_j))
# print(save_x)