name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if not line.startswith('From '):continue
    words = line.split()
    time = words[5]
    time = time.split(':')
    hour = time[0]
    counts[hour] = counts.get(hour,0) + 1
    
    
lst = sorted([(k,v) for (k,v) in counts.items() ])
    
#lst = list()
#for k,v in counts.items():
#	lst.append((k,v))
#lst.sort()

for k,v in lst:
	print k, v 