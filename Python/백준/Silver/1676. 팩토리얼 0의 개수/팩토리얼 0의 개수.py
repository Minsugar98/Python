import sys
N = int(sys.stdin.readline())
result = 1
for i in range(1,N+1,1):
  result *= i

data = list(str(result))
count = 0
# print(data)
for i in range(len(data)-1,0,-1):
  # print(i)
  if data[i] == "0":
    count+=1
  else:
    break
print(count)