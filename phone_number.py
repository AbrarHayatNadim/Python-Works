def create_phone_number(n):
    i = 0
    while(i<len(n)):
        
        x  = '('+str(n[0])+str(n[1])+str(n[2])+")"+" "+str(n[3])+str(n[4])+str(n[5])+"-"+str(n[6])+str(n[7])+str(n[8])+str(n[9])+''
        
        i = i+1
    return(x)  
    
n = [1,2,3,4,5,6,7,8,9,0]
print(create_phone_number(n))