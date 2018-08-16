# check if a number is odd or even
num = int(input("Enter a number: "))
if num%2: # note that it is not checked with ==; result of %2 is 0 or 1 which can be translated as False or True
	print("The number is odd")
else:
	print("The number is even")