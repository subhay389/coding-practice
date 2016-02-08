mylist = [2,7,9,9,9,9,10,12,22]

mylist.insert(0,-1)
mylist.append(101)

answer = []

for i in xrange(len(mylist)-1): 
    current = mylist[i]
    next = mylist[i+1]
    if next - current > 2: 
        answer.extend([str(current+1)+'-'+str(next-1)])
    elif next - current == 2:
        answer.extend([str(current+1)])

print answer