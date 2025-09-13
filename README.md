*Education Inequality – Student Performance Prediction
Overview*

This project focuses on analyzing the impact of educational inequality on student outcomes. The model predicts a student’s average test score percentage based on multiple socio-economic and institutional factors. By examining elements such as funding per student, school type, internet access, and demographic data, the project aims to highlight how inequality affects educational performance.

Dataset

The dataset contains information about schools, their funding, demographics, and performance metrics. Key attributes include:

State – The state where the school is located

School Type – Type of school (e.g., public, private)

Grade Level – Level of education (e.g., primary, secondary)

Funding per Student (USD) – Financial allocation per student

Student-Teacher Ratio – Average number of students per teacher

Percent Low Income – Share of students from low-income households

Percent Minority – Proportion of minority students

Internet Access Percent – Percentage of students with internet access

Dropout Rate Percent – School’s dropout percentage

Average Test Score Percent – Target variable representing student performance

Data Preprocessing

To prepare the dataset for training:

Encoding

Applied LabelEncoder to categorical variables (state, school_type, grade_level).

Used OneHotEncoder for school_name to capture detailed distinctions.

Cleaning

Removed non-essential columns (e.g., ID).

Scaling

Standardized numerical features such as funding, test scores, ratios, and percentages using StandardScaler.

Model

A Decision Tree Regressor was used to predict average student test scores.

Algorithm: Decision Tree Regressor

Max Depth: 6 (to avoid overfitting)

Train-Test Split: 80% training, 20% testing

The model outputs an R² Score, which evaluates how well the independent variables explain variations in student performance.

Evaluation

Metric: R² Score (coefficient of determination)

A higher R² value indicates stronger predictive performance of the model.

Applications

This project can be used to:

Identify how funding, demographics, and infrastructure impact student success.

Support policymakers in reducing educational inequality.

Provide insights for educators and institutions to improve performance outcomes.

Future Improvements

Experiment with advanced models such as Random Forest, Gradient Boosting, or Neural Networks.

Add feature importance analysis to understand which factors contribute most to inequality.

Extend dataset with real-world educational data for broader impact.

Incorporate fairness metrics to assess bias in predictions.
