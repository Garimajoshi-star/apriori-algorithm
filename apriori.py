# Importing libraries.
import numpy as np
import pandas as pd
from apyori import apriori

# Importing dataset.
Basket_items = pd.read_csv("items_list.csv")
Basket_items

# Importing dataset without any header row.
Basket_items = pd.read_csv("items_list.csv", header = None)
Basket_items.head()

# Analysing shape of entire itemset.
Basket_items.shape

# Performing data pre-processing.
records = []
for i in range(0,30):
    records.append([str(Basket_items.values[i,j]) for j in range(0,6)])

# Applying apriori algorithm.
association_rules = apriori(records, min_support = 0.46, min_confidence = 0.7, min_lift = 1.2, min_length = 2)
association_results = list(association_rules)

# Identifying rules mined by apriori class.
print(len(association_rules))

# Displaying the mined rule.
print(association_results)
