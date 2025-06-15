#square patttern printing 
'''n=5
for i in range (n):
    for j in range(n):
        print("*",end=" ")  
    print() '''


#increasing triangle pattern

'''n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()'''

#decreasing triange pattern

'''n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()'''

#Right sided triangle

n=5
for i in range(n):
    for j in range(i,n):
        print("",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()


pirnt("hello")