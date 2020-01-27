import  math
for i in range(int(input())):
    n,k=map(int,input().split())
    save=math.floor(n/k)
    # print(save)
    save_ans=save*k
    # print(save_ans)
    hello=n-save_ans
    # print(hello)
    extra=0
    if (n-save_ans)!=0 and hello>=math.floor(k/2):

        extra=math.floor(k/2)
        # print(extra)

    final_ans=save_ans+extra
    print(final_ans)



