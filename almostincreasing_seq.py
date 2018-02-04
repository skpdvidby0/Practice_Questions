def first_bad_pair(sequence):
    for i in range(len(sequence)):
        if sequence[i]>sequence[i-1]:
            return True
    return -1
def al(sequence):
    j=first_bad_pair(sequence)
    if j ==-1:

        return True
    if first_bad_pair(sequence[j-1:j]+sequence[j+1:])==-1:
        return True
    if first_bad_pair(sequence[j:j+1]+sequence[j+2:])==-1:
        return True
    return False
print al([10,1,2,3,4,5])
