x=[3,3,3,5,5,7,8,9]
sorted_x=[]

for i in x:
    if i==1:
        sorted_x.append(i)
    else:
        for j in sorted_x:
            if i<j:
                sorted_x.insert(sorted_x.index(j),i)
                break
        else:
            sorted_x.append(i)
            
print("sorted list is ", sorted_x)

len=len(sorted_x)
if len%2==0:
    median=(sorted_x[len//2]+sorted_x[len//2-1])/2

else:
    median=sorted_x[len//2]

