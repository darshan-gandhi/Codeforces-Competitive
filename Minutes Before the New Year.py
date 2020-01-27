for i in range(int(input())):
    h,m=map(int,input().split())
    hour=23
    minute=60

    hour_min=int(hour-h)*60 + int(minute-m)

    print(hour_min)