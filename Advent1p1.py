# Advent1 - Part1
# Day 1: The Tyranny of the Rocket Equation
brandstof = 0
bestand = open("Mass.txt","r")
for lijn in bestand:
    massa = int(lijn)
    brandstof = brandstof + int(massa/3)-2
print("Brandstof:",brandstof)