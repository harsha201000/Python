# %%
import pandas as pd
import numpy as np

# %% [markdown]
# Let's load up the hotel booking data

# %%
df = pd.read_csv('hotel-booking-data.txt', delimiter='\t')
df.head()

# %%
df.describe()

# %%
df['Company'].value_counts()

# %%
df.dropna()

# %%
df['2xRoom'] = df['Room number'] * 2

# %%
df

# %%
df2 = df.dropna()

# %%
df2.head()

# %%
df['Room number'].isna()

# %%
mask = df['Room number'].isna()

df['Text Value'] = np.where(mask, df['Date'], np.nan)
df

# %%
df['Text Value'].fillna(method='bfill')

# %%
df2

# %%
df2.plot()


