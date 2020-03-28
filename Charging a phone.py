# def chargingSmartPhone(initCharge, finalCharge):
#     count = 0
#     c = initCharge
class RangeDict(dict):
    def __getitem__(self, item):
        if type(item) != range: # or xrange in Python 2
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)
arr=[]
stealth_check = RangeDict({range(0,11): 10, range(11,231): 5, range(231,560):8, range(560,1010):2,range(1010,5001):7,range(5001,10001):8,range(100001,pow(10,9)+1):3})
for _ in range(int(input())):8,
    initCharge, finalCharge = map(int, input().split())
    stealth_r =initCharge
    count=0
    while(True):


        stealth_r+=stealth_check[stealth_r]
        # print(stealth_r)
        count+=1
        if stealth_r>=finalCharge:
            break
    arr.append(count)
# print("hi")
for i in arr:
    print(i,end="\n")

#     while (True):
#         # ranges
#
#         if 0 <= c <= 10:
#             r = 10
#         elif 11 <= c <= 230:
#             r = 5
#         elif 231 <= c <= 559:
#             r = 8
#         elif 560 <= c <= 1009:
#             r = 2
#         elif 1010 <= c <= 5000:
#             r = 7
#         elif 5001 <= c <= 10000:
#             r = 8
#         else:
#             r = 3
#
#         c = c + r
#         # print(c)
#         count += 1
#         if c >= finalCharge:
#             break
#     # print(count)
#
#     return count
#
#
# T = int(input())
# for _ in range(T):
#     initCharge, finalCharge = map(int, input().split())
#
#     out_ = chargingSmartPhone(initCharge, finalCharge)
#     print(out_)