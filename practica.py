import time 

number1 = int(input())
start = time.time()
sum_number = 0
while number1 != 0:
    sum_number += number1 % 10
    number1 = number1 // 10
print(sum_number)
print(time.time() - start)