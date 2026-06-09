import numpy as np
import matplotlib.pyplot as plt

k_moor = 2.5e5

surge = np.linspace(0,80,200)
F = k_moor * surge

plt.figure(figsize=(6,4))
plt.plot(surge,F/1000)
plt.grid(True)

plt.xlabel("Surge displacement [m]")
plt.ylabel("Restoring force [kN]")

plt.tight_layout()
plt.savefig("mooring_stiffness.png",dpi=300)

plt.show()