"""
tuples()
    -immutable
    -ordered
    -allow duplicates
    -heterogeneous
    -Fixed size
    -index()
    -count()
    -loop
    -len()
    -slicing
"""

#Tuples

cities = ("Dhaka", "Mirpur", "Savar")
print(cities.index("Dhaka"))
print(cities.count("Dhaka"))
print(len(cities))
print(cities[1:2])

for city in cities:
    print(city)
