import pandas as pd
from sklearn.linear_model import LogisticRegression
from joblib import dump

df_train = pd.read_csv('train.feature.txt')
X = df_train.drop(columns=['category', 'title'])
y = df_train['category']
model = LogisticRegression(random_state=0, max_iter=1000)
model.fit(X, y)
dump(model, '052-model.joblib')