def is_isogram(string):

    i=0
    while(i < len(string)-1):

        if(string[i] == string[i+1]):
            x = False
        else:
            x = True
        i +=1
    return x    

print(is_isogram("nadinm"))