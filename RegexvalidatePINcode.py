

import re
#def issequence(num):
#    if (str(num) in '1234567890') or (str(num) in '0987654321'): 
#        return True
#    else:
#        return False  




def validate_pin(pin):
    if re.match('^([0-9]{4}|[0-9]{6})$',pin)  :return True
    else: return False
    

print(validate_pin("1234")) 


    