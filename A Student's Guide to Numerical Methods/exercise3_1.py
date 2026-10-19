import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 0.15346*x + 0.56614

def resolution(f, N, y0, y1):
    x = np.linspace(0, 1, N)
    h = x[1] - x[0]

    D = np.zeros((N-2, N-2))
    for i in range(N-2):
        D[i, i] = -2
        if(i > 0):
            D[i, i-1] = 1
        if(i < N-3):
            D[i, i+1] = 1
    
    print(f"D matrix: {D}")

    D_inv = np.linalg.inv(D)
    print(f"Inverse of D: {D_inv}")

    y = np.zeros(N-2)
    for i in range(N-2):
        y[i] = f(i) *  h**2
    
    y[0] -= y0
    y[-1] -= y1

    print(f"y vector: {y}")

    y_int = D_inv@y

    y_tot = np.concatenate(([y0], y_int, [y1]))
    
    return x, y_tot

def plot(xy):
    x, res = xy
    plt.plot(x, res, 'o', markersize=3)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('ODE solution with two-points boundary')
    plt.show()

def main():
    N = 44
    y0 = 0.53488
    y1 = 0.71957
    x, y = resolution(f, N, y0, y1)
    plot(resolution(f, N, y0, y1))
    print(f"y = {y}")

if __name__ == "__main__":
    main()
