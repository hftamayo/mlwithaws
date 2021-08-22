#exercise 11: challenge
#calculate the std deviation of the dataset

import math

dataset = [1, 3, 99, 100, 120, 32, 330, 23, 76, 44, 31]
ddof = 0
n = len(dataset)
mean = sum(dataset) / n
variance = sum((x - mean) ** 2 for x in dataset) / (n - ddof)

std_dev = math.sqrt(variance)
print(std_dev)
