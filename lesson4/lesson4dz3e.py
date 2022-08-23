def lucky_ticket(ticket_number):
    if (len(str(ticket_number)) != 6) or (type(ticket_number) is not int):
        return 'Неверный номер билета'
    else:
        ticket_number1 = list(str(ticket_number))
        sum1 = int(ticket_number1[0]) + int(ticket_number1[1]) + int(ticket_number1[2])
        sum2 = int(ticket_number1[3]) + int(ticket_number1[4]) + int(ticket_number1[5])
        if sum1 == sum2:
            return 'Билет счастливый'
        else:
            return 'Билет несчастливый'

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(125633))