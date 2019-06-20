import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6, 7), index=list(range(0, 12, 2)),
                   columns=list(range(0, 7, 1)))

print df1