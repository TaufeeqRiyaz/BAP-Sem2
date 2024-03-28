#In[]
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
titanic.head()
# %%
# data visualization
sns.lineplot(data=titanic, x='age', y='fare')
plt.show()
# %%
