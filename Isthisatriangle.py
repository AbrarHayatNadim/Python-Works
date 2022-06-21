def is_triangle(a, b, c):
    if a>0 and b>0 and c>0:
        if (a + b <= c) or (a + c <= b) or (b + c <= a) :
            return False
        return True

print(is_triangle(1, 2, 2))