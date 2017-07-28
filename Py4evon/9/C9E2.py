name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)
counts = dict()
for line in text:
    if not line.startswith('From '):continue
    words = line.split()
    word = words [2]
    counts[word] = counts.get(word,0) + 1
	
print counts