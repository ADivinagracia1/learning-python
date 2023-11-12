import numpy as np
import pandas as pd
import scipy
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import math

def split_train_validation_dataset(df, split):
    mask = np.random.rand(len(df)) < split
    df_train = df[mask]
    df_test = df[~mask]
    return df_train, df_test

# Preprocess Code - Split train and test data
all_filenames = [i for i in glob.glob('Gas Turbine Dataset/*.csv')]
df_raw = pd.concat([pd.read_csv(f) for f in all_filenames])
targets = ["NOX", "CO", "TEY"]
features = [column for column in df_raw.columns if column not in targets]
df_train, df_test = split_train_validation_dataset(df_raw, 0.80)

# Print and examine correlation coefficient
# From examination:
# Highest correlation for NOX was with AT: ~-0.559
# Highest correlation for CO was with TIT: ~-0.706
# Highest correlation for TEY was with CDP: ~0.989
for target in targets:
    print(df_train[features + [target]].corr()[target][:], "\n")

# (1) Build up linear regression models =================================================
NOX_lin_reg = LinearRegression()
CO_lin_reg  = LinearRegression()
TEY_lin_reg = LinearRegression()

x_NOX_train = df_train["AT"].to_numpy().reshape(-1,1)
y_NOX_train = df_train["NOX"].to_numpy()
x_NOX_test = df_test["AT"].to_numpy().reshape(-1,1)
y_NOX_test = df_test["NOX"].to_numpy()

x_CO_train = df_train["TIT"].to_numpy().reshape(-1,1)
y_CO_train = df_train["CO"].to_numpy()
x_CO_test = df_test["TIT"].to_numpy().reshape(-1,1)
y_CO_test = df_test["CO"].to_numpy()

x_TEY_train = df_train["CDP"].to_numpy().reshape(-1,1)
y_TEY_train = df_train["TEY"].to_numpy()
x_TEY_test = df_test["CDP"].to_numpy().reshape(-1,1)
y_TEY_test = df_test["TEY"].to_numpy()

NOX_lin_reg.fit(x_NOX_train, y_NOX_train)
CO_lin_reg.fit(x_CO_train, y_CO_train)
TEY_lin_reg.fit(x_TEY_train, y_TEY_train)

pickle.dump(NOX_lin_reg, open('Model_NOX_lin_reg.pkl', 'wb'))
pickle.dump(CO_lin_reg, open('Model_CO_lin_reg.pkl', 'wb'))
pickle.dump(TEY_lin_reg, open('Model_TEY_lin_reg.pkl', 'wb'))


def viz_linear(x, y, lin_model, title, xaxis, yaxis):
    plt.scatter(x, y, color='red')
    plt.plot(x, lin_model.predict(x), color='blue')
    plt.title(title)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.show()
    return

def get_model_score(lin_model, x, y):
    y_pred = lin_model.predict(x)
    r2 = r2_score(y_pred, y)
    rmse = mean_squared_error(y_pred, y, squared=False)
    return r2, rmse

def rmse(x, y):
    return math.sqrt(((x - y) ** 2).mean())

# (2) Evaluate R2 and RMSE models
viz_linear(x_NOX_train, y_NOX_train, NOX_lin_reg, "Linear Regression: AT vs NOX", "AT", "NOX")
viz_linear(x_CO_train, y_CO_train, CO_lin_reg, "Linear Regression: TIT vs CO", "TIT", "CO")
viz_linear(x_TEY_train, y_TEY_train, TEY_lin_reg, "Linear Regression: CDP vs TEY", "CDP", "TEY")

r2_NOX_test, rmse_NOX_test = get_model_score(NOX_lin_reg, x_NOX_test, y_NOX_test)
r2_CO_test,  rmse_CO_test  = get_model_score(CO_lin_reg, x_CO_test, y_CO_test)
r2_TEY_test, rmse_TEY_test = get_model_score(TEY_lin_reg, x_TEY_test, y_TEY_test)

r2_NOX_train, rmse_NOX_train = get_model_score(NOX_lin_reg, x_NOX_train, y_NOX_train)
r2_CO_train,  rmse_CO_train  = get_model_score(CO_lin_reg, x_CO_train, y_CO_train)
r2_TEY_train, rmse_TEY_train = get_model_score(TEY_lin_reg, x_TEY_train, y_TEY_train)

print(f"Performance of linear regression model for NOX, train: R2 = {r2_NOX_train}, RMSE = {rmse_NOX_train}, test: R2 = {r2_NOX_test}, RMSE = {rmse_NOX_test}")
print(f"Performance of linear regression model for CO, train:  R2 = {r2_CO_train},  RMSE = {rmse_CO_train},  test: R2 = {r2_CO_test},  RMSE = {rmse_CO_test}")
print(f"Performance of linear regression model for TEY, train: R2 = {r2_TEY_train}, RMSE = {rmse_TEY_train}, test: R2 = {r2_TEY_test}, RMSE = {rmse_TEY_test}")

# (3) Bar Graphs for Simple Linear Regression
# Based on the graphs, the error for the NOX model which indicates that the model doesn't fit the dataset
# very well. For the CO model, there is smaller RMSE and less variance but outliers are still present. Finally
# for the TEY model, the RMSE hovers around the same range for all the points indicating that the points follow
# along with the linear regression model across the dataset.

CO_lin_regPt2 = LinearRegression()

datasplit = [0.50,0.70,0.90]
resultDict = {}

for pct in datasplit:
  df_trainPt2, df_testPt2 = split_train_validation_dataset(df_raw, pct)
  CO_lin_regPt2 = LinearRegression()

  x_CO_trainPt2 = df_trainPt2["TIT"].to_numpy().reshape(-1,1)
  y_CO_trainPt2 = df_trainPt2["CO"].to_numpy()
  x_CO_testPt2 = df_testPt2["TIT"].to_numpy().reshape(-1,1)
  y_CO_testPt2 = df_testPt2["CO"].to_numpy()

  CO_lin_regPt2.fit(x_CO_trainPt2, y_CO_trainPt2)

  _, rmse_CO_trainPt2 = get_model_score(CO_lin_regPt2, x_CO_trainPt2, y_CO_trainPt2)
  _, rmse_CO_testPt2 = get_model_score(CO_lin_regPt2, x_CO_testPt2, y_CO_testPt2)

  resultDict[f"CO Train RMSE {pct*100}%"] = rmse_CO_trainPt2
  resultDict[f"CO Test RMSE {pct*100}%"] = rmse_CO_testPt2


plt.bar(range(len(resultDict)), list(resultDict.values()), align='center')
plt.xticks(range(len(resultDict)), list(resultDict.keys()))
plt.show()

# The bigger the dataset provided to train the linear regression model the lower the RMSE became, this applied
# when calculating RMSE for both the train and test datasets meaning that the model has not overfitted