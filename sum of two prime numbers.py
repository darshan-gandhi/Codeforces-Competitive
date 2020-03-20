# code
import math

for i in range(int(input())):
    n = int(input())
    for i in range(2, int(n / 2) + 1):
        num1 = i
        num2 = n - i
        x = math.gcd(num1, num2)
        if x == 1:
            print(num1, num2)
            break

