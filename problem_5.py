"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

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
