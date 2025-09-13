import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.metrics import accuracy_score, classification_report, r2_score


dataset = pd.read_csv(r"D:\AI_Python\education_inequality_data.csv")
# print(dataset.head(5))

print(dataset.info())

# print(dataset.isnull().sum())

# print(dataset.head(10))

#Now I am using the Label Encoder
label = LabelEncoder()
dataset["state"] = label.fit_transform(dataset["state"])
dataset["school_type"] = label.fit_transform(dataset["school_type"])
dataset["grade_level"] = label.fit_transform(dataset["grade_level"])

#droping the useless columns
dataset.drop(columns=["id"], axis=1, inplace=True)
# print(dataset.info())
 
#Now I am using the onehotencoder
Encoder = OneHotEncoder(sparse_output=False, drop=None)
encoded = Encoder.fit_transform(dataset[['school_name']])
encoded_col = Encoder.get_feature_names_out(['school_name'])
encoded_df = pd.DataFrame(encoded, columns=encoded_col, index=dataset.index)
dataset.drop(columns=['school_name'], inplace=True)
dataset = pd.concat([dataset, encoded_df], axis=1)

print(dataset.head(10))

# NUMARIC COLUMNS
numaric_col = ["funding_per_student_usd",
               "avg_test_score_percent",
               "student_teacher_ratio",
               "percent_low_income",
               "percent_minority",
               "internet_access_percent",
               "dropout_rate_percent"]

scalar = StandardScaler()
scaled = scalar.fit_transform(dataset[numaric_col])
scaled_df = pd.DataFrame(scaled, columns=numaric_col, index=dataset.index)
dataset[numaric_col] = scaled_df

# print(dataset.info())

# print(dataset.columns.tolist())

X = dataset.drop(columns=['avg_test_score_percent'], axis=1)
y = dataset['avg_test_score_percent']

# print(X)


X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeRegressor(max_depth=6)
model.fit(X_train, Y_train)

model_pred = model.predict(X_test)

print(f"R2_scoure: {r2_score(Y_test, model_pred)}")