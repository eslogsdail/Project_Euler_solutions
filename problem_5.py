def div_check(n):
    for i in range(10, 21):
        if n % i == 0:
            continue
        else:
            return False
    return True
    
if __name__ == '__main__':
    num = 2520
    while not div_check(num):
        print(num)
        num += 2520
    print(num)
