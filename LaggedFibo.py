from BlumBlumShub import BlumBlumShub
import random

class LaggedFibo:


    # Very minimal Lagged Fibonacci implementation, initial_state size must be
    # the same as offset_high
    # This implementation utilizes XOR as the binary operation
    def exec(self, offset_low, offset_high, modulator, initial_state, iterations):
        initial_state_size = len(initial_state)
        if initial_state_size < offset_high: return []

        end = initial_state_size + iterations
        for i in range(initial_state_size, end):
            new_random_num = (initial_state[i-offset_low] ^ initial_state[i-offset_high]) % modulator
            initial_state.append(new_random_num)
        
        return initial_state[initial_state_size:]

    # Used to get a prime number, is_prime is used as the function that checks primality,
    # After generating a single random number, keep incrementing its value until it has become a prime
    def exec_until_prime(self, is_prime, offset_low, offset_high, modulator, initial_state):
        initial_state_size = len(initial_state)
        if initial_state_size < offset_high: return []

        random_prime = -1;
        i = initial_state_size
        new_random_num = (initial_state[i-offset_low] ^ initial_state[i-offset_high]) % modulator
        if new_random_num % 2 == 0: new_random_num += 1
        while True:
            if is_prime(new_random_num):
                random_prime = new_random_num
                break
            new_random_num += 2

        
        return random_prime
