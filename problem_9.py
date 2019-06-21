from itertools import combinations

nums = []

for i in range(10, 600):
	nums.append(i)
	
combs = combinations(nums, 3)
combs_1000 = []

for x in combs:
	if x[0] + x[1] + x[2] == 1000:
		combs_1000.append(x)
		print(x)
		
for y in combs_1000:
	if (y[0] ** 2) + (y[1] ** 2) == (y[2] ** 2):
		print("The special one " + str(y))
		
