import pandas as pd
import xlrd
import numpy as np
import seaborn as sns
import matplotlib as mat
import matplotlib.pyplot as plt
from scipy import stats

excel=pd.ExcelFile('takenmind.xlsx')
emp=excel.parse('Existing employees')
ex_emp=excel.parse('Employees who have left')
emp['left']=0
ex_emp['left']=1
df3=pd.concat([emp,ex_emp])
df3.to_csv('combined data.csv',sep=',')

