fname = input("Enter file name: ")
if len(fname) < 1:
    fname = 'romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    lst_0 = line.split()
    for word in lst_0:
        if not word in lst:
            lst.append(word)
    lst.sort()
print(lst)

