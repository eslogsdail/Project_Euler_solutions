"""sums up all multiples of 3 and 5 between zero 
argument given"""

def sum_multis_5_3(limit):
	summation = 0
	for x in range(0, limit):
		if x % 3 == 0 or x % 5 == 0:
			summation += x
	return str(summation)
	
print(sum_multis_5_3(1000))
