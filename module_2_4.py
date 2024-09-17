numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes =list()
def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a // 2 + 1)):
        if a % i == 0:
            return False
    else:
        return True
for i in numbers:
    for j in range(1, i):
       if is_prime(i) == True:
           primes.append(i)
           break
       elif is_prime(i) == False:
           not_primes.append(i)
           break

print('primes: ', primes)
print('not_primes: ', not_primes)