import requests
import zipfile
import os

# %% Inputs
zip_name = 'channel.zip'
directory = os.path.splitext(zip_name)[0]
url = 'http://www.pythonchallenge.com/pc/def/{}'.format(zip_name)

# %% Download the Zip
r = requests.get(url)
with open(zip_name, 'wb') as f:
    f.write(r.content)

# %% Extract the zip
zip_ref = zipfile.ZipFile(zip_name, 'r')
if not os.path.exists(directory):
    os.makedirs(directory)
zip_ref.extractall(path=directory)

# %% Start the follow through


def open_read_file(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    comment = zip_ref.getinfo(os.path.basename(path)).comment

    return lines[0].split()[-1], comment


val = '90052'
comments = []
while val.isdigit():
    val, comment = open_read_file(os.path.join(directory, '{}.txt'.format(val)))
    comments.append(comment.decode('utf-8'))

print(''.join(comments))
# oxygen
