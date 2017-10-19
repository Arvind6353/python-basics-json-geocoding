import numpy as np 

# 1 D array
a1 = np.array([1,2,3,4])

# 2D array
a2 = np.array([ [1,2,3,4] , [3,4,6,7]])

# 3D array
a3 = np.array([  [[1,2,3,4] , [3,4,6,7]] ,
                    [ [1,2,3,4] , [3,4,6,7]],
                    [ [1,2,3,4] , [3,4,6,7]]
              ])

# range - (start , stop , step)
a4 = np.arange(10)

# start - stop, step
a5 = np.arange(10,20,2)

# float point range
a6 = np.arange(0.3,2,0.5)


# start , end , no of divisions in between start and stop
a7 = np.linspace(1,8,12)


# ones 2d matrix ((type of matrix))
a8 = np.ones((2,2))


# zeros 3d matrix ((type of matrix))
a9 = np.zeros((3,3))


# empty matrix - with non intialised values ((type of matrix))
a10 = np.empty((3,3))

# diagonal ones ( row , column) 
a11 = np.eye(2,3)

# matrix with prefilled values  ((type of matrix))
a12 = np.random.random((3,3))

a13 = np.arange(8).reshape(4,2)

print(a13)