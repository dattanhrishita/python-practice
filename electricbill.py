# generate electricity bill
units=int(input("eneter the number of units consumed"))

if(units>0 and units<=100):
    cost=units*10
elif(units<=200):
    cost=100*10+(units-100)*15
elif(units<=300):
    cost=100*10+100*15+(units-200)*20
else:
    cost=100*10+100*15+100*20+(units-300)*25
print(f"Total Cost : ₹{cost}")
