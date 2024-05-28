from BlumBlumShub import BlumBlumShub
from LaggedFibo import LaggedFibo

import time
import random

def blum_blum_shub_test(gen_size):

    # Time for getting paramaters is not relevant to this benchmark
    algo = BlumBlumShub()
    p = algo.get_param(gen_size//2)
    q = algo.get_param(gen_size//2)
    seed = algo.get_seed(gen_size, p, q)


    start = time.time()
    vals = algo.exec(p, q, seed, 1000, gen_size)
    print(len(vals))
    end = time.time()

    print(end - start)
    return end - start

def lagged_fibo_test(gen_size):

    # Time for getting paramaters is not relevant to this benchmark
    offset_high = 50
    offset_low = 20
    initial_state = [random.getrandbits(gen_size) for i in range(offset_high)]
    modulator = random.getrandbits(gen_size)

    lagged_fibo = LaggedFibo()

    start = time.time()
    vals = lagged_fibo.exec(offset_low, offset_high, modulator, initial_state, 1000)
    end = time.time()

    print(end - start)
    return end - start




if __name__ == "__main__":
    test_sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    res = []
    for i in test_sizes:
        res.append(blum_blum_shub_test(i)*1000)
    print(res)



# Blumblum values
# [7.583856582641602, 10.931730270385742, 18.309354782104492, 35.85672378540039, 52.02293395996094, 88.73677253723145, 111.0832691192627, 495.29480934143066, 2520.764112472534, 16617.390632629395, 118587.07666397095]
# Lagged fibo values
# [0.09489059448242188, 0.06389617919921875, 0.07915496826171875, 0.06508827209472656, 0.06556510925292969, 0.07939338684082031, 0.06532669067382812, 0.09560585021972656, 0.12540817260742188, 0.141143798828125, 0.44536590576171875]
