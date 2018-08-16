import sys

# prompt messages can be passed as a parameter to the input function
temp_cel = input("Enter temperature in celcius ")

# try except is cleaner way of handling type checks
try:
    # convertion can be stored back to the same variable
    temp_cel = float(temp_cel)
except ValueError:
    print("Cannot convert the input data")
    sys.exit() # terminates the program execution

# type of a variable
print("The type of the converted variable is ", type(temp_cel))

temp_fah = (temp_cel*9/5)+32

# note the difference in both the print statements
# first is passing two arguments and doesnt need convertion
# second is passing a single argument where the float is typecasted before concatentation
print("Temperature in fahrenheit ", temp_fah)
print("Temperature in fahrenheit " + str(temp_fah))

# the above can be achieved without using any variables in a single statement, but is less readable
print("Temperature in celcius = " + str((float(input("Enter temperature in fahrenheit "))-32)*(5/9)))

# different between eval(input()) and input()
# note how same variable can take different input types
sample_input = input("Enter 10: ") # enter 10
print("Type of entered input is ", type(sample_input))
sample_input = eval(input("Enter 10: ")) # enter 10
print("Type of entered input is ", type(sample_input))