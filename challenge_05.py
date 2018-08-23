import pickle

with open('banner.p', 'rb') as f:
    p = pickle.load(f)

print(p)
for line in p:
    print(''.join([i * letter for i, letter in line]))

#channel
