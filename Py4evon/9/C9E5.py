name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)
counts = dict()
for line in text:
    if not line.startswith('From '):continue
    words = line.split()
    word = words [1]
    atpos = word.find('@')
    host = word[atpos+1:] 
    #words = word.split('@')
    #addr(counts) = words[1]
    counts[host] = counts.get(host,0) + 1
print counts
