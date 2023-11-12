import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import math
from sklearn import preprocessing
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

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

# Determine highest correlation features =============================================================
TEY_feat_correlation = df_train[features + ["TEY"]].corr()["TEY"][:].drop("TEY").abs()
TEY_impt_feats = []
print(TEY_feat_correlation, "\n")

for i in range(0, 4):
    max_corr = TEY_feat_correlation.idxmax()
    TEY_impt_feats.append(max_corr)
    TEY_feat_correlation = TEY_feat_correlation.drop(max_corr)

print(f"4 Most important features for TEY: {TEY_impt_feats}", "\n")

x_TEY_train = df_train[TEY_impt_feats].to_numpy()
y_TEY_train = df_train["TEY"].to_numpy()
x_TEY_test = df_test[TEY_impt_feats].to_numpy()
y_TEY_test = df_test["TEY"].to_numpy()

scaler2 = preprocessing.StandardScaler()
scaler5 = preprocessing.StandardScaler()
scaler8 = preprocessing.StandardScaler()

# Training polynomial regression models
polyreg2_TEY = make_pipeline(PolynomialFeatures(2),scaler2,LinearRegression())
polyreg2_TEY.fit(x_TEY_train, y_TEY_train)
polyreg5_TEY = make_pipeline(PolynomialFeatures(5),scaler5,LinearRegression())
polyreg5_TEY.fit(x_TEY_train, y_TEY_train)
polyreg11_TEY = make_pipeline(PolynomialFeatures(11),scaler8,LinearRegression(n_jobs=-1))
polyreg11_TEY.fit(x_TEY_train, y_TEY_train)

pickle.dump(polyreg11_TEY, open('Model_polyreg11_TEY.pkl', 'wb'))
pickle.dump(polyreg5_TEY, open('Model_polyreg5_TEY.pkl', 'wb'))
pickle.dump(polyreg2_TEY, open('Model_polyreg2_TEY.pkl', 'wb'))

# Evaluate
r2_TEY_2, rmse_TEY_2 = get_model_score(polyreg2_TEY, x_TEY_test, y_TEY_test)
TEY_rmse_list_2 = [rmse(y_pred, y_true) for y_pred, y_true in zip(polyreg2_TEY.predict(x_TEY_test), y_TEY_test)]

r2_TEY_5, rmse_TEY_5 = get_model_score(polyreg5_TEY, x_TEY_test, y_TEY_test)
TEY_rmse_list_5 = [rmse(y_pred, y_true) for y_pred, y_true in zip(polyreg5_TEY.predict(x_TEY_test), y_TEY_test)]

r2_TEY_11, rmse_TEY_11 = get_model_score(polyreg11_TEY, x_TEY_test, y_TEY_test)
TEY_rmse_list_11 = [rmse(y_pred, y_true) for y_pred, y_true in zip(polyreg11_TEY.predict(x_TEY_test), y_TEY_test)]

print(f"Performance of 2nd order polynomial regression model for TEY: R2 = {r2_TEY_2}, RMSE = {rmse_TEY_2}")
print(f"Performance of linear regression model for TEY: R2 = {r2_TEY_5}, RMSE = {rmse_TEY_5}")
print(f"Performance of linear regression model for TEY: R2 = {r2_TEY_11}, RMSE = {rmse_TEY_11}")

resultDict = {
    "TEY RMSE 2nd Order": rmse_TEY_2,
    "TEY RMSE 5th Order": rmse_TEY_5,
    "TEY RMSE 11th Order": rmse_TEY_11,
}

plt.bar(range(len(resultDict)), list(resultDict.values()), align='center')
plt.xticks(range(len(resultDict)), list(resultDict.keys()))

plt.show()

# Determine speed of system
import time

df = pd.read_csv("Gas Turbine Dataset/gt_2015.csv")
targets = ["NOX", "CO", "TEY"]
features = [column for column in df.columns if column not in targets]

x_test = df[features].to_numpy()
y_test = df["TEY"].to_numpy()

lin_model = pickle.load(open("Model_TEY_lin_reg_all.pkl", 'rb'))

start = time.time()
y_pred = lin_model.predict(x_test)
end = time.time()

print(f"Model took {end-start} seconds to predict on gt_2015.csv")