# Requests a number for example: 812 and sum all the digits, returns  8 + 1 + 2 = 11
import time 

number1 = int(input())
start = time.time() # Take tiem
sum_number = 0
while number1 != 0:
    sum_number += number1 % 10
    number1 = number1 // 10
print(sum_number)
print(time.time() - start) # How fast the program ran. 
