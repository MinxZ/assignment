largest = None
smallest = None
count = 0
sum = 0
while True:
    num = raw_input("Enter a number: ")
    if num == "done": 
        break
    else:
        try: 
            num = float(num)
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
        except:
            print "Invalid input"

print "Maximum is", largest
print "Minimum is", smallest
print "Average is", sum/count