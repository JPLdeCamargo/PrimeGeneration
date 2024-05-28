import math
import random

class MillerRabin:
    # Modular exponentiation function
    def _modular_power(self, base, exp, mod):
        exp = int(exp)
        if mod == 1: return 0
        result = 1
        base = base % mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            exp //= 2
            base = (base * base) % mod
        return result



    def exec(self, n, n_tests):
        if(n%2 == 0) : return False

        s = 0
        d = n - 1
        # Getting s and d by dividing n-1 by 2 multiple times
        while(d%2 == 0):
            s += 1
            # Caution, always use // instead of /, floating point arithmetic
            # plummets the performance
            d //= 2
        
        for i in range(n_tests):
            a = random.randint(2, n-2)
            x = self._modular_power(a, d, n)
            y = self._modular_power(x, 2, n)

            # All of these calculations makes this algorithm slower than Fermat
            # depending on the value of a, the value of s can be quite significant
            for j in range(s):
                y = self._modular_power(x, 2, n)
                if y == 1 and x != 1 and x != (n-1):
                    return False
                x = y
            
            if y != 1:
                return False
        
        return True
    
    # wrapper used in testing, fixed n_tests to 50
    def wrapper(self, n):
        return self.exec(n, 50)
        
