import pandas as pd

# Read in file
with open('challenge_02_input.txt') as file:
    data = file.readlines()

# Make it all 1 line
data_str = ''.join(data).replace('\n', '')

# Make a pandas series out of it
s = pd.Series(list(data_str))

# Get unique letters - There are multiple ways...I really want the index of the letters
counts = s.groupby(s).transform('count')
letters_idx = counts.loc[counts == 1].index.values

# Actual answer
''.join(s.loc[letters_idx].values)

# equality
