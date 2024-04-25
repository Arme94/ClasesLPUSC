def is_prime(n):
    return len(list(filter(lambda x: n % x == 0, range(2, n)))) == 0

def list_primes_lazy(n):
    i = 2
    while i <= n:
        if is_prime(i):
            yield i
        i += 1

n = int(input("Select the number n >= 30: "))
gen_primos = list_primes_lazy(n)
first_10 = [next(gen_primos) for _ in range(10)]
print(f"First 10: \n{first_10}")

finish = False
while not finish:
    r = input("Generate 10 more? (y/n): ")
    if r == "y":
        try:
            next_10 = [next(gen_primos) for _ in range(10)]
            print(f"Next 10: \n{next_10}")
        except StopIteration:
            print("No more primes")
            finish = True
    else:
        finish = True
        print("Goodbye!")