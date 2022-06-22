
def get_sum(num1, num2):
    sum = 0
    if num2 > num1:
        for i in range(num1, num2+1):
            sum += i
    elif num1 > num2:
        for i in range(num2, num1+1):
            sum += i
    else: sum = num1
    return sum



print(get_sum(-10, -10))




