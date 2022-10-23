import pickle
import pandas as pd

loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
df = pd.read_csv("sample_data.csv")

features = ['cough', 'fever', 'sore_throat', 'shortness_of_breath',
       'head_ache', 'age_60_and_above', 'gender',
       'test_indication']

result = 'corona_result'

X_test = df[features]
Y_test = df[result]

result = loaded_model.predict(X_test)
print(result)