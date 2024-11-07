import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv("C:\\Users\\brhva\\Downloads\\archive\\df_file.csv")

# print(df.head(100))
# df1 = []
# print(df.loc[df["Label"] == 0])
# # print(df.describe())
# df1.append(df.loc[df["Label"] == 0])
# print(df1)
# df3 = []
# df3.append(df.head(100))
# print (df3)
# df4 = df.drop(["Text"], axis=1)
# df_without_column = df.drop("Label", axis=1).copy()
# print(df_without_column)


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['Text'], df['Label'], test_size=0.3, random_state=42)

# Convert the text data to numerical features using TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=5000)  # You can adjust max_features based on your dataset
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# Check the dimensions of the vectors
print("Dimensions of X_train_tfidf:", X_train_tfidf.shape)
print("Number of samples in y_train:", len(y_train))

# Create a KNN classifier
knn_classifier = KNeighborsClassifier(n_neighbors=3)

# Fit the model on the training data
knn_classifier.fit(X_train_tfidf, y_train)

# Make predictions on the test set
y_test_pred = knn_classifier.predict(X_test_tfidf)

# Calculate and print metrics
accuracy = accuracy_score(y_test, y_test_pred)
precision = precision_score(y_test, y_test_pred, average='weighted')
recall = recall_score(y_test, y_test_pred, average='weighted')
f1 = f1_score(y_test, y_test_pred, average='weighted')

print("KNN Metrics:")
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")