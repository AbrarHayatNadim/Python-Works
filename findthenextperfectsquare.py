import math

def find_next_square(sq):
    c = int(math.sqrt(sq))


    if(c*c == sq):
        
        y = c+1
        z = y*y
        return z    
    else:
        return -1
    

print(find_next_square(16))