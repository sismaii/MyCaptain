import operator
def most_frequent(s):                                                            
    d = {}
    for i in s:
        d[i]=d.get(i,0)+1
    sort_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    print(str(sort_d))
s=str(input("Enter a string: "))
most_frequent(s)
