# print a random card
import random
# getting a random integer
card = random.randint(1,13)
if card == 1:
	card = 'A'
elif card == 11:
	card = 'King'
elif card == 12:
	card = 'Queen'
else:
	card = 'Jack'

suit = ['Hearts', 'Spades', 'Diamond', 'Clubs']
# getting an element from a sequence using choice
print(card, 'of', random.choice(suit))

# more information of all the other avaialble methods
# https://docs.python.org/3.6/library/random.html