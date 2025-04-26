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
"""

#Tuples

cities = ("Dhaka", "Mirpur", "Savar")
print(cities.index("Dhaka"))
print(cities.count("Dhaka"))
print(len(cities))

for city in cities:
    print(city)
