def calc_bmi(weight, height):
	return weight/(height*height)

def calc_bmi_def(weight, height=1.50):
	return weight/(height*height)


def calc_bmi_var(weight,*args):
	print("age is:", args[0])
	return weight/(args[1]*args[1])

# note the usage of format specifiers
print("%.2f" %calc_bmi(50, 1.50))
print("%.2f" %calc_bmi_def(50))
print("%.2f" %calc_bmi_var(50, 25, 1.50))