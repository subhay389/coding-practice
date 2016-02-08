mylist = ['a','a','a','b','b','c','d','d','a','a','a', 'b']

current = mylist[0]
num = 1

for i in xrange(1, len(mylist)): 
    if mylist[i] == current: 
        num = num + 1
    else: 
        
        print current, num
        
        current = mylist[i]
        num = 1

print current, num        
  
        
    
