import math
import random


def generate_two_prime_numbers(max_value):
    prime_numbers = []
    for num in range(1001, max_value + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)

    x = random.choice(prime_numbers)
    y = x
    while y == x:
        y = random.choice(prime_numbers)

    return x, y


def are_coprime(a, b):
    return math.gcd(a, b) == 1


def find_e(phi):
    coprime_numbers = []
    for num in range(2, 10000):
        if are_coprime(num, phi):
            coprime_numbers.append(num)

    return random.choice(coprime_numbers)


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


def modular_inverse(a, b):
    gcd, x, y = extended_gcd(a, b)
    if gcd != 1:
        print('Err')
    else:
        return x % b


if __name__ == '__main__':
    x, y = generate_two_prime_numbers(1500)
    n = x * y
    phi = (x - 1) * (y - 1)
    e = find_e(phi)
    d = modular_inverse(e, phi)
    public_key = (n, e)
    private_key = (n, d)
    f = open("public_key", "w")
    f.write(str(public_key))
    f.close()
    f = open("private_key", "w")
    f.write(str(private_key))
    f.close()
