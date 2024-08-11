import sys
t = input()
list = []
for i in range(int(t)):
  n = sys.stdin.readline().rstrip().split()
  if(n[0] == "1"):
    list.append(n[-1])
  elif(n[0] == "2"):
    if(len(list) == 0):
      print("-1")
    else:
      print(list.pop(-1))
  elif(n[0] == "3"):
    print(len(list))
  elif(n[0] == "4"):
    if(len(list) == 0):
      print(1)
    else:
      print(0)
  
  elif(n[0] == "5"):
    if(len(list) == 0):
      print("-1")
    else:
      print(list[-1])
  else:
    print("error")
  
