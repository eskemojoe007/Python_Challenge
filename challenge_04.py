import requests

link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

val = b'12345'
while val.isdigit():
    r = requests.get(link, {'nothing': int(val)})
    r_str = r.content
    print(r_str)
    val = r_str.split()[-1]

# Start again after break
val = '{}'.format(int(16044/2))
while val.isdigit():
    r = requests.get(link, {'nothing': int(val)})
    r_str = r.content
    print(r_str)
    val = r_str.split()[-1]
# val = 'peak.html'
