import sys
import math
input = sys.stdin.readline

N, M = map(int,input().strip().split())

print(math.gcd(N,M))
print(math.lcm(N,M))