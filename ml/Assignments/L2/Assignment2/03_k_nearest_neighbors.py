import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import accuracy_score, f1_score, recall_score
from sklearn.neighbors import KNeighborsClassifier

### PREPROCESSING

# File organization (Change this depending on folder structure)
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


### K-Nearest Neighbors

# Output data
labels = ['Alive', 'Dead'];
def classifier_performance_knn(model, y_prediction, kval):
    # Develop Confusion Matrix
    disp = plot_confusion_matrix(model, X_test, y_test, display_labels=labels, cmap=plt.cm.Blues, normalize='true')
    disp.ax_.set_title(f'Confustion Matrix: KNN where K = {kval}')

    # Calculate Specifity
    TN = disp.confusion_matrix[1][1]
    FP = disp.confusion_matrix[0][1]
    specif = TN / (TN + FP)

    # Print performance values and confusion matrix
    print(f'=================================== K = {kval} ===================================')
    print('Confusion Matrix\n', disp.confusion_matrix)
    print("Accuracy:\t", round(accuracy_score(y_test, y_prediction), 3))
    print("F1 Score:\t", round(f1_score(y_test, y_prediction), 3))
    print("Sensitivity:\t", round(recall_score(y_test, y_prediction), 3))
    print("Specificity:\t", round(specif, 3))
    plt.show()

    return accuracy_score(y_test, y_prediction)

# Run models from K = 1...10
k_accuracy = []
for K in range(1,11):

    # Instantiating the model (using the default parameters)
    MODEL_KNN = KNeighborsClassifier(n_neighbors=K)      # instanciating model
    MODEL_KNN.fit(X_train,y_train)                       # create model based on data
    y_pred_KNN = MODEL_KNN.predict(X_test)               # predict label basted on test

    # Save trained model
    pickle.dump(MODEL_KNN, open(f'{generate_path}Model_KNN_{K}.pkl', 'wb'))

    # Generate confusion matrix and performance data
    k_accuracy.append(classifier_performance_knn(MODEL_KNN,y_pred_KNN,K))

print(k_accuracy)

# Output K-Value performance
plt.plot(k_accuracy)
plt.title('K-value Trained Model Accuracy')
plt.xlabel('K-Value')
plt.ylabel('Accuracy')
plt.show()