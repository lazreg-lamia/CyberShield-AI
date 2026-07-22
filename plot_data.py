import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/students.csv")

df.plot(x="Name", y="Age", kind="bar")

plt.title("Students Age")
plt.xlabel("Student")
plt.ylabel("Age")

plt.show()