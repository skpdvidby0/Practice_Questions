def add_all(t):
    total,counter=0,1
    print helper(t,counter,total)


def helper(t,counter,total):
    total = 0
    for i in t:
        if type(i)==list:
            temp=counter
            counter+=1
            total=total+helper(i,counter,total)
            counter=temp
        else:
            total=total+(i*counter)
    f=total
    return total

add_all(t)