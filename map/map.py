from pprint import pprint
import itertools


sizes   = ['small', 'medium', 'large']
colors  = ['lavander','teal', 'burnt orange']
animals = ['koala', 'platypus', 'salamander']

def combine(quantity, size, color, animal):
    return f"{quantity} {size} {color} {animal}"

lst = list(map(combine, itertools.count(), sizes, colors, animals))
for item in lst:
    print (item)

