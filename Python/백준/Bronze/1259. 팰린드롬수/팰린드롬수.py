import sys
input=sys.stdin.readline

while(True):
  data = []
  N = list(input().strip())
  data.append(N[::-1])
  if N[0] == "0":
    break
  if(N == data[0]):
    print("yes")
  else:
    print("no")