import sys
input = sys.stdin.readline

N, M = map(int,input().strip().split())
data = list(map(int,input().strip().split()))
max_value = 0
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      if max_value < (data[i]+data[j]+data[k]) and (data[i] + data[j]+data[k]) <= M:
        max_value = data[i] + data[j]+data[k]
    
print(max_value)