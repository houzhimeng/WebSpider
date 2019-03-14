import subprocess
# subprocess.call(['df', '-h'])
x = subprocess.check_output(["echo", "Hello World!"], shell=True)

print(x)

# p = subprocess.Popen(["ping","www.baidu.com"], stdout=subprocess.PIPE)
# p.wait()
# p.stdout.read().decode('utf8')