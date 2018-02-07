from collections import defaultdict
def perpali(s):
    a={}
    countodd=1
    a=defaultdict(lambda:0,a)
    for i in s:
        a[i]=a[i]+1
        if a[i]%2==1:
            countodd+=1
        else:
            countodd-=1
    return countodd<=1

print perpali(s="tacoocat")