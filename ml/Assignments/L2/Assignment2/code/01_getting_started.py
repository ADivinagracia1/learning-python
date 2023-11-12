import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt

### PREPROCESSING
# Folder Organization (Change this depending on folder structure)
# sample: dataset_multi_path  = "datasets/multi_class/"
generate_path       = ""
dataset_binary_path = ""
dataset_multi_path  = ""

# Importing the dataset via pandas
df_raw = pd.read_csv(f"{dataset_binary_path}heart_failure_dataset.csv")
# Separate Targets and Features
targets = ["death_event"]
features = [column for column in df_raw.columns if column not in targets]
#Split death and alive
df_death = df_raw.loc[df_raw['death_event'] == 0]
df_alive = df_raw.loc[df_raw['death_event'] == 1]

# Split features and targets - X: Features, y: Targets
X_logreg = df_raw[features]
y_logreg = df_raw[targets].values.ravel()
# Splitting the dataset into the Training set and Test set where split is 80/20
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_logreg, y_logreg, test_size=0.2, random_state=42)
# Save Test Set
np.savetxt(f"{generate_path}features_heart_failure_logreg.csv", X_test, delimiter=",")
np.savetxt(f"{generate_path}targets_heart_failure_logreg.csv",  y_test, delimiter=",")
# Standardize features by removing the mean and scaling to unit variance
from sklearn.preprocessing import StandardScaler
X_train = pd.DataFrame(StandardScaler().fit_transform(X_train))
X_test  = pd.DataFrame(StandardScaler().fit_transform(X_test))

### Getting Started

#Count Patients who Died and Survived
death_split = df_raw["death_event"].value_counts(normalize=False)
print(f"Survived: {death_split[0]}, Died: {death_split[1]}\n")

#(1) Calculate Percentage
Anem_Smok = ((df_death['anaemia'] == 1) & (df_death['smoking'] == 1))
print(f"{round(Anem_Smok.sum()/death_split[1]*100, 2)}% who died had anaemia and smoked")

#(2a) CPK Values and boxplot
print(f"CPK Deaths Mean:  {round(df_death['creatinine_phosphokinase'].mean(), 2)}")
print(f"CPK Survive Mean: {round(df_alive['creatinine_phosphokinase'].mean(), 2)}")

# CPK Boxplot
plt.boxplot([df_death['creatinine_phosphokinase'], df_alive['creatinine_phosphokinase']], labels=['Dead','Alive'])
plt.ylabel("Level")
plt.title("Boxplot of CPK for Death vs Survival")

#(2b) CPK P Values
cpk_res = scipy.stats.ttest_ind(df_death['creatinine_phosphokinase'], df_alive['creatinine_phosphokinase'])
print(f"t-value: {cpk_res[0]}\np-value: {cpk_res[1]}")

plt.show()