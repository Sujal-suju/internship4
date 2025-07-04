# spam_detector.py

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 2. Load Dataset
# Using SMS Spam Collection Dataset
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])

# 3. Data Exploration
print("First 5 records:\n", df.head())
print("\nDataset Info:\n")
print(df.info())
print("\nClass Distribution:\n", df['label'].value_counts())

# 4. Data Preprocessing
df['label_num'] = df.label.map({'ham': 0, 'spam': 1})

# Convert text to numeric features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['message'])  # Feature matrix
y = df['label_num']                          # Target labels

# 5. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Train the Model
model = MultinomialNB()
model.fit(X_train, y_train)

# 7. Predict and Evaluate
y_pred = model.predict(X_test)

print("\nAccuracy Score:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# 8. Test with Custom Input
def predict_spam(text):
    vec = vectorizer.transform([text])
    result = model.predict(vec)
    return "SPAM" if result[0] == 1 else "HAM"

# Example Test
test_msg = "Congratulations! You've won a free ticket. Call now!"
print("\nTest message:", test_msg)
print("Prediction:", predict_spam(test_msg))
