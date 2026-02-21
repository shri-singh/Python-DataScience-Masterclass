x=[3,3,3,5,5,7,8,9]
unique1=[]
freq_count=[]



for i in x:
    if i==1:
        unique1.append(i)
        freq_count.append(1)
    if i in unique1:
        freq_count[unique1.index(i)] = freq_count[unique1.index(i)]+1
    else:
        unique1.append(i)   
        freq_count.append(1)

print("unique elements in the list are ", unique1)
print("frequency count of the unique elements in the list are ", freq_count)