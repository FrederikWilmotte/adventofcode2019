# Advent8 - Part1
# Day 8: Space Image Format

bestand = open("Day8image.txt","r")

def layers(image,layerNr,wide,tall):
    laatste = "nee"

    startlayer = (layerNr-1) * wide * tall
    stoplayer = layerNr * wide * tall

    if stoplayer + 1 > len(image):
        laatste = "ja"

    layer = image[startlayer:stoplayer]

    aantalNul = layer.count('0')
    aantalEen = layer.count('1')
    aantalTwee = layer.count('2')
    checksum = aantalEen * aantalTwee

    return (aantalNul,checksum,laatste)

for imageinput in bestand:
    image = imageinput

layerNr = 1
(aantalNul,checksum,laatste) = layers(image,layerNr,25,6)
minsteNul = aantalNul
gezochtChecksum = checksum
while laatste == "nee":
    layerNr = layerNr + 1
    (aantalNul,checksum,laatste) = layers(image,layerNr,25,6)
    if aantalNul < minsteNul:
        minsteNul = aantalNul
        gezochteChecksum = checksum

print('Checksum',gezochteChecksum)