
def my_round(number, ndigits):
    number = number * (10 ** ndigits)
    if float(number) - int(number) > 0.5:
         number = number // 1 + 1
    else:
         number = number // 1
    return number / (10 ** ndigits)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))