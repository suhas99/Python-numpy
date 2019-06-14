#numpy is used to faster computation effciently than lists.It aslo can be used to hard maths calculations and multi-dimensional arrays
import numpy as np


#numpy can be given alist as argument (1 dimension array)
l=[0,1,2]
print(l)
a = np.array(l)
print(a*2)


#you can also try using the arange function for contionos allocation with some value
#Functions ndim(),len(), shape() returns the dimension,length and the No of  column and rows of  of the array respectively
#The below function gives shape as(10,) because it is one dimensional

b=np.arange(10)
print(b,b.ndim,b.shape,len(b))


#creating two dimensional and three dimensional array
c=np.array([[1,2,3],[4,5,6]])
print(c,c.ndim,c.shape,len(c))

#creating three dimensional array is similar to that
d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(d,d.ndim,len(d),d.shape)

# 1 dimension array is called vector, 2d array is called matrix and n dimesion array is called Tensors(Hence Tensorflow)

#Types of arrray creation using numpy

#1(Specifing the statrt point,end point and step size
	#It creates the array inclusive of start point and exculsive of end point dividing the entire range and step size gives the gap between numbers
e=np.arange(1,10,2)
print(e)

#2 using linspasce
	#Linspace takes a set of points a linear plane and gives the number of points reguiresd in the specified range by dividing equally.
f=np.linspace(1,5,5)
print(f)

#3 Array with values as 1( n dimensions array can be directly intilaized)
	#Always the value must be in tuples
g=np.ones((3))
print(g)
g=np.ones((3,3))
print(g)
g=np.ones((3,3,3,3))

#4 Array with all the value as 0's:

h=np.zeros((2,2))
print(h)

#5 Iarray:  In this all the diagonal elements are 1
# when given rows and columns manually it will make all the elements coming here as 1 tiil the diagonal ends

i=np.eye(3)
print(i)
i=np.eye(3,2)
print(i)
i=np.eye(3,3) # This similar to the first example and will give the same output
print(i)

#6 Diagonaly arrays : To get and populate array with diagonal elements and rest of the elemnets will be zero

g=np.diag([1,2,3,4])
print(g)
print(np.diag(g))
#for any numpy array get diag elements using np.diag(array name)
k=np.array([[1,2,3],[4,5,6]])
print(k,np.diag(k))


#7 Random values and randn()
h=np.random.rand(4)
print(h)
h=np.random.rand(4)



#Data types in numpy
#int
j=np.arange(10)
print(j.dtype)

#we can specify data type explicitly if we wish to change it explicitly!
#float

j=np.arange(10,dtype='float')
print(j.dtype)

j=np.arange(10.0)
print(j.dtype)

# when we use functions 0's or 1's it will always create the float data type.

j=np.zeros(3)
print(j.dtype)

j=np.ones(3)
print(j.dtype)


#bool
j=np.array([True,False])
print(j.dtype)

#string
j=np.array(['adfgh','bcvb','ccvbn'])
print(j.dtype)

#for detail explanation in data types you can go on to
#https://www.numpy.org/devdocs/user/basics.types.html



# slicing operations on numpy
# we give start, end and step size and we get a sub array of this
k = np.arange(10)
print(k, k[1:5:1])

# We can get value , assign and work with these elements using the ":" and "::" operator

k[5:] = 10
print(k[5:], k)

# Here -1 is the step size backwards[Start:end:-1 is backwarfds]
k1 = np.arange(10, 20, 2)
print(k1)
k[5:] = k1[::-1]
print(k, k[:4:-1], k[4:])

# Copy and Views

# Shallow copy(views) and Deep copy()
#l and l1 both share same memory and shares_memory() can be used to check and it returns a logical vector. and copy() is used to deep copy or force copy.
l=np.arange(10)
l1=l[1:8:2]
l2=l1.copy()
l2
print(l,np.shares_memory(l,l1),np.shares_memory(l1,l2))

#Fancy indexing
l=np.array([10,30,50,60])
print(l,l[[0,2,3]])

l[[0,2,3]]= -10
print(l)



