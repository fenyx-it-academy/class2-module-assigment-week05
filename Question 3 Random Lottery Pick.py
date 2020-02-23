import random
import time

#numbers=[0,1,2,3,4,5,6,7,8,9]
numbers=list(range(0,10)) # bu sekilde elle teker teker yazilmadan cok kisa istenilen uzunlukta liste olusturulabilir.
lottery_ticket_list =[]
while True:
    print('Do you want to try your chance with ticket?')#oyuncuya soruldu
    answer= input('Yes/Y or No/N) :  ').lower()#cevaba gore oyun baslayack
    if answer == 'n' or answer=='no':
        print('Good Luck')
        break
    elif answer == 'yes' or answer=='y':
        print('Your ticket is creating, please wait')
        time.sleep(3)
        your_ticket = random.sample(numbers, 10)
        print(*your_ticket,'\nnow it is checking')
        time.sleep(5)

        for i in range(3):
            a = random.sample(numbers, k=10)
            lottery_ticket_list.append(a)
            # print(lottery_ticket_list)
        winner_tickets = []
        for i in range(2):
            b = random.choice(lottery_ticket_list)
            winner_tickets.append(b)

        if your_ticket in winner_tickets:
            print('you win congratulations')
        else:
            print('Sorry you can try again')
            print('winner numbers : ')
            print((*winner_tickets[0]),'and',(*winner_tickets[1]))

