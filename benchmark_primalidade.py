from LaggedFibo import LaggedFibo
from Fermat import Fermat
from MillerRabin import MillerRabin

import random
import time


if __name__ == "__main__":
    lagged = LaggedFibo()

    test_sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    random_primes = []
    for i in test_sizes:
        offset_high = 7
        offset_low = 3
        initial_state = [random.getrandbits(i) for j in range(offset_high)]

        miller = MillerRabin()
        start = time.time()
        random_prime = lagged.exec_until_prime(miller.wrapper, offset_low, offset_high, random.getrandbits(i), initial_state)
        end = time.time()
        print(random_prime)
        print()
        print(i)
        print(end-start)
        print()
    print(random_primes)