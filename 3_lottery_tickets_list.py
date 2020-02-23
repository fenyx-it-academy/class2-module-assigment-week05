import random

lotteryTickets = []

for i in range(100):
    lotteryTickets.append(random.randrange(1000000000, 9999999999))

winners = random.sample(lotteryTickets, 2)
print("Lucky 2 lottery tickets are", winners)
