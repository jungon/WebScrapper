import numpy as np
import time


delays = [12, 3, 9, 21, 5, 6, 19, 7, 33, 11, 2, 17, 4]


def get_random_ua():
    delay = np.random.choice(delays)
    time.sleep(delay)

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
