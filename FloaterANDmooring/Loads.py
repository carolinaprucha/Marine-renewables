import pandas as pd

LC1 = ["Operational", 2500, 150, 1500]
LC2 = ["50-year Wind", 4600, 150, 2500]
LC3 = ["100-year Wave", 500, 407, 2500]
LC4 = ["Combined Extreme", 4600, 407, 5000]

df = pd.DataFrame(
[
LC1,
LC2,
LC3,
LC4
],
columns=[
"Load Case",
"Wind [kN]",
"Wave [kN]",
"Mooring [kN]"
]
)

df["Total [kN]"] = (
df["Wind [kN]"]
+ df["Wave [kN]"]
+ df["Mooring [kN]"]
)

print(df)