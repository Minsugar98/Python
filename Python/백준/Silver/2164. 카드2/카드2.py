import sys
from collections import deque
N = int(sys.stdin.readline())
data = deque()
for i in range(N):
  data.append(i+1)
for j in range(len(data)-1):
  data.popleft()
  data.append(data.popleft())
print(data[0])