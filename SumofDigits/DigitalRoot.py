def digital_root(n):
    n = str(n)
    sum = 0
    for i in n:
        sum  = sum + int(i)
    if(len(str(sum)) >1):
        return digital_root(sum)      
    return sum

print(digital_root(942))