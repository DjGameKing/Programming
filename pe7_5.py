import re

def gemiddelde(zin):
    woorden = re.split(',| ', zin)
    gemid = sum(len(woord) for woord in woorden) / len(woorden)
    print(gemid)

gemiddelde(input(str('Schrijf hier een zin naar keuze: ')))