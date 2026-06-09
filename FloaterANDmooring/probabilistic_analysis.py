import numpy as np
import matplotlib.pyplot as plt

#based on LC4 = 13510 kN
N_sim = 1000000  

#Load S: Normally distributed
mu_S = 10100      #kN (characteristic load)
sigma_S = 1200    #kN

#resistance R: Lognormally distributed
mu_R = 16500      # kN (Mean breaking strength of the chain)
cov_R = 0.10
sigma_R = mu_R * cov_R

#lognormal parameters for R
mu_ln = np.log(mu_R**2 / np.sqrt(mu_R**2 + sigma_R**2))
sigma_ln = np.sqrt(np.log(1 + (sigma_R**2 / mu_R**2)))

#random Variables
np.random.seed(42)  # Seed for reproducible results
R = np.random.lognormal(mu_ln, sigma_ln, N_sim)
S = np.random.normal(mu_S, sigma_S, N_sim)

g = R - S

N_fail = np.sum(g < 0)
P_f = N_fail / N_sim

if P_f > 0:
    from scipy.stats import norm
    beta = norm.ppf(1 - P_f)
else:
    beta = float('inf')

print(f"Number of failures: {N_fail}")
print(f"Failure Probability Pf: {P_f:.5e}")
print(f"Reliability Index Beta: {beta:.4f}")


plt.figure(figsize=(7, 4))
plt.hist(g, bins=100, alpha=0.75, color='strongblue' if 'strongblue' in plt.colormaps else 'steelblue', edgecolor='black')
plt.axvline(x=0, color='red', linestyle='--', linewidth=2, label='Failure Boundary ($g=0$)')
plt.title('Distribution of the Limit State Function $g(\mathbf{X}) = R - S$')
plt.xlabel('$g$ (Safety Margin in kN)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.savefig('Pictures/reliability_histogram.png', dpi=300)
plt.show()