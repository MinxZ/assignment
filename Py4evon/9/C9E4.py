name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)
counts = dict()
for line in text:
    if not line.startswith('From '):continue
    words = line.split()
    word = words [1]
    counts[word] = counts.get(word,0) + 1
	
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword,bigcount
