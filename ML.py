import pandas as pd
from os.path import dirname, join
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def get_model_accuracy(model, X_test, y_test):
    model_acc = model.score(X_test, y_test)
    return model_acc

def ML(testDF):
    currentDir = dirname(__file__)
    filePath = join(currentDir, "./heart.csv")
    df = pd.read_csv(filePath)
    df.columns = ['Age', 'Sex', 'Chest_pain_type', 'Resting_bp',
                  'Cholesterol', 'Fasting_bs', 'Resting_ecg',
                  'Max_heart_rate', 'Exercise_induced_angina',
                  'ST_depression', 'ST_slope', 'Num_major_vessels',
                  'Thallium_test', 'Condition']
    naVal = testDF.columns[testDF.isna().any()].tolist()
    for val in naVal:
        del testDF[val]
        del df[val]
    X = df.drop(['Condition'], axis=1)
    y = df.Condition
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    lr = LogisticRegression(solver='newton-cg', max_iter=1000, random_state=42)
    lr.fit(X, y)
    # lrAcc = get_model_accuracy(lr, X_test, y_test)
    # print(f'Logistic Regression Accuracy: {lrAcc:.4}')

    prediction = lr.predict(testDF)
    return prediction
