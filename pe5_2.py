leeftijd = int(input('Geef je leeftijd: '))
nlID = input('Nederlands paspoort: ')

if leeftijd < 18 or nlID == 'no' or nlID == 'nee' or nlID == 'Nee' or nlID == 'No':
    print('Helaas, u mag niet stemmen!')
else:
    print('Gefeliciteerd, u mag stemmen!')

# Oops, had deze opdracht al gedaan in the vorige