import sys

t = int(input())
list = []
for i in range(t):
  n = sys.stdin.readline().rstrip()
  if(n!="0"):
    list.append(int(n))
  else:
    list.pop(-1)

print(sum(list))