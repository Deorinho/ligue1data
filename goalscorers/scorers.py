from wsgiref import headers
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['Rk','Player','Nation','Pos','Squad','Age','Born','Gls','Sh','SoT','SoT%','G/Sh','G/SoT','xG','npxG','npxG/Sh']

ax = pd.read_csv("goalscorers.csv", names = headers)

#goal scorers in relation to their Age and Goals
ax.plot(x = 'Age' , y = 'Gls')
plt.show()
