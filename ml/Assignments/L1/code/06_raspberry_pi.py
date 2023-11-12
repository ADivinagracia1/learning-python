import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
import pickle
import time
import glob


def get_model_score(lin_model, x, y):
    y_pred = lin_model.predict(x)
    r2 = r2_score(y_pred, y)
    rmse = mean_squared_error(y_pred, y, squared=False)
    
    return r2, rmse

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

df = pd.concat([pd.read_csv(f) for f in all_filenames])


targets = ["NOX", "CO", "TEY"]
features = [column for column in df.columns if column not in targets]

x_test = df[features].to_numpy()
y_test = df["TEY"].to_numpy()

lin_model = pickle.load(open("Model_TEY_lin_reg_all.pkl", 'rb'))

start = time.time()
y_pred = lin_model.predict(x_test)
end = time.time()

r2_test, rmse_test = get_model_score(lin_model, x_test, y_test)

colabTime = 0.00048995

print(f"\n\nPerformance of linear regression model for TEY: R2 = {r2_test}, RMSE = {rmse_test}")
print(f"Model took {round((end-start), 8)}s to predict on gt_2015.csv compared to {colabTime}s on Google Colab")
print(f"Google Colab was {round(((end-start)/colabTime), 5)} times faster\n")

input("press any key to begin simulation")
print("\n\n----------SIMULATED LINE BY LINE PREDICTION-------------")
for line in x_test:
	print(f"INPUT: {line.round(2)}, PREDICTION: {lin_model.predict(line.reshape(1, -1) )}\n")
	time.sleep(0.3)
