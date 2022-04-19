# Karatsuba's algorithm for multiplying large integers
def karatsuba(number_1, number_2):
    """
    The idea is to break each number into 2 parts
    and use a formula to multiply the halves.
    Master Theorem will prove that's faster
    We shall assume that both numbers input have
    length n divisible by 2
    """
    n = len(str(number_1)) 
    if n == 1:
        return number_1 * number_2
    else:
        # 2 halves of the first number
        w = number_1 // 10**(n//2)
        x = number_1 - (w * (10**(n//2)))
        # 2 halves of the second number
        y = number_2 // 10**(n//2)
        z = number_2 - (y * (10**(n//2)))
        print("w:", w)
        print("x:", x)
        print("y:", y)
        print("z:", z)
        # recursive calls
        wy = karatsuba(w,y)
        wz = karatsuba(w,z)
        xy = karatsuba(x,y)
        xz = karatsuba(x,z)
        return wy*(10**n) + (wz + xy)*(10**(n//2)) + xz