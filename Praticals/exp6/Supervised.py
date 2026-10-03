import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

X = np.array([
    [150, 42],
    [155, 45],
    [160, 48],

    [160, 55],
    [165, 60],
    [170, 65],
    [175, 70],

    [160, 70],
    [165, 75],
    [170, 80],
    [175, 85],

    [160, 85],
    [165, 90],
    [170, 95],
    [175, 100]
])
y = np.array([
    0, 0, 0,
    1, 1, 1, 1,
    2, 2, 2, 2,
    3, 3, 3, 3
])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model = MLPClassifier(
    hidden_layer_sizes=(10,),
    activation='relu',
    max_iter=2000,
    random_state=42
)
model.fit(X_scaled, y)
print("       BMI PREDICTION")
print("   MLP Supervised Learning")
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
height_m = height / 100
bmi = weight / (height_m * height_m)
print("\nYour BMI is:", round(bmi, 2))
user_data = np.array([[height, weight]])
user_scaled = scaler.transform(user_data)
prediction = model.predict(user_scaled)
categories = {
    0: "Underweight",
    1: "Normal",
    2: "Overweight",
    3: "Obese"
}
result = categories[prediction[0]]
print("Predicted BMI Category:", result)
print("Prediction completed!")
