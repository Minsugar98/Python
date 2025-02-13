
import sys

input = sys.stdin.readline
N = int(input()) 
data = list(map(int, input().split())) 
cnt = 0

for num in data:
    if num < 2:  # 0이나 1은 소수가 아님
        continue
    is_prime = True
    for j in range(2, int(num ** 0.5) + 1): 
        if num % j == 0:
            is_prime = False
            break
    if is_prime:
        cnt += 1

print(cnt)