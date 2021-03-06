"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

stuff = []
palindromes = []

def reverse(n):
    rev = ""
    for y in str(n):
        rev = y + rev
    return rev

for x in range(10000, 998002):
    if str(x) == reverse(x):
            palindromes.append(x)
            
for x in palindromes:
    for i in range(100, 1000):
        r = ((x / i) + 0.0)
        if r == int((x / i)) and r < 1000 and r > 99:
            stuff.append(x)

    
print(stuff)
