from multiprocessing.dummy import Pool

def calc(num):
    return num * num

pool = Pool(3)
o = [ x for x in range(10)]
he = pool.map(calc, o)
print(f'打印该循环数字是: {he}')
