import pandas as pd

glass = pd.read_csv("D:\data\glass.csv")
result = glass['Mg'][glass['typeGlass']==1].mean()
print('유리 종류 1번의 마그네슘(Mg) 성분의 평균 : {0}'.format(result))