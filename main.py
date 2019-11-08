def around(x,y,all):
    all=list(all)



RoomsAndWaals=[]
for q in range(int(input())):
    i=list(input())
    for w in range(len(i)):
        if i[w]==".":i[w]=True
        else:i[w]=False
    RoomsAndWaals.append(i)
#end of input

