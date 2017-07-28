fname = input('Input a file name: ')
if len(fname) == o:
    fname = 'mbox-shout.txt'
fhand = open(fname)
fro line in fhand:
    line = line.rstrp().upper()
    print line