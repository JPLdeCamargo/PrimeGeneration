import random
from MillerRabin import MillerRabin

# Inherits MillerRobin in order to use _modular_power
class Fermat(MillerRabin):

    # Simple Fermat implementation, 
    # only if the result from the modular exponentiation is not 1
    def exec(self, n, n_tests):
        if(n%2 == 0) : return False

        for i in range(n_tests):
            a = random.randint(2, n-2)
            mod_val = self._modular_power(a, n-1, n)
            if mod_val != 1:
                return False

        return True

    # wrapper used in testing, fixed n_tests to 50
    def wrapper(self, n):
        return self.exec(n, 50)
