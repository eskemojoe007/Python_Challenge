import requests
import cv2
import numpy as np

# %% Download Image
url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
r = requests.get(url, allow_redirects=True)

with open('oxygen.png', 'wb') as f:
    f.write(r.content)

# %% Now we have to read the gradients of the image
img = cv2.imread('oxygen.png')


for row in img:
    if len(set(row[0])) <= 1:
        print('Found GREY MOTHER FUCKER')
        grey_row = row
        break

just_greys = []
for col in grey_row:
    print(col)
    if len(set(col)) <= 1:
        just_greys.append(col[0])

a = np.array(just_greys)

print(''.join(chr(x) for x in a[4::7]))

new_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join(chr(x) for x in new_list))

# integrity
