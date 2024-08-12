t = int(input())

for i in range(t):
    data = input()
    count = 0
    while len(data)==0:
        if(data[0] != "("):
            print("NO")
        else:
            if(data[0]=="("):
                count+=1
            else:
                count-=1

    print(count)