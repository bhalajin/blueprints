def fn_modifier(f):
	def _call_():
		print("______________________")
		return f()
	return _call_

@fn_modifier
def func1():
	print("Function 1")

@fn_modifier
def func2():
	print("Function 2")

if __name__ == '__main__':
	func1()
	func2()