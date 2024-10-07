number = input('enter a number less than 25: ')
number = int(float(number))
if number >= 25:
    print('error')
while number <= 25:
    print(number)
    number = number + 1