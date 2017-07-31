import shutil
import pandas as pd
import numpy as np
#y_train = pd.read_csv('train_labels.csv')

#y_train = np.array(y_train)

#print(y_train)
#shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

for a in ['dog', 'cat']:
    for x in range(1000):
        x += 1400
        name = a+'.'+str(x)+'.jpg'
        shutil.move('data1/train/'+name, 'data/train/'+a+'/'+name)
        
for a in ['dog', 'cat']:
    for x in range(400):
        x += 1000 + 1400
        name = a+'.'+str(x)+'.jpg'
        shutil.move('data1/train/'+name, 'data/validation/'+a+'/'+name)
