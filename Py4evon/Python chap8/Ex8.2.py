fhand = open ('mbox-short.txt')
count = 0
for line in fhand :
    words = line.split()
    if len(words) == 0 : continue
    if words [0] != 'From' : continue
    count = count +1
    try :
        print words[1]
    except:
        print 'No data element at index sub-2'
        continue
print "There were", count, "lines in the file with From as the first word"

