t=int(input())
arr=[]

for i in range(t):
    row=list(map(int,input().split()))
    arr.append(row)
sum_x=0
sum_y=0
sum_z=0
for i in range(t):
    sum_x=sum_x+arr[i][0]
    sum_y = sum_y + arr[i][1]
    sum_z = sum_z + arr[i][2]


if (sum_x==0) and (sum_y==0) and (sum_z==0):
    print("YES")
else:
    print("NO")