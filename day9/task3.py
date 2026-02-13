import pandas as pd

# Sample DataFrame
data = {
    "Location": [" New York", "new york", "NEW YORK ", " New York "]
}

df = pd.DataFrame(data)

print("Before Cleaning:")
print(df["Location"].unique())