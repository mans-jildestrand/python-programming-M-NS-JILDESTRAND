import numpy as np
import matplotlib.pyplot as plt
from Functions import Functions


unlabelled = np.loadtxt(r"C:\Users\monza\Desktop\REPO\python-programming-M-NS-JILDESTRAND\Labs\Lab3\unlabelled_data.csv", delimiter=",")

# Skapa linjen för klassificering
x_line = np.linspace(np.min(unlabelled[:, 0]), np.max(unlabelled[:, 0]), 100)
y_line = -0.9 * x_line + 0.5

# Använd funktion för att dela punkter ovanför och under linjen
x_above, y_above, x_below, y_below, above_idx, below_idx = Functions(
    unlabelled[:, 0], unlabelled[:, 1], slope=-0.9, intercept=0.5
)

labels = np.empty(len(unlabelled), dtype=int)
labels[above_idx] = 1
labels[below_idx] = 0

# Spara den labelade datan till en ny fil
labeled_data = np.column_stack((unlabelled, labels))
np.savetxt(
    r"C:\Users\monza\Desktop\REPO\python-programming-M-NS-JILDESTRAND\Labs\Lab3\labelled_data.csv",
    labeled_data,
    delimiter=",",
    fmt=["%.16f", "%.16f", "%d"]
)

# Plotta punkterna och linjen
plt.figure(figsize=(6, 6), dpi=100)
plt.title("Klassificering av punkter")
plt.plot(x_line, y_line, label="y = -0.9x + 0.5", color="green")
plt.scatter(x_above, y_above, c="red", label="Label 1 above")
plt.scatter(x_below, y_below, c="blue", label="Label 0 below")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc="upper left")
plt.grid(True)
plt.show()
