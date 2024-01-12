#Video 1

import numpy as np

#creating arrays: 
"""
#ndarray : n-dimensional array

myarr = np.array([1,2,3,4,5,6,7,8,9]) --> [1 2 3 4 5 6 7 8 9]
my_ones = np.ones(10)                 --> [1 1 1 1 1 1 1 1 1 1]
myrange = np.arange(0,10)             --> [1 2 3 4 5 6 7 8 9]

#can also create array of strings, although its numerical python and mostly used for numbers

string_array = np.array(["cat","dog","frog"])

#or of Booleans

bool_array = np.array([True, False, True, False, False])

#return slices of arrays:

print(myarr[1:])

print(myarr[-3:])

#sclices with steps :

print(myarr[1:5:2])
print(myarr[::2])

#with 2 dims

new_arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
new_arr *= 2
print(new_arr[0][0])

#sclice from both rows

print(new_arr[0:2,0:2])
"""

#Numpy universal functions
"""
new_arr = ([0,1,2,3,4,5,6,7,8,9])

#square root:

print(np.sqrt(new_arr))

#absolute value --> turns all values into positive values

print(np.absolute(new_arr))

#exponents

print(np.exp(new_arr))

# min / max value

print(np.min(new_arr)) # --> 0
print(np.max(new_arr)) # --> 9

# sign value --> for x in array : returns -1 if x <0 , 0 if x == 0 , 1 if x > 0 

print(np.sign(new_arr))

# Trig sin cos log

print(np.sin(new_arr))
print(np.cos(new_arr))
print(np.log(new_arr))
"""

# all functions are found on numpy.org

# copy vs view
"""
#copy is a copy, a new array made out of the old array
#view is also a copy, but its connected with the old array, NOT A NEW ARRAY

new_arr = np.arange(0,10)

np1 = new_arr.view()

print(f"Original new_arr: {new_arr}")
print(f"Original np1: {np1}")

#change element in new_arr

new_arr[0] = 40

print(f"CHANGED new_arr: {new_arr}")
print(f"Original np1: {np1}")

#np1 got changed by changing new_arr

#do the same thing with copy:

new_arr = np.arange(0,10)

np2 = new_arr.copy()

print(f"Original new_arr: {new_arr}")
print(f"Original np2: {np2}")

#change element in new_arr

new_arr[0] = 40

print(f"CHANGED new_arr: {new_arr}")
print(f"Original np2: {np2}")

#np2 didnt change value by changing new_arr, because its a copy
"""

#Shaping and Reshaping arrays

"""
#create a 1-D array

new_arr = np.arange(1,13)

#find shape

print(new_arr.shape)

#Create a 2-D array amd get shape (rows, columns)

two_d_array = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(two_d_array.shape)

#Reshape 2-D
np3 = new_arr.reshape(3,4)
print(np3)

#the reshaping parameters must multiply to the same number as the parameters of the original array 
# --> original shape: (12), --> new shape: (3,4), or (6,2), 3*4 = 12, 6*2 = 12
# --> original shape: (2,3,4) --> new_shape (6,4) or (12,2) or (24), 2*3*4 = 24, 6*4 = 24, 12*2 = 24

# Reshape 3-D
np4 = new_arr.reshape(2,3,2)
print(np4)
print(np4.shape)

# Flatten to 1-D

np_flat = np4.reshape(-1)
print(np_flat)

# flattening back to 1 dimension is really easy, just put in the parameter -1 
"""

# Iterating through arrays in numpy:

"""
#create an array : ONE-DIMENSIONAL

new_arr = np.arange(1,11)

#simple for-loop

for x in new_arr:
    print(x)
    
#create an array : TWO-DIMENSIONAL

two_d_array = np.array([[1,2,3,4,5],[6,7,8,9,10]])
    
# if we now use a simple for loop, ONLY the first dimension is gonna get looped through, so in this case it loops over the rows

for x in two_d_array:
    #print the rows
    print(x)

#getting inside of the rows:

for row in two_d_array:
    #extract the rows
    for number in row:
        #print each element of the row
        print(number)
        
#create an array : THREE-DIMENSIONAL

three_d_array = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(three_d_array.shape)

#now we see the problem:
#creating a loop for each dimension might be possible when there are only 1 or 2 Dimensions, but lets say we have a 20-D array, then it gets really tricky really fast

#sure, its possible:

for row in three_d_array:
    #extract the rows
    for column in row:
        #extract the column out of the row
        for number in column:
            #extract and print all the elements of the 3rd dimension:
            print(number)

#but its much easier with np.nditer()
# ---> iterates through the deepest dimension

for x in np.nditer(three_d_array):
    print(x)

#works with all dimensions, could be a 50-dimensional array or 1-dimensional array
#short, just ALWAYS use np.nditer() when you want to iterate throguh the deepest dimension
"""

#sorting numpy arrays

"""

new_arr = np.array([1,4,5,6,7,8,2,3]) # --> unordered

#sort them in numerical order from LOW TO HIGH
#np.sort(array)

print(new_arr)              # --> [1 4 5 6 7 8 2 3]
print(np.sort(new_arr))     # --> [1 2 3 4 5 6 7 8]

#sort string array

string_array = np.array(["dog","cat","frog"])
print(string_array)             # --> ['dog' 'cat' 'frog']
print(np.sort(string_array))    # --> ['cat' 'dog' 'frog']

#sorts the array on basis of the letters of the alphabet

#sort Boolean array

bool_array = np.array([True, False, True, False, False])
print(bool_array)           # --> [ True False  True False False]
print(np.sort(bool_array))  # --> [False False False  True  True]

#sorts the False first, and the Trues afterwards ( False -> 0, True -> ) 

#sorting creates a copy not a view

print(new_arr)              # --> [1 4 5 6 7 8 2 3]
print(np.sort(new_arr))     # --> [1 2 3 4 5 6 7 8]
print(new_arr)              # --> [1 4 5 6 7 8 2 3]

#original doesnt get changed

#sorting 2-dimensional arrays

two_d_array = np.array([[1,2,5,4,3],[10,6,9,7,8]]) # -_> unsorted

print(two_d_array)              # --> [[ 1  2  5  4  3] [10  6  9  7  8]]
print(np.sort(two_d_array))     # --> [[ 1  2  3  4  5] [ 6  7  8  9 10]]

#sorting 2d arrays (or higher dimesnions) sorts the deepest dimension according to value
"""

#searching numpy arrays

"""

new_arr = np.arange(1,11)

#search for a specific entry in the array
#where function --> np.where(array + condition)

x = np.where(new_arr == 3) # --> (array([2], dtype= int64),)
print(x)

#returns tuple of index numbers of all indexes of new_arr where new_arr equals 3 and data type
#to get just the index just extract the zeroth item of the tuple

index = x[0] # --> [2]
print(index)

# how about more than one entry?

new_arr = np.array([1,2,3,3,4,5,6,7,8,9,3])
pos_tuple = np.where(new_arr == 3) 
print(pos_tuple[0]) # --> [ 2  3 10]

#returns array of the indexes

#get items of the indexes (all 3s)
print(new_arr[pos_tuple[0]])

#return even items
even_tuple = np.where(new_arr%2 == 0)
print(even_tuple)                       # --> (array([1, 4, 6, 8], dtype=int64),)
print(new_arr[even_tuple[0]])           # --> [2 4 6 8]

#works with any conditional statements
"""

#filtering numpy arrays:

"""

new_arr = np.arange(1,11)

#filter out the first 2 values

#create a list of boolean values of length of the array --> True for all numbers you want to extract, False for all the others

boolean_list = [True, True, False, False, False, False,False, False,False, False] # 2 Trues for value 1 & 2 and 8 False for values 3-10

print(new_arr)                  # --> [ 1 2  3  4  5  6  7  8  9 10]
print(new_arr[boolean_list])    # --> [1 2]

#just pass the list of boolean values as index and numpy filters the array

#this approach works, but is super annoying
# --> 1. you dont want to create a super long list of boolean values
# --> 2. ypu dont want to do this with multiple dimensions

#instead create filtered list

filtered = []
for value in new_arr:
    #insert logic
    if value%2 == 0:        
        filtered.append(True)
    else: 
        filtered.append(False)

#compare filtered and unfiltered array:

print(new_arr)
print(filtered)
new_arr_filtered = new_arr[filtered]
print(new_arr_filtered)

#still a lot of work AND it does not work with multidimensional arrays
#numpy has a shortcut

#create 2-D array
new_arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

#create filter mechanism
filtered = new_arr%2 == 0

print(new_arr[filtered]) # --> [ 2  4  6  8 10]

#the return is a onedimensional array of all the values which passed the logic of filtered
# --> just always use filtered = logic, array[filtered]
#but understand mechanic of how it works
"""