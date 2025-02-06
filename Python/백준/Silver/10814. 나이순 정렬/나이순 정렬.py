import sys
N = sys.stdin.readline().strip()
info = []
for i in range(int(N)):
  info.append(sys.stdin.readline().split())
info.sort(key=lambda x:int(x[0]))
for text in info:
  print(text[0], text[1])