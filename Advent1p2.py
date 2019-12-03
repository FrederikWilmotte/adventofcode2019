# Advent1 - Part2
# Day 1: The Tyranny of the Rocket Equation
brandstof = 0
bestand = open("Mass.txt","r")
for lijn in bestand:
    massa = int(lijn)
    brandstofmassa = int(massa/3)-2
    while brandstofmassa > 0:
        brandstof = brandstof + brandstofmassa
        brandstofmassa = int(brandstofmassa/3)-2
print("Brandstof:",brandstof)