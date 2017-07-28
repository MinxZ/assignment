numl = []
while 1:
    num = input('Enter an number: ')
    if num == 'done':break    
    try:num = int(num)
    except:continue
    numl.append(num)
    
average = sum(numl)/len(numl)
print(average,max(numl),min(numl))



