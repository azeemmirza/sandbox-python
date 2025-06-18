import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

titanic = sns.load_dataset('titanic')

print("First 10 rows of the dataset:")
print(titanic.head(10))

print("\nDataset Information:")
titanic.info()