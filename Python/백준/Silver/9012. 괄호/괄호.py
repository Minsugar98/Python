import sys

N = int(sys.stdin.readline().strip())
for i in range(N):
  data=list(sys.stdin.readline())
  result = 0
  for i in range((len(data))):
    if result == -1:
      break
    else:
      match data[0]:
        case "(":
          data.pop(0)
          result +=1
        case ")":
          data.pop(0)
          result -=1
  if result == 0:
    print("YES")
  else:
    print("NO")
        