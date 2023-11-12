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

def get_model_score(lin_model, x, y):
    y_pred = lin_model.predict(x)
    r2 = r2_score(y_pred, y)
    rmse = mean_squared_error(y_pred, y, squared=False)
    return r2, rmse

def rmse(x, y):
    return math.sqrt(((x - y) ** 2).mean())

# Preprocess Code - Split train and test data
all_filenames = [i for i in glob.glob('Gas Turbine Dataset/*.csv')]
df_raw = pd.concat([pd.read_csv(f) for f in all_filenames])
targets = ["NOX", "CO", "TEY"]
features = [column for column in df_raw.columns if column not in targets]
df_train, df_test = split_train_validation_dataset(df_raw, 0.80)

# (1) Set up multiple linear regression of TEY and CO and evaluate R2 and RMSE ========================================
CO_lin_reg_all  = LinearRegression()
TEY_lin_reg_all = LinearRegression()
x_CO_train = df_train[features].to_numpy()
y_CO_train = df_train["CO"].to_numpy()
x_CO_test = df_test[features].to_numpy()
y_CO_test = df_test["CO"].to_numpy()
x_TEY_train = df_train[features].to_numpy()
y_TEY_train = df_train["TEY"].to_numpy()
x_TEY_test = df_test[features].to_numpy()
y_TEY_test = df_test["TEY"].to_numpy()
CO_lin_reg_all.fit(x_CO_train, y_CO_train)
TEY_lin_reg_all.fit(x_TEY_train, y_TEY_train)

pickle.dump(CO_lin_reg_all, open('Model_CO_lin_reg_all.pkl', 'wb'))
pickle.dump(TEY_lin_reg_all, open('Model_TEY_lin_reg_all.pkl', 'wb'))
r2_CO, rmse_CO = get_model_score(CO_lin_reg_all, x_CO_test, y_CO_test)
r2_TEY, rmse_TEY = get_model_score(TEY_lin_reg_all, x_TEY_test, y_TEY_test)
print(f"Performance of linear regression model for CO: R2 = {r2_CO}, RMSE = {rmse_CO}")
print(f"Performance of linear regression model for TEY: R2 = {r2_TEY}, RMSE = {rmse_TEY}")

resultDict = {}
resultDict["CO RMSE All Feats"] = rmse_CO
resultDict["TEY RMSE All Feats"] = rmse_TEY
plt.bar(range(len(resultDict)), list(resultDict.values()), align='center')
plt.xticks(range(len(resultDict)), list(resultDict.keys()))
plt.show()

# (2) Bar Graphs for Multiple Linear Regression
# As we can see from both R2 score, the RMSE and the bar graphs, both models improved dramatically when more
# features were used compared to single feature linear regression. More features doesn't always lead to a
# better model due to the risk of overfitting or correlatory reltionships between the features, however in
# this case the models did improve but this doesn't necessarily mean that 8 features is the optimal choice,
# a more rigirous selection of features may lead to better results.