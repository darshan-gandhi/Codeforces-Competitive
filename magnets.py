arr=[]
count=0
p=""
for i in range(int(input())):
    x=(input())
    if x!=p:
        count+=1
    p=x

print(count)
