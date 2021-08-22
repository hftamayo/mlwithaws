#exercise 11: challenge
#calculate the probability density function of the Gaussian distribution
#https://towardsdatascience.com/exploring-normal-distribution-with-jupyter-notebook-3645ec2d83f8


import math

dataset = [1, 3, 99, 100, 120, 32, 330, 23, 76, 44, 31]
ddof = 0
n = len(dataset)
mean = sum(dataset) / n
variance = sum((x - mean) ** 2 for x in dataset) / (n - ddof)

std_dev = math.sqrt(variance)

x= 0
var = float(std_dev)**2
denom = (2*math.pi*variance)**.5
num = math.exp(-(float(x)-float(mean))**2/(2*var))
print (num/denom)

#return num/denom
