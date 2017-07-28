data = '78@qq.com '
atpos = data.find('@')
sppos = data.find(' ',atpos)
host = data[atpos+1:sppos]
print(host)