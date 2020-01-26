ans=[]
for i in range(int(input())):
    newstr=[]
    value=input()
    if len(value)>10:
        arr=list(value)
        newstr.append(arr[0])
    # newstr="".join(arr[0])
        x=len(arr[1:-1])

        newstr.append(str(x))
        newstr.append(arr[-1])

        ansvalue="".join(newstr)
        ans.append((ansvalue))
    else:
        ans.append(value)

    # print(ansvalue)


for i in ans:
    print(i,end='\n')