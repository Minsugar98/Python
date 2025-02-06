import sys

A = sys.stdin.readline() # 5
K = set(sys.stdin.readline().strip().split(" "))
# K = N.split(" ")
B = sys.stdin.readline() # 5
K_2 = sys.stdin.readline().strip().split(" ")

for i in range(len(K_2)):
  # print(K,K_2[i])
  if K_2[i] not in K:
    print(0)
  else:
    print(1)