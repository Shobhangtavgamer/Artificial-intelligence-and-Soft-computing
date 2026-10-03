import numpy as np
import matplotlib.pyplot as plt

X = np.array([[0, 0],[0, 1],[1, 0],[1, 1]])
Y = np.array([[0], [1],[1],[0]])
input_neurons = 2
hidden_neurons = 3
output_neurons = 1
learning_rate = 0.5
epochs = 10000

np.random.seed(95)
W1 = np.random.randn(input_neurons, hidden_neurons)
W2 = np.random.randn(hidden_neurons, output_neurons)
b1 = np.zeros((1, hidden_neurons))
b2 = np.zeros((1, output_neurons))
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
errors = []
for epoch in range(epochs):
    hidden = sigmoid(np.dot(X, W1) + b1)
    output = sigmoid(np.dot(hidden, W2) + b2)
    error = Y - output
    errors.append(np.mean(error ** 2))
    d_output = error * output * (1 - output)
    d_hidden = d_output.dot(W2.T) * hidden * (1 - hidden)
    W2 += learning_rate * hidden.T.dot(d_output)
    W1 += learning_rate * X.T.dot(d_hidden)
    b2 += learning_rate * np.sum(d_output, axis=0)
    b1 += learning_rate * np.sum(d_hidden, axis=0)
print("Final Output:")
print(output.round(3))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
input_pos = [(0, 2), (0, 1)]
hidden_pos = [(2, 3), (2, 2), (2, 1)]
output_pos = [(4, 2)]
for x1, y1 in input_pos:
    for x2, y2 in hidden_pos:
        ax1.plot([x1, x2], [y1, y2], color="gray", linewidth=1)
for x1, y1 in hidden_pos:
    for x2, y2 in output_pos:
        ax1.plot([x1, x2], [y1, y2], color="gray", linewidth=1)
for i, (x, y) in enumerate(input_pos):
    ax1.scatter(x, y, s=1000, color="skyblue")
    ax1.text(x, y, f"X{i+1}", ha="center", va="center", fontsize=12)
for i, (x, y) in enumerate(hidden_pos):
    ax1.scatter(x, y, s=1000, color="orange")
    ax1.text(x, y, f"H{i+1}", ha="center", va="center", fontsize=12)
for x, y in output_pos:
    ax1.scatter(x, y, s=1000, color="lightgreen")
    ax1.text(x, y, "Y", ha="center", va="center", fontsize=12)
ax1.text(0, 3.5, "INPUT", ha="center", fontsize=13, fontweight="bold")
ax1.text(2, 3.5, "HIDDEN", ha="center", fontsize=13, fontweight="bold")
ax1.text(4, 3.5, "OUTPUT", ha="center", fontsize=13, fontweight="bold")
ax1.set_xlim(-0.5, 4.5)
ax1.set_ylim(0.5, 4)
ax1.axis("off")
ax1.set_title("MLP Neural Network", fontsize=15)
ax2.plot(range(1, epochs + 1), errors, color="red", linewidth=2)
ax2.set_xlabel("Epoch")
ax2.set_ylabel("Mean Squared Error")
ax2.set_title("Training Error", fontsize=15)
ax2.grid(True)
plt.tight_layout()
plt.show()