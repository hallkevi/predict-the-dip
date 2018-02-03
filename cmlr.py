import pandas as pd
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

#read data
dataframe = pd.read_csv('cms.csv', sep="[;,]", engine='python')

y_values = dataframe['ClosePrice'].tolist()
x_values = dataframe['Date'].tolist()
print(y_values, x_values)
ym = np.mean(y_values)
xm = np.mean(x_values)
print(ym)
print(xm)
yray = np.array(y_values)
xray = np.array(x_values)

sy = np.std(y_values)
sx = np.std(x_values)
cyx = np.corrcoef(y_values, x_values)[0, 1]
print(sy)
print(sx)
print(cyx)

slope = cyx*sy/sx
print(slope)

intercept = ym - slope*xm
print(intercept)

#train model on data
#body_reg = linear_model.LinearRegression()
#body_reg.fit(xray.reshape(-1, 1), yray.reshape(-1, 1))

#visualize results
plt.scatter(xray, yray)
#plt.plot(xray, body_reg.predict(xray))
plt.title('$y=%3.7sx+%3.7s$'%(slope, intercept))
plt.show()



