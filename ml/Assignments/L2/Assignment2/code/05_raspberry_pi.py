import pandas as pd
import pickle
import time
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler

kval = 6
jupyertime = 0.00499964

# File organization
generate_path = "model_generated"
dataset_binary_path = "datasets/binary_class"
df_raw = pd.read_csv(f"{dataset_binary_path}/heart_failure_dataset.csv")

# Split targets and features
targets = ["death_event"]
features = [column for column in df_raw.columns if column not in targets]
X_test = df_raw[features].to_numpy()
y_test = df_raw[targets].to_numpy()
X_test = pd.DataFrame(StandardScaler().fit_transform(X_test)).to_numpy()

# Obtain Model
knn_model = pickle.load(open(f"{generate_path}/Model_KNN_{kval}.pkl", 'rb'))
t_start = time.time()
y_pred = knn_model.predict(X_test)
t_end = time.time()
print('Classification Report: \n', classification_report(y_test, y_pred, target_names=['Alive', 'Dead']))
print(f"Model took {round((t_end-t_start), 8)}s to predict on gt_2015.csv compared to {jupyertime}s on Jupyter Notebook")

result_dict = {0: "Dead", 1: "Alive"}
results = []
input("\npress enter to begin simulation")
print("\n\n----------SIMULATED LINE BY LINE PREDICTION-------------")
for line in X_test:
	dead_alive = result_dict[int(knn_model.predict(line.reshape(1, -1)))]
	print(f"INPUT: {line}, PREDICTION: { dead_alive }\n")
	results.append(dead_alive)
	time.sleep(0.3)

df_csv = df_raw[features]
df_csv["RESULTS"] = results
df_csv.to_csv("out.csv")