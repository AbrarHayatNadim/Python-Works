def find_short(s):
    x = s.split(" ")
    y =  min(x, key=len)
    return len(y)
        
print(find_short('gitrrrrrrr pushrrrr originrrrr main'))