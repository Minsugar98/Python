import sys
from collections import deque

N = int(sys.stdin.readline())
q_data =  deque()
def case(K):
  match K[0]:
    case 'push':
      q_data.append(int(K[1]))
      # print(q_data[-1])
    case 'front':
      if len(q_data) == 0:
        print("-1")
      else:
        print(q_data[0])
    case 'back':
      if len(q_data) == 0:
        print("-1")
      else:
        print(q_data[-1])
    case 'size':
      print(len(q_data))
    case 'pop':
      if len(q_data) == 0:
        print("-1")
      else:
        print(q_data.popleft())

    case "empty":
      if len(q_data) == 0:
        print("1")
      else:
        print("0")



for i in range(N):

  T = sys.stdin.readline().split()
  case(T)
  
  