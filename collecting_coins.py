# -*- coding: utf-8 -*-
"""collecting_coins.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Io0OLrMw60E6v2o1hYbhJoLI377rJHqG
"""

save=[]
for i in range(int(input())):
  a,b,c,n=input().split()
  a=int(a)
  b=int(b)
  c=int(c)
  n=int(n)

  arr=[a,b,c]

  arr.sort()
  diff1=arr[2]-arr[0]
  if diff1>n:
    # print("NO")
    save.append("NO")
    continue
  diff2=arr[2]-arr[1]
  if diff2>n:
    # print("NO")
    save.append("NO")
    continue
  netdiff=diff1+diff2
  if netdiff>n:
    save.append("NO")
    continue
    # print("NO")

  totalnet=n-netdiff

  if totalnet%3==0:
    # print("YES")
    save.append("YES")
  else:
    # print("NO")
    save.append("NO")


for i in save:
  print(i,end="\n")

""