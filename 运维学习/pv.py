import re
import time

ips = []
with open('./access1.log') as f:
    for line in f:
        if line.startswith('100'):
            ips.append(line.split()[0])


print(ips)

print("pv is {0}".format(len(ips)))
print("uv is {0}".format(len(set(ips))))
