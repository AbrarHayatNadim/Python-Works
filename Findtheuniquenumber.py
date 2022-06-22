from collections import Counter
def find_uniq(arr):

     for k,v in Counter(arr).items():

        if v == 1:
            return k

print(find_uniq([2,3,1,1,3333333,3333333,1,1,1,2,1,1,1,1,1]))


