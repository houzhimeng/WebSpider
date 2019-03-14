import os
path = os.getcwd()
print(path)

path2 = os.path.split(path)
print(path2)
print(os.path.dirname(path))