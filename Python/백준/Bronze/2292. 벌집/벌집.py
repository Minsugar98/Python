import sys
input = sys.stdin.readline

num = int(input().strip())
start = 1 # 벌집
cnt = 1

while num > start:
  start += 6 * cnt
  cnt += 1
print(cnt)