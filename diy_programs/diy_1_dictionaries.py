phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook
phonebook["Jake"] = 938273443
del phonebook["Jill"]

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

# Iterating over dictionaries
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Converting a list to a dictionary
sample_list = ['a', 'b', 'c', 'd', 'e']
print(dict(zip(sample_list[::2], sample_list[1::2])))