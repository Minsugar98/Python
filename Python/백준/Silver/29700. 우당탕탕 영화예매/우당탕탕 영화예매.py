import sys
input = sys.stdin.readline
n,m,k = map(int ,input().split())

data = [list(input().rstrip()) for _ in range(n)]

check = 0
for i in range(n):
  cnt = 1
  for j in range(m):
    if data[i][j] == '0':
      if cnt >= k:
        check+=1
      cnt +=1
    else:
      cnt = 1
        
print(check)
