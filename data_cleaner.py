import pandas as pd

df = pd.read_csv("raw_data.csv")
columns = ['cough', 'fever', 'sore_throat', 'shortness_of_breath',
       'head_ache', 'corona_result', 'age_60_and_above', 'gender',
       'test_indication']
df = df[columns]
init_size = df.size
df = df[df.corona_result != 'other']
df = df.dropna()
print(df['corona_result'].unique())
print(df['gender'].unique())
df['corona_result'] = df['corona_result'].replace({ 'positive': 1, 'negative': 0 })
df['age_60_and_above'] = df['age_60_and_above'].replace({ 'Yes': 1, 'No': 0 })
df['gender'] = df['gender'].replace({ 'male': 1, 'female': 0 })
print(df['test_indication'].unique())
df['test_indication'] = df['test_indication'].replace({ 'Other': 0, 'Abroad': 0, 'Contact with confirmed': 1 })
print(df['corona_result'].unique())


final_size = df.size

print((init_size-final_size)*100/init_size)

print(df)
df.to_csv('cleaned_data.csv', index=False)