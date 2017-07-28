def computepay(h,r):
    pay = h*r + (hrs-h)*r*1.5
    return pay

hrs = raw_input("Enter Hours:")
hrs = float(hrs)
if hrs > 40:
    p = computepay(40,10.50)
    print p
else:
    p = hrs*10.5
    print p