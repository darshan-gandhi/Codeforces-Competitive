n,k=map(int,input().split())
arr=list(map(int,input().split()))

for i in range(len(arr)):
    arr[i]=arr[i]+k
    # print(arr[i])

# print(arr)
save=[]
for i in range(len(arr)):
    # print(arr[i])
    if arr[i]<=5:
        save.append(arr[i])
# print(save)


# print(arr)

store=int(len(save)/3)
print(store)