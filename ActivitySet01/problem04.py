hrs = float(input("Enter hours "))
if hrs<= 40:
    fee=hrs*1.5
elif hrs>40:
    hrs1=hrs-40
    fee=40*10.5+hrs1*10.5*r
else:
    fee=0
print(fee)