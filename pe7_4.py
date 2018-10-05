import datetime
def voegtoe(date, tijd, naam):
    f = open("hardlopers.txt", "a")
    f.write(date)
    f.write(tijd)
    f.write(naam)

datum = datetime.datetime(2016, 3, 10)
s = datum.strftime("%a %d %b %Y, ")

voegtoe(s, '10:45:52, ', 'Miranda\n')
voegtoe(s, '10:46:06, ', 'Piet\n')
voegtoe(s, '10:47:27, ', 'Sacha\n')
voegtoe(s, '10:48:33, ', 'Karel\n')
voegtoe(s, '10:48:42, ', 'Kemal\n')