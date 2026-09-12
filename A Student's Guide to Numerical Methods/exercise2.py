import numpy as np

def euler(omega, dt, steps):
    y = np.zeros(steps+1)
    y[0] = 1
    factor = 1 - omega*dt
    for n in range(steps):
        y[n+1] = factor*y[n]
    
    return y, factor
    
def implicit(omega, dt, steps):
    y = np.zeros(steps+1)
    y[0] = 1
    factor = 1/(1 + omega*dt)
    for n in range(steps):
        y[n+1] = factor*y[n]
    
    return y, factor

def main():
    omega = 1
    t_end = 4/omega

    print("(a)+(b) Erreur fractionnelle a t = 4/omega")

    omega_dt_val = [0.1, 0.01, 1]

    y_exact_final = np.exp(-omega*t_end)

    print(f"y_exact(4/omega) = {y_exact_final:.6f}\n")
    print(f"{'omega*dt':>10} | {'y_euler':>13} | {'err. frac. euler':>16} | "f"{'y_implicit':>13} | {'err. frac. implicit':>16}")


    for omega_dt in omega_dt_val:
        dt = omega_dt/omega
        n_steps = round(t_end/dt)
        
        y_euler = euler(omega, dt, n_steps)
        y_implicit = implicit(omega, dt, n_steps)

        error_euler = (y_euler[-1] - y_exact_final)/y_exact_final
        error_implicit = (y_implicit[-1] - y_exact_final) / y_exact_final
        
        print(f"{omega_dt:10.3f} | {y_euler[-1]:13.6f} | {error_euler:16.6e} | "f"{y_implicit[-1]:13.6f} | {error_implicit:16.6e}")

    n_steps_stab = 50
    
    print(f"\n{'omega*dt':>10} | {'facteur (1-omega*dt)':>22} | {'|y_50|':>12} | {'stable ?':>10}")

    omega_dt_scan = np.arange(0.2, 3.01, 0.2)
    seuil_trouve = None

    for omega_dt in omega_dt_scan:
        dt = omega_dt/omega
        y, factor = euler(omega, dt, n_steps_stab)
        stable = abs(y[-1]) < abs(y[0])
        print(f"{omega_dt:10.2f} | {factor:22.4f} | {abs(y[-1]):12.4e} | {'oui' if stable else 'NON':>10}")
        if not stable and seuil_trouve is None:
            seuil_trouve = omega_dt
        
    print(f"\n--> Le schema explicite devient instable pour omega*dt >= ~{seuil_trouve:.2f}")
    print("    (theorie : |1 - omega*dt| > 1  <=>  omega*dt > 2)\n")
 
    print("Affinage autour de omega*dt = 2 :")

    for omega_dt in [1.9, 1.99, 2.0, 2.01, 2.1]:
        dt = omega_dt / omega
        y, factor = euler(omega, dt, n_steps_stab)
        print(f"  omega*dt = {omega_dt:5.2f}  ->  facteur = {factor:7.4f}  ->  "
            f"|y_{n_steps_stab}| = {abs(y[-1]):.4e}")
    
    print(f"\n{'omega*dt':>12} | {'facteur 1/(1+omega*dt)':>24} | {'|y_50|':>14} | {'stable ?':>10}")

    omega_dt_grands = [0.5, 1.0, 2.0, 5.0, 10.0, 100.0, 1000.0, 1e6]

    for omega_dt in omega_dt_grands:
        dt = omega_dt / omega
        y, factor = implicit(omega, dt, n_steps_stab)
        stable = abs(y[-1]) < abs(y[0])
        print(f"{omega_dt:12.1f} | {factor:24.6e} | {abs(y[-1]):14.6e} | {'oui' if stable else 'NON':>10}")

    print("\n--> Le facteur 1/(1+omega*dt) reste toujours dans (0,1) pour tout omega*dt > 0 :")
    print("    le schema implicite est INCONDITIONNELLEMENT STABLE.")
 


if __name__ == "__main__":
    main()