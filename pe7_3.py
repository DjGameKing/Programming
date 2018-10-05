import re

def eigenschap(filename):
    file = open(filename, 'r')
    content = file.read()
    file.close()

    num_lines = sum(1 for line in open(filename))
    print('Deze file telt ' + str(num_lines) + ' regels')

    nummer = []

    words = re.split(', |\n', content)
    for elem in words:
        if elem.isdigit():
            nummer.append(elem)

    print('Het grootste kaartnummer is: ' + str(max(nummer)) + ' en dat staat op regel ' + str(nummer.index(max(nummer)) + 1))

eigenschap('kaartnummers.txt')