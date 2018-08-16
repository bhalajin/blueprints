import math

class Error(Exception):
	pass

class ZeroError(Error):
	pass

def compute_sqrt(number):
	try:
		number = float(number)
		if number == 0:
			raise ZeroError
	except ValueError:
		print("Enter only float!!!")
	except ZeroError:
		print("Enter number greater than 0!!!")
	else:
		return math.sqrt(number)

print(compute_sqrt(0))
print(compute_sqrt(1))
print(compute_sqrt('a'))