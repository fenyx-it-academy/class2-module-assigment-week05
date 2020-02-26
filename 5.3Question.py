import random
ticket_list = []
while len(ticket_list) < 100:
    ticket = random.randint(1000000000, 9999999999)
    if ticket not in ticket_list:
        ticket_list.append(ticket)
ticket1 = ticket_list.pop(random.randrange(len(ticket_list)))
ticket2 = ticket_list.pop(random.randrange(len(ticket_list)))
print('Winning numbers= {}-{}'.format(ticket1, ticket2))
