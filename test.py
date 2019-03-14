import  subprocess



Cen = subprocess.check_output('ps -ef',shell=True).decode().strip()

print(Cen)