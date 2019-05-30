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
