n,k=map(int,input().split())

arr=list(map(int,input().split()))

count=0
for i in range(len(arr)):
    if arr[i]!=0:
        if i<k:
            count+=1
            # print(arr[i])
            # print(count)
num=arr[k-1]
# print(num)
for i in range(k,len(arr)):
    if num==arr[i] and num!=0:
        # print(arr[i])
        count+=1

print(count)