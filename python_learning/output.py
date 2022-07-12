year = 2026
event = "world cup"
f'Results of {year} was {event}'
#string format
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
# another string format
import math
print(f'The value of pi is approximately {math.pi:.3f}.')

#formatted string literals

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
     print(f'{name:10} ==> {phone:10d}')
     
    #using the !s and !r
     animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals!r}.')
