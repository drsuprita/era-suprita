import pandas as pd
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
cleaned_usernames = usernames.str.strip().str.lower()
print("Cleaned Usernames:")
print(cleaned_usernames)
print("\nNames containing letter 'a':")
print(cleaned_usernames.str.contains('a'))