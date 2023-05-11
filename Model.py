import sklearn.model_selection
from sklearn import preprocessing
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

loan_df = pd.read_csv('loan_train.csv')

for col in loan_df:
    if loan_df[col].dtype == 'object':
        loan_df[col] = OrdinalEncoder().fit_transform(loan_df[col].values.reshape(-1, 1))

# pre-processing
loan_data = loan_df.copy()
le = preprocessing.LabelEncoder()
Gender = le.fit_transform(list(loan_data["Gender"]))  # gender (1 = male; 0 = female)
Married = le.fit_transform(list(loan_data["Married"]))
Dependents = le.fit_transform(list(loan_data["Dependents"]))
Education = le.fit_transform(list(loan_data["Education"]))
Self_Employed = le.fit_transform(list(loan_data["Self_Employed"]))
Applicant_Income = le.fit_transform(list(loan_data["Applicant_Income"]))
Coapplicant_Income = le.fit_transform(list(loan_data["Coapplicant_Income"]))
Loan_Amount = le.fit_transform(list(loan_data["Loan_Amount"]))
Term = le.fit_transform(list(loan_data["Term"]))
Area = le.fit_transform(list(loan_data["Area"]))
Credit_History = le.fit_transform(list(loan_data["Credit_History"]))
Status = le.fit_transform(list(loan_data["Status"]))

x = list(
    zip(Gender, Married, Dependents, Education, Self_Employed, Applicant_Income, Coapplicant_Income, Loan_Amount, Term,
        Area, Credit_History))
y = list(Status)
# Test options and evaluation metric
num_folds = 5
seed = 7
scoring = 'accuracy'

# The test data will test the accuracy of the model created
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.20, random_state=seed)

# Model prediction
best_model = RandomForestClassifier()
best_model.fit(x_train, y_train)
y_pred = best_model.predict(x_test)
model_accuracy = accuracy_score(y_test, y_pred)
