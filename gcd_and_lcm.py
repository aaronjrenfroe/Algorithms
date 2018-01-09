
# Compute the greatest common divisor of a and b
def gcd(a,b):
    
    while b > 0:
        a, b = b, a % b
    return a


#Compute the lowest common multiple of a and b
def lcm(a, b):
    return a * b / gcd(a, b)