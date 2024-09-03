X=int(input("ENTER UNIT CONSUMPTION"))
if X<=50:
    total=X*2.60
    Tax=25
elif X>50 and X<=100:
    total=(50*2.60)+((X-50)*3.25)
    Tax=35
elif X>100 and X<=200:
    total=(50*2.60)+(50*3.25)+((X-100)*5.26)
    Tax=45
else:
    total=(50*2.60)+(50*3.25)+(100*5.26)+((X-200)*8.45)
    Tax=75
Bill=total+Tax
print("YOUR TOTAL BILL IS:",Bill)
