# print the number of the day in a week
days_of_week = {"mon":"first", "tue":"second", "wed":"third", "thr":"fourth", "fri":"fifth", "sat":"sixth", "sun": "seventh"}
# note that by having the keys in a single format and by converting the user input to the same format makes the user input handling easier
# remember that users can enter any input in any way possible
day = input("Enter the day of the week: ").lower()

# check if key is available in the dictionary
if day in days_of_week:
	print(days_of_week[day], "day of the week") # note that when print is used with multiple args, space is available by default
else:
	print("invald user input")