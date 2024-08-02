# 상수

# T = int(input())

# for i in range(T):
a , b = input().split()
a = a[::-1]
b = b[::-1]
if a > b:
    print(a)
else:
    print(b)