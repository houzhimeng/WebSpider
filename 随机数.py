import random
import string

# 第一种方法

seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
sa = []
for i in range(32):
    sa.append(random.choice(seed))
salt = ''.join(sa)
print(salt)

resutl = ''.join([random.choice(seed) for i in range(6)]) 

salt2 = ''.join(random.sample(string.ascii_letters + string.digits, 16))
print(salt2)