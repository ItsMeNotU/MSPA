
# coding: utf-8

# #MSPA PREDICT 400

# ##Discussion Topic: Week 2 Linear Equations and the Echelon or Gauss-Jordan Methods

# ###Introduction

# This document presents the results of the second weeks discussion topic for the Masters of Science in Predictive Analytics course: PREDICT 400. This assessment required the student to present a system of equations that contains two or more linear equations, and to solve the equations using both the Echelon or Gauss-Jordan methods.

# ###System of Equations

# For this assessment, I generated my own system of equations based on a structural model of supply-demand relationships found within the Western Australian Tourism Accommodation Industry. Relationships were estimated using a Two-Stage Least Squares (TSLS) approach, with endogenous factors being solved simultaneously based on log-level quarterly data.
# 
# Final model specification:
# 
# $Qd=Qs-P$
# 
# $Qs=Qd+P$
# 
# $P=Qd-Qs$
# 
# where:
# 
# $Qd/x$: Total room nights occupied
# 
# $Qs/y$: Total room nights available
# 
# $P/z$: Revenue per average room night
# 
# I will omit further detail of the estimation as the origin of the system of equations is not intended to be the focus of this assessment.

# ###Echelon Method

# Three given equations are given in their proper form below:

# $x-y+\frac{29}{100}z=\frac{-169}{100}\quad(1)$
# 
# $\frac{-17}{20}x+y+\frac{-1}{5}z=\frac{243}{100}\quad(2)$
# 
# $\frac{-47}{20}x+\frac{119}{100}y+z=\frac{-161}{50}\quad(3)$

# The augmented matrix of the linear system:

# In[1]:

import numpy as np

matrix = np.asarray([
    [1, -1, 29/100, -169/100],
    [-17/20, 1, -1/5, 243/100],
    [-47/20, 119/100, 1, -161/50]
], dtype=np.float32)

print(matrix)


# $\left[\begin{array}{rrr|r}
# 1 & -1 & \frac{29}{100} & \frac{-169}{100} \\ 
# \frac{-17}{200} & 1 & \frac{-1}{5} & \frac{243}{100} \\
# \frac{-47}{20} & \frac{119}{100} & 1 & \frac{-161}{50}
# \end{array}\right]$

# $STEP \: 1: \frac{17}{20} R1 + R2 \rightarrow R2:$

# In[2]:

matrix[1] += (matrix[0] * 17/20)

print(matrix)


# $\left[\begin{array}{rrr|r}
# 1 & -1 & \frac{29}{100} & \frac{-169}{100} \\ 
# 0 & \frac{3}{20} & \frac{93}{2000} & \frac{1987}{2000} \\
# \frac{-47}{20} & \frac{119}{100} & 1 & \frac{-161}{50}
# \end{array}\right]$

# $STEP \: 2: \frac{47}{20} R1 + R3 \rightarrow R3:$

# In[3]:

matrix[2] += (matrix[0] * 47/20)

matrix


# $\left[\begin{array}{rrr|r}
# 1 & -1 & \frac{29}{100} & \frac{-169}{100} \\ 
# 0 & \frac{3}{20} & \frac{93}{2000} & \frac{1987}{2000} \\
# 0 & \frac{-29}{25} & \frac{3363}{2000} & \frac{-14383}{2000}
# \end{array}\right]$

# $STEP \: 3: \frac{116}{15} R2 + R3 \rightarrow R3:$

# In[4]:

matrix[2] += (matrix[1] * 116/15)

matrix


# $\left[\begin{array}{rrr|r}
# 1 & -1 & \frac{29}{100} & \frac{-169}{100} \\ 
# 0 & \frac{3}{20} & \frac{93}{2000} & \frac{1987}{2000} \\
# 0 & 0 & \frac{20411}{10000} & \frac{14747}{30000}
# \end{array}\right]$

# The matrix has been transformed into its row-echelon form. The converted equations are given in their proper form below:

# $x-y+\frac{29}{100}z=\frac{-169}{100}\quad(4)$
# 
# $\frac{3}{20}y+\frac{93}{2000}z=\frac{1987}{2000}\quad(5)$
# 
# $\frac{20411}{10000}z=\frac{14747}{30000}\quad(6)$

# $STEP \: 4: Solve \: for \: z:$

# $x-y+\frac{29}{100}z=\frac{-169}{100}\quad(4)$
# 
# $\frac{3}{20}y+\frac{93}{2000}z=\frac{1987}{2000}\quad(5)$
# 
# $z=\frac{14747}{61233}$

# $STEP \: 5: Substitute \: z \: and \: solve \: for \: y:$

# $x-y+\frac{29}{100}z=\frac{-169}{100}\quad(4)$
# 
# $y=\frac{133665}{20411}$
# 
# $z=\frac{14747}{61233}$

# $STEP \: 6: Substitute \: y \: and \: solve \: for \: x:$

# $x=\frac{1466173}{306165}$
# 
# $y=\frac{133665}{20411}$
# 
# $z=\frac{14747}{61233}$

# ###The Gauss-Jordan Method

# Three given equations are given in their proper form below:

# $x-y+\frac{29}{100}z=\frac{-169}{100}\quad(1)$
# 
# $\frac{-17}{20}x+y+\frac{-1}{5}z=\frac{243}{100}\quad(2)$
# 
# $\frac{-47}{20}x+\frac{119}{100}y+z=\frac{-161}{50}\quad(3)$

# The augmented matrix of the linear system:

# In[5]:

import numpy as np

matrix = np.asarray([
    [1, -1, 29/100, -169/100],
    [-17/20, 1, -1/5, 243/100],
    [-47/20, 119/100, 1, -161/50]
], dtype=np.float32)

print(matrix)


# $\left[\begin{array}{rrr|r}
# 1 & -1 & \frac{29}{100} & \frac{-169}{100} \\ 
# \frac{-17}{200} & 1 & \frac{-1}{5} & \frac{243}{100} \\
# \frac{-47}{20} & \frac{119}{100} & 1 & \frac{-161}{50}
# \end{array}\right]$

# $STEP 1: \frac{17}{20} R1 + R2 \rightarrow R2:$

# In[6]:

matrix[1] += (matrix[0] * 17/20)

print(matrix)


# $\left[\begin{array}{rrr|r}
# 1 & -1 & \frac{29}{100} & \frac{-169}{100} \\ 
# 0 & \frac{3}{20} & \frac{93}{2000} & \frac{1987}{2000} \\
# \frac{-47}{20} & \frac{119}{100} & 1 & \frac{-161}{50}
# \end{array}\right]$

# $STEP 2: \frac{47}{20} R1 + R3 \rightarrow R3:$

# In[7]:

matrix[2] += (matrix[0] * 47/20)

matrix


# $\left[\begin{array}{rrr|r}
# 1 & -1 & \frac{29}{100} & \frac{-169}{100} \\ 
# 0 & \frac{3}{20} & \frac{93}{2000} & \frac{1987}{2000} \\
# 0 & \frac{-29}{25} & \frac{3363}{2000} & \frac{-14383}{2000}
# \end{array}\right]$

# $STEP 3: \frac{20}{3} R2 \rightarrow R2:$

# In[8]:

matrix[1] = (matrix[1] * 20/3)

matrix


# $\left[\begin{array}{rrr|r}
# 1 & -1 & \frac{29}{100} & \frac{-169}{100} \\ 
# 0 & 1 & \frac{31}{100} & \frac{1987}{300} \\
# 0 & \frac{-29}{25} & \frac{3363}{2000} & \frac{-14383}{2000}
# \end{array}\right]$

# $STEP 4: R2 + R1 \rightarrow R1:$

# In[9]:

matrix[0] += matrix[1]

print(matrix)


# $\left[\begin{array}{rrr|r}
# 1 & 0 & \frac{3}{5} & \frac{74}{15} \\ 
# 0 & 1 & \frac{31}{100} & \frac{1987}{300} \\
# 0 & \frac{-29}{25} & \frac{3363}{2000} & \frac{-14383}{2000}
# \end{array}\right]$

# $STEP 5: \frac{29}{25} R2 + R3 \rightarrow R3:$

# In[10]:

matrix[2] += (matrix[1] * 29/25)

print(matrix)


# $\left[\begin{array}{rrr|r}
# 1 & 0 & \frac{3}{5} & \frac{74}{15} \\ 
# 0 & 1 & \frac{31}{100} & \frac{1987}{300} \\
# 0 & 0 & \frac{20411}{10000} & \frac{14747}{30000}
# \end{array}\right]$

# $STEP 6: \frac{10000}{20411} R3 \rightarrow R3:$

# In[11]:

matrix[2] = (matrix[2] * 10000/20411)

print(matrix)


# $\left[\begin{array}{rrr|r}
# 1 & 0 & \frac{3}{5} & \frac{74}{15} \\ 
# 0 & 1 & \frac{31}{100} & \frac{1987}{300} \\
# 0 & 0 & 1 & \frac{14747}{61233}
# \end{array}\right]$

# $STEP 7: \frac{-3}{5} R3 + R1 \rightarrow R1:$

# In[12]:

matrix[0] += (matrix[2] * -3/5)

print(matrix)


# $\left[\begin{array}{rrr|r}
# 1 & 0 & 0 & \frac{1466173}{306165} \\ 
# 0 & 1 & \frac{31}{100} & \frac{1987}{300} \\
# 0 & 0 & 1 & \frac{14747}{61233}
# \end{array}\right]$

# $STEP 8: \frac{-31}{100} R3 + R2 \rightarrow R2:$

# In[13]:

matrix[1] += (matrix[2] * -31/100)

print(matrix)


# $\left[\begin{array}{rrr|r}
# 1 & 0 & 0 & \frac{1466173}{306165} \\ 
# 0 & 1 & 0 & \frac{133665}{20411} \\
# 0 & 0 & 1 & \frac{14747}{61233}
# \end{array}\right]$

# The matrix has been transformed into its reduced row-echelon form. The linear system associated with the final augmented matrix is:

# In[14]:

import numpy as np

x = matrix[0,3]
y = matrix[1,3]
z = matrix[2,3]

sys = np.asarray([[x],[y],[z]], dtype=np.float32)
print(sys)


# ###Conclusion

# The Gauss-Jordan Method carries the benefit of not requiring back substitution and its process also produces the invert of the original matrix, which may be of benefit to particular users. Ultimately, my preference of method would depend on whichever is more computationally efficient.
