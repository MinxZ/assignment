score = raw_input("Enter Score: ")
try:
    s = float(score)
    if s <= 1.0:
        if s >= 0.0:
            if s >= 0.9:
                print "A"
            elif s >= 0.8:
                print "B"
            elif s >= 0.7:
                print "C"
            elif s >= 0.6:
                print "D"
            else:
                print "F"
        else:
            print "< 0"
    else:        
        print "> 1"        
except:
    print "not number"     