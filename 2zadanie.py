from math import *
tot_pr=1
for n in range(1,11):
    mnz=(2*n**2+sin(2*n**n)+1)/(n+n**2+2)
    tot_pr=tot_pr*mnz
print("итоговое произведение:",tot_pr)