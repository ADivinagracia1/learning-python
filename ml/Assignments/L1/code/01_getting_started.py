import numpy as np
import pandas as pd
import scipy
from scipy import stats
import matplotlib.pyplot as plt
import glob

#Preprocess Code: Gather datasets from all cvs's and seperate them
# (1), (2): Load datasets into array
extension = 'csv'
all_filenames = [i for i in glob.glob('Gas Turbine Dataset/*.{}'.format(extension))]
df_raw = pd.concat([pd.read_csv(f) for f in all_filenames])
targets = ["NOX", "CO", "TEY"]
features = [column for column in df_raw.columns if column not in targets]

# (3) Generate a histogram with 100 bins for the Nitrogen oxides (NOx) emission
# NOX looked like a normal distribution centered around ~62
df_raw.hist(column="NOX", bins=100, legend=True)
plt.xlabel("NOx Emissions")
plt.ylabel("Number of Points")

# (4a) Generate turbine inlet temperature (TIT) versus Turbine after temperature (TAT)
fig=plt.figure()
plt.scatter(df_raw['TIT'], df_raw['TAT'], label = "TIT vs TAT")
fig.legend(loc = 'upper right')
plt.title("TIT vs TAT")
plt.xlabel("TIT")
plt.ylabel("TAT")

# (4b) Generate turbine inlet temperature (TIT) versus Turbine energy yield (TEY)
fig=plt.figure()
plt.scatter(df_raw['TIT'], df_raw['TEY'], label = "TIT vs TEY")
fig.legend(loc = 'upper right')
plt.title("TIT vs TEY")
plt.xlabel("TIT")
plt.ylabel("TEY")

# (4c)
print(f"Pearson's Correlation Coefficient of TIT vs TAT: {stats.pearsonr(df_raw['TIT'], df_raw['TAT'])}")
print(f"Pearson's Correlation Coefficient of TIT vs TEY: {stats.pearsonr(df_raw['TIT'], df_raw['TEY'])}")

## Scatter Plots and Pearson's Correlation Coefficients of TIT vs TAT and TIT vs TEY
# There appears to be a non linear associations between TIT and TAT with a decreasing slope the higher TIT rises.
# On the other hand, there appears to be a linear relationship between TIT and TEY.
#
# In both cases, there seems to be a hard limitation to the sensor readings indicating that there may be readings
# that go beyond the range of the sensor that are incorrectly recorded which might affect the relationship inference
# from the scatter plots.
#
# Looking at the Pearson's correlation coefficients, this confirms our assumptions based on the scatter plots. For
# TIT vs TAT, a PCC of ~-0.381 indicates there isn't a strong linearity between the two variables, this might even be
# skewed higher because of the apparent limitation on TIT readings. For TIT vs TEY, a PCC of ~0.910 indicates a strong
# positive linear relationship between the variables as we can see in the scatter plot.

# (5) Split Training Data
def split_train_validation_dataset(df, split):
    mask = np.random.rand(len(df)) < split
    df_train = df[mask]
    df_test = df[~mask]
    return df_train, df_test

df_train, df_test = split_train_validation_dataset(df_raw, 0.80)

plt.show()