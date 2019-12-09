# Advent8 - Part2
# Day 8: Space Image Format

def printLayer(layer,wide):
    layer = makeLayerReadable(layer)
    startlayer = 0
    stoplayer = wide
    while startlayer + wide <= len(layer):
        print(layer[startlayer:stoplayer])
        startlayer = startlayer + wide
        stoplayer = stoplayer + wide

def makeLayerReadable (layer):
    layerReadable = ""
    for c in layer:
        if c == "1":
            layerReadable = layerReadable + "X"
        elif c == "0":
            layerReadable = layerReadable + " "
        else:
            layerReadable = layerReadable + "."
    return layerReadable

def makeLayer(image,layerNr,wide,tall):
    laatste = "nee"
    startlayer = (layerNr-1) * wide * tall
    stoplayer = layerNr * wide * tall
    if stoplayer + 1 > len(image):
        laatste = "ja"
    layer = image[startlayer:stoplayer]
    return (layer,laatste)

def compareLayer(layerBoven,layerOnder):
    layer = ""
    v = 0
    for c1 in layerBoven:
        c2 = layerOnder[v]
        if c1 == "0" or c1 == "1":
            c3 = c1
        else:
            c3 = c2
        layer = layer + c3
        v = v + 1
    return layer


bestand = open("Day8image.txt","r")
for imageinput in bestand:
    image = imageinput

layerNr = 1
(layer,laatste) = makeLayer(image,layerNr,25,6)
while laatste == "nee":
    layerBoven = layer
    layerNr = layerNr + 1
    (layerOnder,laatste) = makeLayer(image,layerNr,25,6)
    layer = compareLayer(layerBoven,layerOnder)

printLayer(layer,25)