import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = np.array([
    [20, 10],
    [25, 12],
    [30, 15],
    [35, 18],

    [40, 30],
    [45, 35],
    [50, 40],
    [55, 45],

    [70, 70],
    [75, 75],
    [80, 82],
    [85, 88]
])
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)
kmeans.fit(data)
clusters = kmeans.labels_
centers = kmeans.cluster_centers_

print("   K-MEANS CLUSTERING")
print("   CLOTHING STORE")
print("\nCluster Centers:")
for i, center in enumerate(centers):
    print(
        "Cluster", i,
        ": Income =", round(center[0], 2),
        "Spending =", round(center[1], 2)
    )
order = np.argsort(centers[:, 1])
cluster_names = {}
cluster_names[order[0]] = "Genuine Buyer"
cluster_names[order[1]] = "Middle Buyer"
cluster_names[order[2]] = "VIP Buyer"
print("\nCustomer Clusters:")
for i in range(len(data)):
    cluster = clusters[i]
    print(
        "Income:", data[i][0],
        "Spending:", data[i][1],
        "->",
        cluster_names[cluster]
    )
print("     NEW CUSTOMER")
income = float(
    input("Enter annual income (in thousands): ")
)
spending = float(
    input("Enter annual spending (in thousands): ")
)
new_customer = np.array([
    [income, spending]
])
cluster = kmeans.predict(new_customer)[0]
print("\nCustomer belongs to:")
print(cluster_names[cluster])
plt.figure(figsize=(8, 6))
for cluster_number in range(3):
    points = data[clusters == cluster_number]
    plt.scatter(
        points[:, 0],
        points[:, 1],
        s=100,
        label=cluster_names[cluster_number]
    )
plt.scatter(
    centers[:, 0],
    centers[:, 1],
    s=250,
    marker="X",
    label="Cluster Centers"
)
plt.scatter(
    income,
    spending,
    s=200,
    marker="*",
    label="New Customer"
)
plt.xlabel("Annual Income (in thousands)")
plt.ylabel("Annual Spending (in thousands)")
plt.title("Clothing Store Customer Segmentation")
plt.legend()
plt.grid(True)
plt.show()