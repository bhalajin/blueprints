hist = input("Enter the list of integers (Sep with comma): ")
hist = hist.split(',') # string split function
for entry in hist:
	print('*' * int(entry)) # note the way * is used