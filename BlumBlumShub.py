import random
import math
from Fermat import Fermat

class BlumBlumShub:


    # Used to check if a certain parameter is congruent to 3 mod(4)
    def __congruence_check(self, n):
        return not ((n-3) % 4)
    
    # gcd using euclides, a < b
    # Must be iterative, otherwise may break pythons recursion limit
    def __gcd(self, a, b):
        if a > b: return -1;
        while a != 0:
            a, b = b % a, a
        return b



    # Actually executing the algorithms
    # pq = modulator
    # seed must be coprime of pq
    def exec(self, p, q, seed, i, gen_size):
        if(not (self.__congruence_check(p) and self.__congruence_check(q))):
            return
        if self.__gcd(seed, p*q) != 1:
            return

        pseudo_random_numbers = []

        for i in range(i):
            random_num = 0
            m = p*q
            lst = seed
            for j in range(gen_size):
                lst = pow(lst, 2, m)
                random_num = (random_num << 1) | (lst & 1)

            pseudo_random_numbers.append(random_num)
        
        return pseudo_random_numbers


    # Used for testing purpouses
    # Returns a prime number of size = bit_size and congruent to 3 mod 4
    # Uses Fermat with 30 iterations in order to check primality
    def get_param(self, bit_size):
        prime_test = Fermat()
        rand = random.getrandbits(bit_size)
        while (not prime_test.exec(rand, 30)) or (not self.__congruence_check(rand)):
            rand = random.getrandbits(bit_size)
        return rand
    # Used for testing purpouses
    # Return a seed that is coprime of pq
    def get_seed(self, bit_size, p, q):
        rand = random.getrandbits(bit_size)
        while self.__gcd(rand, p*q) != 1:
            rand = random.getrandbits(bit_size)
        return rand
