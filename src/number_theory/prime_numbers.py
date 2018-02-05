"""
    module to operations with prime numbers
"""
def check_prime(self, number):
        """
            it's not the best solution
        """
        return all([number % i for i in range(2, number)])

def double_next_prime(self, value):
	i = 1
	value = 2 * value

    while not check_prime(value):
            value += i

    return value