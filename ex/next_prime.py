def next_prime(number):
    while True:
        number += 1
        divisors = 0
        for c in range(1,number+1):
            if number % c == 0:
                divisors += 1
        if divisors == 2:
            break
    return number

print(next_prime(10001))