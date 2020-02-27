t=int(input())

for i in range(t):
    noofdigits=int(input())
    actual_num=input()
    arr=list(actual_num)
    arr=list(map(int,arr))
    store_sum=0
    for i in arr:
        store_sum+=i
    print(store_sum)

    if int(actual_num)%2!=0 and store_sum%2==0:
        print(actual_num)
    else:
        new_store=0
        for i in range(len(arr)):
            new_store+=arr[i]
            if new_store%2==0:
                save=arr[:i+1]
                # print(save)

    # save=[0,0,0,0,0,1,2,3]

    while(True):
        if save[0]==0:
            save.remove(0)

        if save[0]!=0:
            break

    print(save)

    break