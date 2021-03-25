# Python implemented trig functions

from math import pi, sqrt, e
from scipy.special import zeta

def radians(degrees):
	return (degrees/180) * pi

def factorial(n):
	return n * factorial(n-1) if n > 1 else 1

def bernoulli(n):
	return (((-1)**(n-1)*2*factorial(2*n)) / (2*pi)**(2*n)) * zeta(2*n)

def sin(x):
	"""Maclaurin power series expansion of the sine function."""
	return sum([((-1)**n / factorial(2*n+1)) * x**(2*n+1) for n in range(10)])

def cos(x):
	"""Maclaurin power series expansion of the cosine function."""
	return sum([((-1)**n / factorial(2*n)) * x**(2*n) for n in range(20)])

def tan1(x):
	"""Maclaurin power series expansion of the tangent function."""
	return sum([((bernoulli(n)*(-4)**n*(1-4**n)) / factorial(2*n)) * x**(2*n-1) for n in range(20)])

def tan2(x):
	"""Trig identity."""
	return sin(x) / cos(x)