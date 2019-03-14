#-*- coding: UTF-8 -*-
import subprocess
output = subprocess.check_output(['df','-h'])
out2 = output.decode('utf-8')

for line in out2[1: -1]:
    print(line)

