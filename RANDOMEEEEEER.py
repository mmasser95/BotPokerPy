t = []
p = [True, True, True]
h = input()
numofc = input()
c = []
counter=0
for i in range(0,h):
    t.append()
for j in range(0,numofc):
    c = raw_input().split(" ")
    if c[1]=="L":
        t[int(c[0])][0] = False
    elif c[1]=="M":
        t[int(c[0])][1] = False
    else:
        t[int(c[0])][2] = False
    counter += 1
    if t[int(c[0])]==[True,False,False] or t[int(c[0])]==[False,False,True] or t[int(c[0])]==[False,False,False]:
        print (counter)
        break
print counter
