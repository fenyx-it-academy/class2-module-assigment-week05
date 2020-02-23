from random import randint, choice # random modülünden sadece randint ve choice içeri aktarılıyor.

tickets = set() #benzersiz olması için küme oluşturduk.
while len(tickets)<100: #100 tane bilet olması için kurulan döngü.
    lottery=randint(1000000000,9999999999) #ilk ve son sayı dahil.
    tickets.add(lottery) #her seçilen kümeye ekelniyor.

tickets=list(tickets) #kümelerde choice yapamadığımız için listeye çevirdik.

winner1 = choice(tickets)
tickets.remove(winner1) #aynı numarayı tekrar seçmemesi için listeden çıkarılıyor.
winner2 = choice(tickets)
print(winner1, winner2)