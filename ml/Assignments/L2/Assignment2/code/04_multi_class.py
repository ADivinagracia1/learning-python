
from scipy.io import loadmat
from tslearn import metrics
from tslearn.metrics import dtw
import numpy as np
import pandas as pd
import scipy
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


### Feature Extratcion

# File organization (Change this depending on folder structure)
# sample: dataset_multi_path  = "datasets/multi_class/"
generate_path       = ""
dataset_binary_path = ""
dataset_multi_path  = ""

# Load all files into variables
files = ["APC", "LBBB", "NORMAL", "PVC", "RBBB"]
categories = {beat:i for i, beat in zip(range(0,len(files)), files)} #dictionary, creates 6th Class column
ecg_data = {}
for name in files:
    ecg_data[name] = {}
    ecg_data[name]["sample"] = loadmat(f'{dataset_multi_path}/{name}_BEATS.mat')[f'{name}_BEATS']
    ecg_data[name]["true"] = loadmat(f'{dataset_multi_path}/{name}.mat')[f'{name}']

categories = {beat:i for i, beat in zip(range(0,len(files)), files)}

# Evaluate DTW and generate new dataframe
data_list = []
for beat in files:
    for sample in np.transpose(ecg_data[beat]["sample"]):
        data_row = [dtw(ecg_data[beat_inner]['true'], sample) for beat_inner in files]
        data_row.append(categories[beat])
        data_list.append(data_row)

# Show dataframe
df_ecg = pd.DataFrame(data_list, columns=[*files, "Class"])
print(df_ecg)

# Save dataframe
df_ecg.to_csv(generate_path+"/ecg_dataframe.csv", index=False)
df_ecg = pd.read_csv(generate_path+"/ecg_dataframe.csv")

### Prerpocessing
files = ["APC", "LBBB", "NORMAL", "PVC", "RBBB"]
ecg_features = df_ecg[files]
ecg_target   = df_ecg["Class"]
X_train_ecg, X_test_ecg, y_train_ecg, y_test_ecg = train_test_split(ecg_features, ecg_target, test_size=0.2, stratify=df_ecg["Class"])

def classifier_performance_ecg(model, y_pred_ecg, title):
    print('Classification Report: \n', classification_report(y_test_ecg,y_pred_ecg,target_names=files))
    # Plot normalized confusion matrix
    disp = plot_confusion_matrix(model, X_test_ecg, y_test_ecg,
                                 display_labels=files,
                                 cmap=plt.cm.Blues,
                                 normalize='true')
    disp.ax_.set_title(title)
    print(title)
    print(disp.confusion_matrix)
    plt.show()
    return

### K NEAREST Neighbors Classification
from sklearn.neighbors import KNeighborsClassifier
ECG_MODEL_KNN = KNeighborsClassifier(n_neighbors=5)  # Instantiating the model (using the default parameters)
ECG_MODEL_KNN.fit(X_train_ecg,y_train_ecg)           # Train the Model
y_pred_ecg_KNN = ECG_MODEL_KNN.predict(X_test_ecg)   # Predict the Trained Model on our Test data
classifier_performance_ecg(ECG_MODEL_KNN, y_pred_ecg_KNN, "K Nearest Neighbors Confusion Matrix")
pickle.dump(ECG_MODEL_KNN, open(generate_path+'/ECGKNearestNeighbors.pkl', 'wb')) # Save Trained Model

### Decision Tree Classification
from sklearn.tree import DecisionTreeClassifier
ECG_MODEL_DT = DecisionTreeClassifier()               # Instantiating the model (using the default parameters)
ECG_MODEL_DT.fit(X_train_ecg,y_train_ecg)             # Train the Model
y_pred_ecg_DT = ECG_MODEL_DT.predict(X_test_ecg)      # Predict the Trained Model on our Test data
classifier_performance_ecg(ECG_MODEL_DT, y_pred_ecg_DT, "Decision Tree Confusion Matrix")
pickle.dump(ECG_MODEL_DT, open(generate_path+'/ECGDecisionTree.pkl', 'wb')) # Save Trained Model

### Gaussian Naive Bayes Classification
from sklearn.naive_bayes import GaussianNB
ECG_MODEL_GNB = GaussianNB()                       # Instantiating the model (using the default parameters)
ECG_MODEL_GNB.fit(X_train_ecg,y_train_ecg)         # Train the Model
y_pred_ecg_GNB = ECG_MODEL_GNB.predict(X_test_ecg) # Predict the Trained Model on our Test data
classifier_performance_ecg(ECG_MODEL_GNB, y_pred_ecg_GNB, "Gaussian Naive Bayes Confusion Matrix")
pickle.dump(ECG_MODEL_GNB, open(generate_path+'/ECGGaussianNaiveBayes.pkl', 'wb')) # Save Trained Model

### Support Vector Machine Classification
from sklearn.svm import SVC
ECG_MODEL_SVM = SVC()                              # Instantiating the model (using the default parameters)
ECG_MODEL_SVM.fit(X_train_ecg,y_train_ecg)         # Train the Model
y_pred_ecg_SVM = ECG_MODEL_SVM.predict(X_test_ecg) # Predict the Trained Model on our Test data
classifier_performance_ecg(ECG_MODEL_SVM, y_pred_ecg_SVM, "Gaussian Naive Bayes Confusion Matrix")
pickle.dump(ECG_MODEL_SVM, open(generate_path+'/ECGSupportVector.pkl', 'wb')) # Save Trained Model

# Judging based off the Confusion matricies from the outputs of each models, the K Nearest Neighbors with have the
# most success of classification. Every model hovers around a precision of 0.9. The model that comes close is the
# decision tree classification which NORMAL ECG beats with a <0.80 precision. In real world application, I would be
# testing the dataset with other models and compare more performances. More datapoints would be prefered for a more
# accurate performance, but the KNN model for this dataset is a good choice.