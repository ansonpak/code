max = 10000
primes = range(max)
 
for p in primes:
    if p > 1:
        print(p)
    for s in primes[p*2::p]:
        primes[s] = 0
print(primes)