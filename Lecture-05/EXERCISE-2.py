def generate_primes(n):
    primes = []

    for number in range(2, n + 1):
        is_prime = True

        for divisor in range(2, number):
            if number % divisor == 0:  #นำ number หารด้วย divisor แล้วเหลือเศษ 0
                is_prime = False
                break

        if is_prime:
            primes.append(number)

    return primes


# Example usage
print(generate_primes(10))  # Output: [2, 3, 5, 7]
print(generate_primes(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
print(generate_primes(1))   # Output: []
print(generate_primes(2))   # Output: [2]