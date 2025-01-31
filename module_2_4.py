numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
# Перебираем каждый элемент в списке numbers
for num in numbers:
    if num <= 1:  # Пропускаем 1, так как оно не являются
        # ни простым, ни составным числом
        continue
    is_prime = True  # Предполагаем, что число простое
    for i in range(2, num):
        if num % i == 0:  # Если num делится на i,
            # то оно не простое
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)
print("Простые числа:", primes)
print("Не простые числа:", not_primes)
