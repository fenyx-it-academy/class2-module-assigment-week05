from random import *


ticket_list = []
counter = 0
while counter < 100:
    ticket = randint(1000000000, 9999999999)
    if ticket not in ticket_list:
        ticket_list.append(ticket)
        counter += 1
    else:
        continue
# print(*ticket_list, sep='\n')
# Please uncomment the line above to see the whole 100 ticket numbers.
winner1 = ticket_list.pop(randrange(len(ticket_list)))
winner2 = ticket_list.pop(randrange(len(ticket_list)))
print('The lucky numbers are {}, {}'.format(winner1, winner2))