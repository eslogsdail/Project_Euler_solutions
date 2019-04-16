import math

def get_pfs():
    n = 600851475143 
    while True:
        p = smallest_pf(n)
        if p < n:
            n //= p      
        else:
           return str(n)
           
def smallest_pf(x):
    assert x >= 2
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return i
    return x
        
if __name__ == "__main__":
	print(get_pfs())
