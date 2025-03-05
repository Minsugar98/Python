import sys
input = sys.stdin.readline
chess1=[['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
chess2=[['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

N,M = map(int,input().split())
data = []
for i in range(N):
  data.append(list(input().strip()))
min_count = float('inf')
for i in range(N-7):
  for j in range(M-7):
    check1 = 0
    check2 = 0
    for k in range(8):
      for l in range(8):
        # print(chess1[k][l],data[i+k][j+l])
        if chess1[k][l] != data[i+k][j+l]:
          check1 += 1
        if chess2[k][l] != data[i+k][j+l]:
          check2 +=1
    min_count = min(min_count, check1, check2)

    
print(min_count)