#!/usr/bin/env python3

a = [2, 8, 9, 48, 8, 22, -12, 2]
b = [num+2 for num in a]
c = [num for num in b if num > 5]

print('original array is:',a)
print('new array array is:',c)