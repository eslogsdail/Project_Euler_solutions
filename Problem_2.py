"""Sums up even fibbonacci numbers less than 4,000,000"""

fib_sum = 0
fib_nums = [1, 2]

while max(fib_nums) < 4000000:
	x = len(fib_nums)
	next_term = fib_nums[x - 1] + fib_nums[x - 2]
	fib_nums.append(next_term)

for x in fib_nums:
	if x > 4000000:
		fib_nums.remove(x)
		
	
for x in fib_nums:
	if x % 2 ==0:
		fib_sum+= x
		
print(fib_sum)
print(fib_nums)
