n = int(input())
target = 666
count = 0

while True:
  if '666' in str(target):
    count +=1
    if count == n:
      break 
  target+=1

print(target)