fhand = open ('mbox-short.txt')
count = 0
for line in fhand :
    if line.startswith("From "):
        count = count +1
        lst = line
        lst = lst.split()
        words = lst[1]
        print words
    
print "There were", count, "lines in the file with From as the first word"

