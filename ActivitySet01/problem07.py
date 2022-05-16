[2:47 pm, 16/05/2022] Veg Muzan: def computepay(h, r):
    if h<=40:
        return h*r
    elif h>40:
        h1=h-40
        fee=40*r+h1*r*1.5
        return fee
hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))
p = computepay(hrs, rte)
print("Pay", p)
[2:48 pm, 16/05/2022] Veg Muzan: large=0
small=1111111111111111110
a= None
while True:
    a=input("Enter the number: ")
    if a == 'Done' or a == 'done':
        break
    try:
        if int(a)>0 or int(a) <=0:
            if int(a)>large:
                 large=int(a)
            if int(a)<small:
                 small=int(a)
    except:
        pass    
print("Maximum =",large,"\nMinimum=",small)