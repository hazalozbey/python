#kökler toplamı ve kökleri bulma
from math import *
import cmath 
a=int(input("a sayısını giriniz:"))
b=int(input("b sayısını giriniz:"))
c=int(input("c sayısını bulunuz:"))
delta=(b**2-(4*a*c))
print(delta)
x1=((-b+(sqrt(delta)))/(2*a))
x2 =((-b-(sqrt(delta)))/(2*a))
print("birinci kök: {} \n ikinci kök :{}".format(x1,x2))