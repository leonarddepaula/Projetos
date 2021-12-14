import numpy as np
import pandas as pd

# == CODIGO 1 == #
print('\n***Codigo 1***\n')
z = np.zeros((4, ))
print('Z: ',z)

# == CODIGO 2 == #
print('\n***Codigo 2***\n')
z = np.zeros((4, ))
z[1] = 1.
print('Z: ',z)

# == CODIGO 3 == #
print('\n***Codigo 3***\n')
z = np.zeros((4, ))
z[1:] = 1.
print("z: ",z)

# == CODIGO 4 == #
print('\n***Codigo 4***\n')
z = np.zeros((4, ))
z[:3] = 1.
print('z: ',z)

# == CODIGO 5 == #
print('\n***Codigo 5***\n')
#x = np.twos((2, 2)) codigo errado
x = np.ones((2, 2)) + np.ones((2, 2))
xx = 2 * np.ones((2, 2))
xxx = np.array([2.] * 4).reshape(2, 2)
print('x:\n', x)
print('xx:\n', xx)
print('xxx:\n', xxx)

# == CODIGO 6 == #
print('\n***Codigo 6***\n')
x = np.array([[1, 2], [3, 4]])
y = x[0, :]
y[1] = 10
print('X: \n',x) 

# == CODIGO 7 == #
print('\n***Codigo 7***\n')
x = np.array([[1, 3], [11, 10]])
print(np.mean(x[x > np.pi]))

# == CODIGO 8 == #
print('\n***Codigo 8***\n')
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog',
'cat', 'snake', 'cat', 'dog', 'dog'],
'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'priority': ['yes', 'yes', 'no', 'yes', 'no',
            'no', 'no', 'yes','no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# == CODIGO 9 == #
print('\n***Codigo 9***\n')
df = pd.DataFrame(data=data, index=labels)

# == CODIGO 10 == #
print('\n***Codigo 10***\n')
y_true = np.array([1., 2., 1.])
y_pred = np.array([1.1, 1.98, 1.05])