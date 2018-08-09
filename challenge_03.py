import re

# Read in file
with open('challenge_03_input.txt') as file:
    data = file.readlines()

# Make it all 1 line
data_str = ''.join(data).replace('\n', '')

# Regex
results = re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', data_str)

# Get middle character
''.join([x[4] for x in results])
