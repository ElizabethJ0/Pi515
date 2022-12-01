min = 10000
max = -10000
numList = [1,12,8,5,20,80,40,3,6,2000]
#numList=[0,0,0,0]
for x in numList:
 # if(min<x):
    #print (x)
  if (max<x):
    #print(x)
    max = x
  if(min>x):
    #print (x) 
 # elif(min>x):
    #print (x, "This is the smallest so far")
    min = x

print ("This is the min:", min, "and This is the max:", max)
#print (max, "This is the max")