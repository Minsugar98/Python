import sys
input = sys.stdin.readline

N = int(input().strip())

for i in range(N):
  k = int(input().strip())
  n = int(input().strip())
  people = [i for i in range(1,n+1)]

  for j in range(1,k+1):
    for y in range(1,n):
      people[y] += people[y-1]

  print(people[-1])