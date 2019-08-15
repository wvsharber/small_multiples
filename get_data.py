# load necessary libraries ----
import pandas as pd
import numpy as np

# create test data ----
commits_df = pd.DataFrame({"hour": range(1, 11),
                   "sam": np.random.randn(10) + np.random.randint(low=4, high=6, size=10),
                   "alex": np.random.randn(10) + np.random.randint(low=15, high=18, size=10),
                   "blake": list(range(1, 11))[::-1], 
                   "addison": [2] * 10, 
                   "cameron": np.random.randn(10) + np.random.randint(low=1, high=20, size=10),
                   "jaime": np.random.randn(10) + np.random.randint(low=1, high=10, size=10), 
                   "dakota": np.random.randn(10) + np.random.randint(low=5, high=6, size=10),
                   "jordan": np.random.randn(10) + np.random.randint(low=8, high=16, size=10), 
                   "kieran": np.random.randn(10) + np.random.randint(low=9, high=12, size=10)})

# transform commits_df from wide to long ----
commits_long_df = pd.melt(commits_df,
                          id_vars=["hour"],
                          value_vars=["sam", "alex", "blake",
                                      "addison", "cameron", "jaime",
                                      "dakota", "jordan", "kieran"])

# export commits_long_df as a CSV file ----
commits_long_df.to_csv("write_data/commits_per_hour_long.csv", index=False)

