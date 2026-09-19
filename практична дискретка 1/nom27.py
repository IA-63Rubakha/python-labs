import numpy as np
a = np.random.randint(1, 100, size=(5, 5))
print("Матриця:")
print(a)
print("Максимум по стовпцях:", a.max(axis=0))
print("Мінімум по стовпцях:", a.min(axis=0))
print("Максимум по рядках:", a.max(axis=1))
print("Мінімум по рядках:", a.min(axis=1))