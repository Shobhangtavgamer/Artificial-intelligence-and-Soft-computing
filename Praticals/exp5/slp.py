import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("C:\\Users\\Shobhankar\\OneDrive\\Desktop\\codinig\\AISC\\exp7\\data.csv")
X = data[["Area"]]
y = data["Price"]
model = LinearRegression()
model.fit(X, y)
print("Linear Regression Model")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
area = float(input("\nEnter Area: "))
prediction = model.predict([[area]])
print("Predicted Price:", round(prediction[0], 2))
plt.scatter(X, y, label="Actual Data")
plt.plot(X, model.predict(X), label="Regression Line")
plt.scatter([area], [prediction[0]], label="Predicted Point")
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Real State Price Prediction")
plt.legend()
plt.grid(True)
plt.show()
