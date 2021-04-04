# Python implemented trig functions

from math import pi, sqrt, e
from scipy.special import zeta
from numpy.linalg import det
import numpy as np 

def radians(degrees):
	"""Convert angle in degrees to radians."""
	return (degrees/180) * pi

def factorial(n):
	"""Compute n!"""
	return n * factorial(n-1) if n > 1 else 1

def binomial(n, x):
	"""Compute the binomial distribution"""
	return factorial(n)/(factorial(n-x)*factorial(x))

def bernoulli(n):
	return (((-1)**(n-1)*2*factorial(2*n)) / (2*pi)**(2*n)) * zeta(2*n)

def euler(n):
	# return (-1)**n*factorial(2*n) * det(np.array([reversed([1/factorial(2*k) for k in range(i)]) for i in range(2*n)]))
	iterated_sum = 0
	i = complex(0,1)
	for k in range(1, 2*n+1):
		for j in range(k):
			iterated_sum += binomial(k,j)*((-1)**j*(k-2*j)**(2*n+1))/(2**k*i**k*k)
	return iterated_sum

def sin(x):
	"""Maclaurin power series expansion of the sine function."""
	return sum([((-1)**n / factorial(2*n+1)) * x**(2*n+1) for n in range(10)])

def cos(x):
	"""Maclaurin power series expansion of the cosine function."""
	return sum([((-1)**n / factorial(2*n)) * x**(2*n) for n in range(20)])

def tan(x):
	"""Maclaurin power series expansion of the tangent function."""
	return sum([((bernoulli(n)*(-4)**n*(1-4**n)) / factorial(2*n)) * x**(2*n-1) for n in range(20)])

def sec(x):
	"""Maclaurin power series expansion of the secant function."""
	return sum([(((-1)**n*euler(n)) / factorial(2*n)) * x**(2*n) for n in range(20)])

def precise_tan(x):
	"""Trig identity: tan(x) = sin(x)/cos(x)"""
	return sin(x) / cos(x)

def precise_sec(x):
	"""Trig identity: sec(x) = 1/cos(x)"""
	return 1 / cos(x)


if __name__ == '__main__':
	from inspect import cleandoc

	menu = cleandoc("""
		Functions available for testing:
		<0> sin(x)
		<1> cos(x)
		<2> tan(x)
		<3> sec(x)
		<4> arcsin(x)
		<5> arccos(x)
		<6> arctan(x)
		<7> sinh(x)
		<8> cosh(x)
		<9> tanh(x)
		<10> arsinh(x)
		<11> artanh(x)
		-------------------------------
		Enter your choice here: """)
	
	menu_options = {
		'0':('sin(x)', [sin]),
		'1':('cos(x)', [cos]),
		'2':('tan(x)', [tan, precise_tan]),
		'3':('sec(x)', [sec, precise_sec]),
		'4':('arcsin(x)', []),
		'5':('arccos(x)', []),
		'6':('arctan(x)', []),
		'7':('sinh(x)', []),
		'8':('cosh(x)', []),
		'9':('tanh(x)', []),
		'10':('arsinh(x)', []),
		'11':('artanh(x)', [])}

	while True:
		
		menu_prompt = input(menu)
		
		trig_id, trig_function = menu_options[menu_prompt]
		if len(trig_function) == 2:
			sub_menu = cleandoc("""
				<0> {}: based on {}
				<1> {}: based on {}
				{}
				Enter your choice here: """.format(
					trig_function[0].__name__,
					trig_function[0].__doc__,
					trig_function[1].__name__,
					trig_function[1].__doc__,
					'-'*60)
				)
			sub_menu_prompt = input(sub_menu)
			trig_function = trig_function[int(sub_menu_prompt)]
		elif len(trig_function) == 1:
			trig_function = trig_function[0]
		else:
			trig_function = None
			print('Sorry. That function is not supported yet.')

		if trig_function:
			while True:
				print('\nYou working with {}!'.format(trig_id))
				angle_in_degrees = float(input('Enter angle in degrees: '))
				theta = radians(angle_in_degrees)
				print(trig_function(theta))
				exit = input('Continue working with {}? [y/n] '.format(trig_id))
				if exit == 'n':
					break

		restart = input('Would like to restart the script? [y/n] ')
		if restart == 'n':
			break
