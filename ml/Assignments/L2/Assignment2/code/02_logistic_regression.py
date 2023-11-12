import numpy as np
import pandas as pd
import pickle
import scipy
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

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

### LOGISTIC REGRESSION

logreg = LogisticRegression()    # instanciating model
logreg.fit(X_train,y_train)      # create model based on data
y_pred = logreg.predict(X_test)  # predict label basted on test
#save trained model
pickle.dump(logreg, open(f'{generate_path}Model_LogisticRegression.pkl', 'wb'))

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Generate Confusion Matrix
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
cnf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix\n', cnf_matrix)

# Plot Confusion Matrix
plt_cnf_matrix = plot_confusion_matrix(logreg, X_test, y_test,
                                       display_labels=['Alive','Dead'],
                                       cmap=plt.cm.Blues,
                                       normalize='true')
plt_cnf_matrix.ax_.set_title('Confusion Matrix - Binary Classification')

# Print Evaluation Metrics
print("Accuracy:\t", accuracy_score( y_test, y_pred))
print("Precision:\t",precision_score(y_test, y_pred))
print("Recall:\t\t",   recall_score( y_test, y_pred))
print("F1 Score:\t", f1_score(       y_test, y_pred))

plt.show()

print("yeet")