largest = None
smallest = None
count = 0
sum = 0
while True:
    num = raw_input("Enter a number: ")
    
    # Handle the edge cases
    if num == "done": break 
    if len(num) < 1 : break # Check for empty line 
    
    # Do the work
    try: 
        num = float(num)
    except:
        print "Invalid input"
        continue
    count = count + 1
    sum = sum + num
    if largest is None:
        largest = num
    elif largest < num:
        largest = num
    if smallest is None:
        smallest = num 
    elif smallest > num:
        smallest = num  
    print num,sum,count      
    
print 'Done'

print "Maximum is", largest
print "Minimum is", smallest
print "Average is", sum/count