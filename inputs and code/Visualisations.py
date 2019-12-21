import pandas as pd
import xlrd
import numpy as np
import seaborn as sns
import matplotlib as mat
import matplotlib.pyplot as plt
from scipy import stats

"""This is to note that creating several plots in one go may lead to distotion of certain plots due to correlation and overlapping of variables.thus it is expected
to save them one by one to avoid such errors"""

f=pd.read_csv('combined data.csv')
s=sns.heatmap(f.corr())
s.set_xticklabels(s.get_xticklabels(),rotation=14,fontsize=6)
s.set_yticklabels(s.get_yticklabels(),rotation=14,fontsize=6)
s.get_figure().savefig('correlation.png')
g=sns.heatmap(f.isnull(),yticklabels=False,cbar=False)
g.set_xticklabels(g.get_xticklabels(),rotation=12,fontsize=7)
g.get_figure().savefig('Null values.png')
left=f.groupby('left')
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',2000)
pd.set_option('display.max_rows',50)
print(left.mean())
print('\n\n')
print(f.describe())
print('\n\n')
print(f.left.value_counts())
sns.countplot(x="left",data=f).get_figure().savefig('Employee dist.png')
sns.countplot(x='salary',data=f,hue='left').get_figure().savefig("Salary dist.png")
hue='left' divides the data on basis of 'left' column.
sns.countplot(x='number_project',data=f,hue='left').get_figure().savefig("project dist.png")
#.set_title('Frquency plot of number_projects') can be used to add a title if required.

sns.countplot(x='time_spend_company',hue='left',data=f).get_figure().savefig("timespend.png")

sns.countplot(x='Work_accident',data=f,hue='left').get_figure().savefig("work accident.png")
g=sns.countplot(x='dept',data=f)
g.set_xticklabels(g.get_xticklabels(),rotation=12,fontsize=7)
g.get_figure().savefig('dept.png')
#please comment out the other countplots to see correct visualisation,as graph gets affected due correlation amongst variables.
f["satisfaction_level"].plot.hist(bins=80).get_figure().savefig('satisfaction.png')
sns.countplot(x='promotion_last_5years',data=f).get_figure().savefig("promotion.png")

