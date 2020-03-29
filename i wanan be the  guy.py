n=int(input())
flag=0
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

print(len(arr1))
print(set(len(arr1)))

if len(arr1)!=len(set(arr1)):

    flag=1
    print("Oh, my keyboard!")
if len(arr2)!=len(set(arr2)):
    flag=1
    print("Oh, my keyboard!")

new_arr=arr1+arr2

# print(new_arr)
save=set(new_arr)
if 0 in save:
    save.remove(0)

# print(save)
# print(len(save))
if flag==0:
    if len(save)==n:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")