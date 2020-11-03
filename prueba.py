from fork import USERNAME
from fork import PASSWORD
import os
import requests

x = 5
y = 6
z = x+y
text = "Z=11"
if z == 11:
    print(z)
    print(x)
print(os.chdir("/"))
print(text)
r = requests.get('?access_token=')
tokens = text.split("=", (1))
print(tokens)
numbers = [1, 2, 3]
print(numbers)
print(USERNAME)
print(PASSWORD)
