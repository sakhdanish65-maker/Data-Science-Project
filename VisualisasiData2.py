import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset('iris')
df = pd.DataFrame(data).drop_duplicates()

# print(df.head())
# print(df.info())
print(df.describe())
# print(df.isnull().sum())
# print(df.duplicated().sum())
# sns.histplot(df['sepal_length'])
sns.scatterplot(data=df,x='sepal_length',y='petal_length')
plt.show()