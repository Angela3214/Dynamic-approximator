import numpy as np
import scipy.linalg
import matplotlib.pyplot as pt
def f(x): # Наша функция
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
x = np.arange(0, 16, 0.3)
y = f(x)
pt.plot(x, y) # График функции

A = np.array([[1, 1], [15, 1]])
B = np.array([[f(1)], [f(15)]])
X = scipy.linalg.solve(A, B)
pt.plot(x, X[0, 0]*x + X[1, 0])
A = np.array([[1, 1, 1], [1, 8, 64], [1, 15, 225]])
B = np.array([[f(1)], [f(8)], [f(15)]])
X = scipy.linalg.solve(A, B)
pt.plot(x, X[0, 0] + X[1, 0]*x + X[2, 0]*x**2)
A = np.array([[1, 1, 1, 1], [1, 4, 16, 64], [1, 10, 100, 1000], [1, 15, 225, 3375]])
B = np.array([[f(1)], [f(4)], [f(10)], [f(15)]])
X = scipy.linalg.solve(A, B)
pt.plot(x, X[0, 0] + X[1, 0]*x + X[2, 0]*x**2 + X[3, 0]*x**3)
file = open('submission-2.txt', 'w')
file.write(str(X[0, 0]) + ' ' + str(X[1, 0]) + ' ' + str(X[2, 0]) + ' ' + str(X[3, 0]))
file.close()
