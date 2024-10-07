num_1 = input('Input your first number')
num_2 = input('Input your second number')
num_1 = float(num_1)
num_2 = float(num_2)
product = num_1 * num_2
full_product = int(product)
print(full_product)
if full_product > 0 :
    print('This number is positive')
elif full_product < 0 :
    print('This number is negative')
elif full_product == 0 :
    print('This Number is equal to zero')