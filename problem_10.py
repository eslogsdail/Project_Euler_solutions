def check_prime(n):
    assert n > 2
    for x in range(2, n):
        if n % x == 0:
            return False
    return True
    
sum_primes = 2
 
for x in range(3, 2000000, 2):
    if check_prime(x):
        sum_primes += x
        print(x)
         
print(sum_primes)
