#문자열 반복

T = int(input())



for i in range(T):
    a, b = input().split()
    for j in range(len(b)):
        print(int(a)*b[j], end="")
    print()
        