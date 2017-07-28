fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print index,letter
    index = index + 1    
for letter in fruit:
    print letter

    
count = 0    
for letter in fruit:
    if letter == 'n':
        count = count + 1
print count

# slicing
s = 'Monty Python'
print s[0:4]
# up to but not including
print s[0:12]
# =
print s[0:13]
print s[:4]
print s[:]


a = 'Hello'
b = 'World'
c = a + b
print c


if 'n' in fruit:
    print 'True'
    
word = 'cananabanana'
word < fruit
 
f = 'Five'
f = f.lower()
F = f.upper()
print F

pos = fruit.find('na')
print pos


NA = fruit.replace('na','NA')


# lstrip retrip strip


ifB = fruit.startwith('B')
