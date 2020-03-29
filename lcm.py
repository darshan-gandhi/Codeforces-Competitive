# from math import gcd
#
# n=int(input())
# arr=list(map(int,input().split()))
# k=int(input())
# arr.sort()
# lcm = arr[0]
# for i in arr[1:]:
#   lcm = int(lcm*i/gcd(lcm, i))
# # print(lcm)
# store=lcm*k
# save=int(store%(pow(10,9)+7))
# print(save)


import operator
import functools
import math
from math import gcd

from functools import reduce
def find_gcd(arr):
    x = reduce(gcd, arr)
    return x


n=int(input())
arr=list(map(int,input().split()))
k=int(input())
store=find_gcd(arr)
print((store))
save=(functools.reduce(operator.mul,arr, 1))
print(save)
