import re

# get all the members of re
find_members = []
for member in dir(re):
    if "find" in member:
        help(member)
        find_members.append(member)

print(sorted(find_members))