import sys
import math
input = sys.stdin.readline

N = int(input())

data = list(map(int,(input().strip().split())))

T, P = map(int,(input().split()))
cnt = 0

for i in range(len(data)):
  if data[i] != 0:
    cnt += math.ceil(data[i]/T)
  else:
    continue
print(cnt)

R_result = math.floor(N/P)
print(R_result,N-(P*R_result))