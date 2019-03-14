
d = {}
with open('./access1.log') as f:
    for line in f:
        key = line.split()[8]
        d.setdefault(key, 0)
        d[key] += 1
        sum_requests = 0
        error_request = 0
        # print(d)

        for key, val in d.items():
            if int(key) >= 200:
                error_request += val
            sum_requests += val
        print('eror rate : {0:.2f}%'.format(error_request * 100.0 / sum_requests))

