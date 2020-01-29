arr=[]
for i in range(int(input())):
    x=input().lower()
    arr.append(x)

# print(arr)
d={'tetrahedron':4,'cube':6, 'octahedron':8,'dodecahedron':12,'icosahedron':20 }
save=[]
sum1=0
for i in arr:
    sum1=sum1+d[i]
    # print(sum1)

print(sum1)
