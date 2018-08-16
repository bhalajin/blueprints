for i in range(1,51): # note that the upper limit is exclusive in range function
	if not i%3 and not i%5:
		print('FizzBuzz')
	else:
		if not i%3:
			print('Fizz')
		else:
			if not i%5:
				print('Buzz')
			else:
				print(i)