l= list(map(int,input().split(',')))  #to input the elements
k=[]                                  #list for positive numbers of actual list
for i in l:
    if i>0:                           #checking positive numbers in list
        k.append(i)                   #adding positive numbers into new list
print(list(k))                        #output
