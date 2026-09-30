from math import *
tot_sum=0
for n in range(1,51):
    slag=(2**(2*n))/factorial(2*n)*log(n)
    tot_sum=tot_sum+slag
print("итоговая сумма:",tot_sum)