hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)

if h > 40:
    pay = (h-40)*1.5*r + 40*r
else:
    pay = h*r
print pay    
