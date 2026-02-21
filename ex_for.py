list1   =[3,5,5,5,7,9] # this list has 6 elements and the sum of all the elements is 34. So the mean of this list is 34/6 = 5.66
sum=0 
variance1=0 
#count=0
'''
for i in list1:
    sum=sum+i
    for i in list1:
        variance1=variance1+(i-mean_of_list1)**2
'''
# mean_of_list1=sum/len(list1)

# print("mean of list1 is ", mean_of_list1)   
#time Complexity
  O(log n)
  O(n)  # where n is the number of elements in the list. This is because we need to iterate through all the elements of the list once to calculate the sum. 
  O(nlogn)
  O(n^2) # where n is the number of elements in the list. This is because we need to iterate through all the elements of the list once to calculate the sum and then we need to iterate through all the elements of the list again to calculate the mean.
    O(n^3) # where n is the number of elements in the list. This is because we need to iterate through all the elements of the list once to calculate the sum and then we need to iterate through all the elements of the list again to calculate the mean and then we need to iterate through all the elements of the list again to calculate the variance.
# FLOPS stands for Floating Point Operations Per Second. It is a measure of the performance of a computer. It is the number of floating point operations that a computer can perform in one second.
numpy is a library in Python that is used for scientific computing. It provides support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. Numpy is widely used in data science, machine learning, and artificial intelligence for tasks such as data manipulation, numerical analysis, and linear algebra.