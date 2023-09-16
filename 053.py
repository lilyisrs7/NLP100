import pandas as pd
import numpy as np
from joblib import load

wvmodel = load('051-wvmodel.joblib')
model = load('052-model.joblib')
def predict(title):
    vec = np.mean([wvmodel.wv[word] for word in title.split()], axis=0)
    probs = model.predict_proba(pd.DataFrame([vec]))
    y = np.argmax(probs[0])
    y_prob = probs[0][y]
    return y, y_prob