smallest = None 
count = 0
sum = 0
print 'Before'
for value in [1,2.5,3.0,4.0,5.0]:
    count = count + 1.0
    if smallest == None:
        smallest = value
    elif value < smallest:
        smallest = value
    print smallest,value
    sum = sum + value
    
print 'After',smallest,sum/count
