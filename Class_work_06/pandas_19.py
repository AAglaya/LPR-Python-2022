import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.rand(10, 2))
df[2] = df[0]**2 + df[1]**2

print(df)