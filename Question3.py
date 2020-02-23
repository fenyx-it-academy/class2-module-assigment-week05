import random

lottery_tickets = []  # We define a list to record 100 random ticket numbers.
winning_numbers = []  # We define a list to record two winning numbers.


def lottery():
    while len(set(lottery_tickets)) < 101:  # We use a while loop with a set to generate 100 unique 10 digit numbers.
        number = random.randint(1000000000, 9999999999)  # We use randint function to generate 10 digit numbers.
        lottery_tickets.append(number)  # We add them to our list.
        if len(set(lottery_tickets)) == 100:  # If we get 100 numbers, we break the loop.
            break

    while len(set(winning_numbers)) < 3:  # We use a while loop to pick 2 unique numbers from the ticket list.
        winning_numbers.append(random.choice(lottery_tickets))  # We use choice function to pick up winning numbers.
        if len(set(winning_numbers)) == 2:  # As we get two numbers, we execute and end the function.
            return winning_numbers


print(f'The lucky numbers are {lottery()}')  # We print the winning numbers.
