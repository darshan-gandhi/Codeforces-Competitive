str1="Tax#!cd.KL"
arr=list(str1)
store=["#","!","."]
j = len(arr) - 1
for i in range(int(len(arr)/2)):


    if arr[i] not in store and arr[j] not in store:
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        j=j-1
    else:
        j=j-1
    print(arr)