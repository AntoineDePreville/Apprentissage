import matplotlib.pyplot as plt
import numpy as np

X = sorted(np.array([0.67085004191557851,
 0.58061004378865544,
 0.58676136374070842,
 0.54829984180149793,
 0.066813005469924303,
 0.72624132677351849]))

Y = np.array([1.1549663619314816,
 1.7532607936413218,
 1.4802793451948357,
 1.7280338083651636,
 0.67311880038766103,
 1.3996565390944993
])


def f(x, y):
    a1, a2, a3, a4, a5, a6, a7 = np.polyfit(x, y, 6)
    g = []
    for i in range(len(x)):
        g.append(a1*x[i]**6 + a2 *x[i]**5 + a3 * x[i]**4 + a4 * x[i]**3 + a5 * x[i]**2 + a6 * x[i]**1 + a7)

    return g

S = np.array([[X[0]**5, X[0]**4, X[0]**3, X[0]**2, X[0]],
              [X[1]**5, X[1]**4, X[1]**3, X[1]**2, X[1]],
              [X[2]**5, X[2]**4, X[2]**3, X[2]**2, X[2]],
              [X[3]**5, X[3]**4, X[3]**3, X[3]**2, X[3]],
              [X[4]**5, X[4]**4, X[4]**3, X[4]**2, X[4]],
              [X[5]**5, X[5]**4, X[5]**3, X[5]**2, X[5]]])

c = np.matmul(np.linalg.pinv(S), Y)
print(c)

xfit = np.linspace(min(X), max(X), 200)
yfit = np.polyval(c, xfit)

plt.scatter(X, Y)
plt.plot(xfit, yfit)
plt.show()
