import random


def two_sum(numbers, target):
	idx = tuple(range(len(numbers)))
		
	while True:
		samples = random.sample(idx, k=2)
	
		if numbers[samples[0]]+numbers[samples[1]] == target:
			return samples


print(two_sum([1, 2, 3], 4))
