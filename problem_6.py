"""Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

sum_of_sqs = []

sums = []

for i in range(0, 101):
	sum_of_sqs.append(i ** 2)
	sums.append(i)
	
print(sum(sum_of_sqs) - (sum(sums) ** 2))
	
	
