for i in range(int(input())):
    m,n=map(int,input().split())
    arr=list(map(int,input().split()))
    p=list(map(int,input().split()))

    for j in range(len(p)):
       while (True):
            if (arr[p[j]-1]>=arr[p[j+1]-1]):
                print(arr)
                arr[p[j]-1],arr[p[j+1]-1]=arr[p[j+1]-1],arr[p[j]-1]
                print(arr)
            else:
                print("NO")
                break
    print(arr)
    if sorted(arr)==arr:
        print("YES")