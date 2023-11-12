# Load General Libraries
import numpy as np
import pandas as pd
import scipy
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import glob

#Preprocess Code: Gather datasets from all cvs's and seperate them
extension = 'csv'
all_filenames = [i for i in glob.glob('Gas Turbine Dataset/*.{}'.format(extension))]
df_raw = pd.concat([pd.read_csv(f) for f in all_filenames])
targets = ["NOX", "CO", "TEY"]
features = [column for column in df_raw.columns if column not in targets]
print(f"Targets = {targets}")
print(f"Features = {features}")
print(f"Is there any NaN values in df? {df_raw.isnull().values.any()}")

df_raw.hist(column="NOX", bins=100, legend=True)
plt.xlabel("NOx Emissions")
plt.ylabel("Number of Points")
plt.show()