# Carl Gustaf HEAT shell parameters
m = 3.2      # mass in kg
v = 255      # muzzle velocity in m/s
s = 0.95     # barrel acceleration distance in m

# Average force calculation in newtons
F_avg_N = (m * v**2) / (2 * s)

# Convert to kilonewtons
F_avg_kN = F_avg_N / 1000

print(f"Average force: {F_avg_kN:.2f} kN")
