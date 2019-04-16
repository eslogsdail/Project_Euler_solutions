def check_prime(n):
    assert n > 2
    for x in range(2, n):
        if n % x == 0:
            return False
    return True
            
if __name__ == '__main__':
    primes = [2]
    i = 3
    while len(primes) < 10001:
        if check_prime(i):
            primes.append(i)
            print(i)
            i += 2
        else:
            i += 2
    print(primes)
