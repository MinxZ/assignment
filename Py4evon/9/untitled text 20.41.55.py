counts = dict()
names = ['csev','cwen','csev','zhen','zhen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts) 

counts = dict()
names = ['csev','cwen','csev','zhen','zhen']
for name in names:
    counts[name] = counts.get(name,0) + 1
print (counts) 

counts = dict()
line = input('Enter a line: ')
ll = 'the the is the most common word in this sentence'
ll = line.split()
for name in ll:
    counts[name] = counts.get(name,0) + 1
print ('Counts',counts) 


for key in counts
	print key ,counts[key]
	
print list(counts)
# List of the keys

print counts.keys()
# List of the keys
print counts.values()
#List of the values
print counts.items()
# Tuples 
#In the same order no matter what is the orde



