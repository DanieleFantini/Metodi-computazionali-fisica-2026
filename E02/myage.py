from datetime import datetime, timedelta
datenow = datetime.now()
mydate_str = input('Inserisci la tua data di nascita scrivendo (g-m-y): ')
mydate = datetime.strptime(mydate_str, "%d-%m-%Y")
print('date:', mydate)
timediff = datenow - mydate
totd = timediff.days
tots = timediff.total_seconds()
toty = datenow.year - mydate.year
d = {'anni':toty, 'giorni':totd, 'secondi':tots}
for i in d:
    print('{: ^10} {:.2f}'.format(i, d[i]))