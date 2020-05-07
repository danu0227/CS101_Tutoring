def sieve(n):
    candidates = list(range(2, n))
    i = 0
    while i < len(candidates):
        prime = candidates[i]
        j = i
        while j < len(candidates):
            if candidates[j] % prime == 0:
                candidates.pop(j)
            else:
                j = j + 1
            print("i:", i, "j", j, candidates)
        i = i + 1

sieve(50)
