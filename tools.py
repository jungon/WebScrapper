import numpy as np


def get_random_ua():
    random_ua = ''
    ua_file = 'ua_file.txt'
    try:
        with open(ua_file, encoding='utf-8') as f:
            lines = f.readlines()
        if len(lines) > 0:
            while not random_ua.strip():
                prng = np.random.RandomState()
                index = prng.permutation(len(lines)-1)
                idx = np.asarray(index, dtype=np.integer)[0]
                random_ua = lines[int(idx)].replace('\n', '')
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    finally:
        return random_ua
