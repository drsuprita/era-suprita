import pandas as pd

data = {
    "Price": ["$100.50", "$200.75", "$150.00"],
    "Date": ["2025-01-01", "2025-01-02", "2025-01-03"]
}

df = pd.DataFrame(data)
print("Before Conversion:")
print(df.dtypes)