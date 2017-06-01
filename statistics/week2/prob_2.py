import pandas as pd

glass = pd.read_csv("D:\data\glass.csv")
result = glass['Ca'][glass['typeGlass']==2].var()
print('유리 종류 1번의 마그네슘(Mg) 성분의 분산 : {0}'.format(result))