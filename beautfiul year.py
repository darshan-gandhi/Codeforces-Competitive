year=(input())
year_val=list(year)
# print(save_val)
# arr=list(year)
# arr.reverse()
# print(arr)
# i=year+1
i=(int(year)+1)
# i=str(i)
# print(arr)
while(True):
    save_val=list(str(i))
    save=set(save_val)
    if len(save)==len(year_val):
        print("".join(save_val))
        break
    i+=1