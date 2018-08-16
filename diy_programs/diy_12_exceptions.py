try:
	print(1/1) # change it to 1/0 and change the difference
except ZeroDivisionError:
	print("divide by 0 exception")
else:
	print("no exception occurred")
finally:
	print("bye!!!!bye!!!")
